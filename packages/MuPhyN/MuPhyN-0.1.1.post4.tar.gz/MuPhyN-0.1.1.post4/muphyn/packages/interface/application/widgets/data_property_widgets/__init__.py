
#
from muphyn.packages.core.application import DataType
from muphyn.packages.core.base import LogManager
from muphyn.packages.interface.properties_pages.abstract_properties_editor import AbstractPropertiesEditor

# DataType {FLOAT, INT, BOOLEAN, STRING}
from muphyn.packages.interface.application.widgets.data_property_widgets.basic_type_property_widgets import \
    UnknownTypePropertyWidget

# Datatype {ANYFILE, DIRECTORY, EXISTINGFILE, EXISTINGFILES}
from muphyn.packages.interface.application.widgets.data_property_widgets.path_property_widgets import \
    AnyFilePropertyWidget, DirectoryPropertyWidget, ExistingFilePropertyWidget, ExistingFilesPropertyWidget

from muphyn.packages.interface.application.widgets.data_property_widgets.typed_property_line_edit import \
    BooleanPropertyLineEdit, IntegerPropertyLineEdit, FloatPropertyLineEdit, StringPropertyLineEdit

from muphyn.packages.interface.application.widgets.data_property_widgets.choice_property_widget import ChoicePropertyWidget

def property_widget_factory(parameter_to_edit: dict) -> AbstractPropertiesEditor:
    # Get parameter type name
    param_type_name = parameter_to_edit["type"].__str__().lower()


    if param_type_name == str(DataType.BOOLEAN):
        return BooleanPropertyLineEdit(parameter_to_edit)

    elif param_type_name == str(DataType.FLOAT):
        return FloatPropertyLineEdit(parameter_to_edit)

    elif param_type_name == str(DataType.INT):
        return IntegerPropertyLineEdit(parameter_to_edit)

    elif param_type_name == str(DataType.STRING):
        return  StringPropertyLineEdit(parameter_to_edit)

    elif param_type_name == str(DataType.ANYFILE):
        return AnyFilePropertyWidget()

    elif param_type_name == str(DataType.DIRECTORY):
        return DirectoryPropertyWidget()

    elif param_type_name == str(DataType.EXISTINGFILE):
        return ExistingFilePropertyWidget()

    elif param_type_name == str(DataType.EXISTINGFILES):
        return ExistingFilesPropertyWidget()

    elif param_type_name == str(DataType.CHOICE):
        return ChoicePropertyWidget(parameter_to_edit)
    else:
        LogManager().error(f"Unsupported parameter type for : {param_type_name}")
        return UnknownTypePropertyWidget(param_type_name.__str__())
