#-----------------------------------
# Imports
#-----------------------------------

from typing import List
import numexpr as ne

from muphyn.packages.core.application import Box, SchedulerEvent

#-----------------------------------
# Functions
#-----------------------------------

def _function_formula_box (box: Box, event_: SchedulerEvent) -> List :
    # Add all input value to local env
    for inputSignal in box.inputSignals:
        locals()[inputSignal.input_name] = inputSignal.value

    # Get Formula
    formula = box["Formula"]

    # Calculate formula resolution
    v = float(ne.evaluate(formula))

    return v