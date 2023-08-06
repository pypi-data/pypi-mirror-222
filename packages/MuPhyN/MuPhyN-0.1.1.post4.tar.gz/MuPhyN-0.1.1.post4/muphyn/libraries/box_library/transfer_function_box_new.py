# -----------------------------------
# Imports
# -----------------------------------
from typing import List
from scipy.integrate import solve_ivp

from PyQt6.QtCore import QSizeF
from PyQt6.QtGui import QFontMetrics

from muphyn.packages.interface.models.graphical_models.box_model import BoxModel
from muphyn.packages.interface.base.math_expression_painter import mathTex_to_QImage
from muphyn.packages.core.application import Box, SchedulerEvent, SchedulerParams

# Library imports
from utils.TransferFunction import TransferFunction

# -----------------------------------
# Functions
# -----------------------------------
def _updateDisplayedValue(boxModel: BoxModel):
    # Build numerator string
    num = TransferFunction.coefFromString(boxModel.get_parameter('numerator')["value"])
    numStr = TransferFunction.equationStringFromCoeffs(num)

    # Build denominator string
    denom = TransferFunction.coefFromString(boxModel.get_parameter('denominator')["value"])
    denomStr = TransferFunction.equationStringFromCoeffs(denom)

    # Build horizontal ligne separator
    nUnderscore = max(len(numStr), len(denomStr))
    underscoreText = '_' * nUnderscore

    boxText = f"{numStr}\n{underscoreText}\n{denomStr}"
    width = boxModel._font_metrics_used.horizontalAdvance(underscoreText)
    boxModel.setValue(boxText)
    boxModel.setSize(QSizeF(width, boxModel.size.height()))

def _init_transfer_function(box: Box, simulation_params: SchedulerParams) -> None:
    
    transferFunction = TransferFunction.fromString(box["numerator"], box["denominator"], box["initial_value"], simulation_params.stop_time, simulation_params.step_time)
    box["transferFunction"] = transferFunction
    box["times"] = []
    box['last_timing'] = -1

def _function_transfer_function(box: Box, event_: SchedulerEvent):        

    
    if box['last_timing'] == event_.timing:    # if we are still on the current step, leave
        return None
    
    # Get Transfer Function object
    transferFunction: TransferFunction = box["transferFunction"]

    # Execute step
    lastTime = transferFunction.lastTime
    targetValue = box.input_values[0]
    
    # If never executed → force first step
    if lastTime == -1:
        status, time, out = transferFunction.stepSolve(targetValue)
        lastTime = time
        
    # Make simulation until pass the current time
    while event_.timing > lastTime and transferFunction.canRun:
        status, time, out = transferFunction.stepSolve(targetValue)
        lastTime = time
    
    # Get the value for the current time
    out = transferFunction.getValue(event_.timing)

    
    box['last_timing'] = event_.timing

    
    return out

def _end_transfer_function (box: Box) -> None :
    pass
