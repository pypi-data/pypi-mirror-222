#-----------------------------------
# Imports
#-----------------------------------

from muphyn.packages.interface.models.graphical_models.box_model import BoxModel

from muphyn.packages.core.application import Box, SchedulerEvent

#-----------------------------------
# Functions
#-----------------------------------
def _update_box_value(box_model: BoxModel):
    box_model.setValue(box_model["gain"])

def _function_amplifier_box (box: Box, event_: SchedulerEvent):
    return box['gain'] * box.get_input(0).value