import numpy as np
from typing import Any, Union

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QAction, QFocusEvent
from PyQt6.QtWidgets import QHBoxLayout, QLineEdit

from muphyn.packages.core.base import LogManager, GlobalEnvVariablesManager, Regex
from muphyn.packages.core.application import DataType
from muphyn.packages.interface.application.widgets.data_property_widgets.abstract_property_widget import AbstractPropertyWidget
from muphyn.utils.paths import ROOT_DIR

class PropertyLineEdit(AbstractPropertyWidget):

    def __init__(self, parameterToEdit, propertyType: DataType, parent = None, flags: Qt.WindowType = Qt.WindowType.Widget) -> None:
        super().__init__(parent, flags)

        # Init Layout
        layout = QHBoxLayout()

        # 
        self._parameterToEdit = parameterToEdit
        self._propertyType: DataType = propertyType

        # Init Line Edit
        self._lineEdit = QLineEdit()
        self._lineEdit.editingFinished.connect(self.line_edit_editing_finished)
        self._lineEditTooltip = QAction(
            QIcon(ROOT_DIR + "/" +"packages/interface/assets/GeneralIcons/error.svg"), 
            ""
        )

        # Set Layout
        layout.addWidget(self._lineEdit)
        self.setLayout(layout)

        # 
        self._isVariable = False
    
    # ------------
    #  Properties
    # ------------
    @property
    def parameterToEdit(self) -> dict:
        return self._parameterToEdit
    
    @property
    def propertyType(self):
        return self._propertyType
    
    # ------------------
    #  Abstract Methods
    # ------------------
    def checkType(self, value: Any):
        raise(NotImplementedError(f"{self.__class__.__name__}.checkType not implemented yet"))
        
    def setTypedValue(self, value: str):
        raise(NotImplementedError(f"{self.__class__.__name__}.setTypedValue not implemented yet"))

    # ---------
    #  Methods
    # ---------
    def setError(self, isError: bool, message: str = None):
        if isError:
            # Test if Tool Tip Icon is in Line Edit
            if not self._lineEditTooltip in self._lineEdit.actions():
                self._lineEdit.addAction(
                    self._lineEditTooltip, 
                    QLineEdit.ActionPosition.TrailingPosition
                )

            # Set Tool Tip message
            if message is not None:
                self._lineEditTooltip.setToolTip(message)
            
        else:
            # Remove tooltip Icon
            if self._lineEditTooltip in self._lineEdit.actions():
                self._lineEdit.removeAction(self._lineEditTooltip)
    
    def setValue(self, newValue: str):
        # Remove leading and ending whitespaces
        newValue = str(newValue).strip()

        # Handle variable name case
        if newValue in GlobalEnvVariablesManager().global_vars:
            # Get global variable
            global_var = GlobalEnvVariablesManager().global_vars[newValue]

            # Set Property Line Edit as variable value
            self._isVariable = True

            if self.checkType(global_var):
                # Set Checked
                self.validValue(newValue)
            else:
                self.setError(True, f"{self._propertyType} object expected: {type(global_var)} instead")
                LogManager().error(TypeError(f"{self._propertyType} object expected: {type(global_var)} instead"))


        # Handle typed value case
        elif self.checkType(newValue):
            self._isVariable = False
            self.setTypedValue(newValue)

        else:
            self._isVariable = False
            self.setError(True, f"Invalid input: Please set a {self._propertyType} value or an existing variable name")
            LogManager().error(TypeError(f"Invalid input: Not a int neither an existing variable name"))

    def validValue(self, newValue: Any):
        # Save value
        self._value = newValue

        # Set Checked
        self._lineEdit.setText(str(newValue))

        # Emit value changed
        self.valueChanged.emit()

        # Reset Error
        self.setError(False)

    # -------
    #  Slots
    # -------
    def line_edit_editing_finished(self):
        self.setValue(self._lineEdit.text())


class BooleanPropertyLineEdit(PropertyLineEdit):

    def __init__(self, parameterToEdit, parent=None, flags: Qt.WindowType = Qt.WindowType.Widget) -> None:
        super().__init__(parameterToEdit, DataType.INT, parent, flags)
        
    def checkType(self, value: Any):
        if type(value) == str:
            return Regex.isBoolean(value)
        else:
            return type(value) == bool

    def setTypedValue(self, value: Union[bool, str]):
        if type(value) == bool: 
            self.validValue(value)
        elif type(value) == str:
            self.validValue(Regex.isTrueValue(value))

class IntegerPropertyLineEdit(PropertyLineEdit):

    def __init__(self, parameterToEdit, parent=None, flags: Qt.WindowType = Qt.WindowType.Widget) -> None:
        super().__init__(parameterToEdit, DataType.INT, parent, flags)

        # Get 64 bits integer informations
        int64_info = np.iinfo(np.int64)

        # Calculate min value
        self._minValue = int64_info.min
        if "min" in parameterToEdit:
            min_value = parameterToEdit["min"]
            try:
                self._minValue = max(int(float(min_value)), self._minValue)
            except:
                LogManager().error(f"IntegerPropertyWidget.__init__(): given 'min' value not a integer: {min_value}")

        # Calculate max value
        self._maxValue = int64_info.max
        if "max" in parameterToEdit:
            max_value = parameterToEdit["max"]
            try:
                self._maxValue = min(int(float(max_value)), self._maxValue)
            except:
                LogManager().error(f"IntegerPropertyWidget.__init__(): given 'max' value not a integer: {max_value}")
        
    def checkType(self, value: Any):
        if type(value) == str:
            return Regex.isInteger(value) or Regex.isDotFloat(value)
        else:
            return type(value) == int or type(value) == float

    def setTypedValue(self, value: Union[float, int, str]):
        # Handle from numeric type conversion
        if type(value) == float or type(value) == int:
            # Convert to int
            value = int(value)

        # Handle from string type conversion
        elif type(value) == str:
            if value == "" or value == "+" or value == "-":
                self.validValue(0)
            else:
                # Handle Comma decimal separator
                if Regex.isCommaFloat(value):
                    value = value.replace(",", ".")

                # Convert to int
                value = int(float(value))

        # Handle other types
        else:
            raise(AttributeError(f"value attribute has an unsupported type: {type(value)} instead of float or int or str"))

        # Handle limits
        if value > self._maxValue:
            value = self._maxValue
        elif value < self._minValue:
            value = self._value

        # Set valid value
        self.validValue(value)

class FloatPropertyLineEdit(PropertyLineEdit):

    def __init__(self, parameterToEdit, parent=None, flags: Qt.WindowType = Qt.WindowType.Widget) -> None:
        super().__init__(parameterToEdit, DataType.FLOAT, parent, flags)

        # Get min/max values
        self._minValue = -np.inf
        # self._minValue = -sys.float_info.max
        if "min" in parameterToEdit:
            minValue = parameterToEdit["min"]
            try:
                self._minValue = max(float(minValue), self._minValue)
            except:
                LogManager().error(f"DoublePropertyWidget.__init__(): given 'min' value not a float: {minValue}")


        self._maxValue = np.inf
        # self._maxValue = sys.float_info.max
        if "max" in parameterToEdit:
            maxValue = parameterToEdit["max"]
            try:
                self._maxValue = min(float(maxValue), self._maxValue)
            except:
                LogManager().error(f"DoublePropertyWidget.__init__(): given 'max' value not a float: {maxValue}")
        
    def checkType(self, value: Any):
        if type(value) == str:
            return Regex.isInteger(value) or Regex.isDotFloat(value)
        else:
            return type(value) == int or type(value) == float

    def setTypedValue(self, value: Union[float, int, str]):
        # Handle from numeric type conversion
        if type(value) == float or type(value) == int:
            # Convert to float
            value = float(value)

        # Handle from string type conversion
        elif type(value) == str:
            if value == "" or value == "+" or value == "-":
                value = 0.0
            elif value == "inf":
                value = np.inf
            else:
                # Handle Comma decimal separator
                if Regex.isCommaFloat(value):
                    value = value.replace(",", ".")

                # Convert to float
                value = float(value)

        # Handle other types
        else:
            raise(AttributeError(f"value attribute has an unsupported type: {type(value)} instead of float or int or str"))
        
        # Handle limits
        if value > self._maxValue:
            value = self._maxValue
        elif value < self._minValue:
            value = self._value

        # Set valid value
        self.validValue(value)

class StringPropertyLineEdit(PropertyLineEdit):

    def __init__(self, parameterToEdit, parent=None, flags: Qt.WindowType = Qt.WindowType.Widget) -> None:
        super().__init__(parameterToEdit, DataType.STRING, parent, flags)

        # Set limit characters
        self._limitCharacters = -1
        if "maxLength" in parameterToEdit:
            limitCharacters = parameterToEdit["maxLength"]
            try:
                self._limitCharacters = max(int(limitCharacters), self._limitCharacters)
            except:
                LogManager().error(f"StringPropertyWidget.__init__(): given 'maxLength' value not a valid value: {limitCharacters}")
        self._lineEdit.setMaxLength(self._limitCharacters)

        # Active Line Edit focus event
        self._lineEdit.focusInEvent = self.lineEditFocusIn
        self._lineEdit.editingFinished.connect(self.addQuotes)

        # 
        self.addQuotes()

    def addQuotes(self):
        if not self._isVariable:
            # Update max characters length
            if self._limitCharacters > -1:
                self._lineEdit.setMaxLength(self._limitCharacters+2)
                
            # Add quotes from displayed text
            self._lineEdit.setText(f"\"{self.value}\"")
        
    def checkType(self, value: Any):
        return type(value) == str
    
    def removeQuotes(self):
        if not self._isVariable:
            # Remove quotes from displayed text
            self._lineEdit.setText(f"{self.value}")

            # Update max characters length
            if self._limitCharacters > -1:
                self._lineEdit.setMaxLength(self._limitCharacters)

    def setTypedValue(self, value: str):
        if Regex.isStringLiteral(value):
            value = value[1:-1]
        elif type(value) == str:
            pass
        else:
            raise(AttributeError(f"value attribute has an unsupported type: {type(value)} instead of str"))
        
        # 
        self._isQuotedValue = True
        
        # Set valid value
        self.validValue(value)
    
    def lineEditFocusIn(self, focusEvent: QFocusEvent) -> None:
        # Remove quotes
        self.removeQuotes()
        return QLineEdit.focusInEvent(self._lineEdit, focusEvent)