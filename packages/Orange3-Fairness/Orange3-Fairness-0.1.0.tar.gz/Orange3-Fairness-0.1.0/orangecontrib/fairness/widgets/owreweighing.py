from typing import Optional

from Orange.widgets import gui
from Orange.widgets.widget import Input, Output, OWWidget
from Orange.data import Table, Domain, ContinuousVariable
from Orange.preprocess import preprocess

from aif360.algorithms.preprocessing import Reweighing as ReweighingAlgorithm

from orangecontrib.fairness.widgets.utils import table_to_standard_dataset, check_fairness_data


class MzCom:
    # The __init__ method is called when the class is created and can have as many arguments as you want. MzCom(model) creates an instance of the class
    # The __call__ method is called when the class is called, it must only have one argument, which is the data. MzCom(model)(data) calls the __call__ method of the class
    def __init__(self, model, original_domain=None):
        self.original_domain = original_domain
        self.model = model

    def __call__(self, data):
        # For creating a standard dataset we need the "Favorable class values" domain attribute, which may not be present in the data so we need to add it
        if not data.domain.class_var:
                data.domain.class_var = self.original_domain.class_var
        data, _, _ = table_to_standard_dataset(data)
        # Call the transform method of the model
        data = self.model.transform(data)
        # Return the weights
        return data.instance_weights

    # TODO: Check if this is ok
    InheritEq = True


class ReweighingModel():
    # This class doesn't need an __init__ method because it doesn't need any arguments when it is created
    # The __call__ method creates an instance of the ReweighingAlgorithm, fits it to the data and returns it
    def __call__(self, data):
        (
            standardDataset,
            privileged_groups,
            unprivileged_groups,
        ) = table_to_standard_dataset(data)
        reweighing = ReweighingAlgorithm(unprivileged_groups, privileged_groups)
        reweighing = reweighing.fit(standardDataset)
        return reweighing


class ReweighingTransform(preprocess.Preprocess):
    # The __call__ method applies the reweighing algorithm to the data and returns the data with the weights
    def __call__(self, data):
        # Create an instalce of the ReweighingModel, and call the __call__ method with the data as argument
        model = ReweighingModel()(data)
        # Create a new variable "weights" with the compute_value function, the compute_value function is the MzCom class, which when called calls the transform method of the model
        weights = ContinuousVariable("weights", compute_value=MzCom(model, original_domain=data.domain))
        # Alternative for the compute_value: compute_value=lambda data, model=model: transf(data, model)

        # Add the variable "weights" to the domain of the data
        new_data = data.transform(
            Domain(
                data.domain.attributes,
                data.domain.class_vars,
                data.domain.metas + (weights,),
            )
        )
        return new_data


class OWReweighing(OWWidget):
    name = "Reweighing"
    description = "Applies the reweighing algorithm to a dataset, which adjusts the weights of rows."
    icon = 'icons/reweighing.svg'
    # priority = 0

    want_control_area = False
    resizing_enabled = False

    # Define the inputs and outputs of the widget
    class Inputs:
        data = Input("Data", Table)

    class Outputs:
        data = Output("Preprocessed Data", Table)
        preprocessor = Output("Preprocessor", preprocess.Preprocess, dynamic=False)

    # Define the initial state of the widget (constructor)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.preprocessor = ReweighingTransform()
        self.Outputs.preprocessor.send(self.preprocessor)

        box = gui.vBox(self.mainArea, "Info")
        gui.widgetLabel(
            box,
            "This widget applies the reweighing algorithm to a dataset, which adjusts the weights of rows.\nThe input data must have the additional 'AsFairness' attributes and be without any missing values.",
        )

        self._data: Optional[Table] = None

    # Define what should happen when the input data is received
    @Inputs.data
    @check_fairness_data
    def set_data(self, data: Optional[Table]) -> None:
        if not data:
            return

        self._data = data

    def handleNewSignals(self):
        self.apply()

    def apply(self):
        if self._data is None:
            return

        preprocessed_data = self.preprocessor(self._data)

        self.Outputs.data.send(preprocessed_data)
        self.Outputs.preprocessor.send(self.preprocessor)
