#-----------------------------------
# Imports
#-----------------------------------

from typing import List

from muphyn.packages.core.application import Box, SchedulerEvent, SchedulerParams
from muphyn.packages.interface.models.graphical_models.box_model import BoxModel

#-----------------------------------
# Functions
#-----------------------------------

def _init_integrator_box (box: BoxModel, simulation_params: SchedulerParams) -> None :
    box['last_output'] = 0
    box['last_input'] = 0
    box['last_timing'] = 0


def _function_integrator_box (box: Box, event_: SchedulerEvent) -> List:
    input_ = box.input_values[0]

    if event_.timing == 0 :
        return None

    if box['last_timing'] == event_.timing :
        return None

    box['last_timing'] = event_.timing

    v = (event_.step_time * (input_ + box['last_input']) / 2) + box['last_output']

    box['last_output'] = v
    box['last_input'] = input_

    return v