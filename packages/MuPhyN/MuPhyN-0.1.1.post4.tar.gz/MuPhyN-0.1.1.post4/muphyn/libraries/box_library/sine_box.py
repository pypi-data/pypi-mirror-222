#-----------------------------------
# Imports
#-----------------------------------

from typing import List
from numpy import sin

#-----------------------------------
# Functions
#-----------------------------------

def _init_sine_box (box, simulation_params) -> None :

    if not 'amplitude' in box :
        box['amplitude'] = 1.0

    if not 'pulsation' in box :
        box['pulsation'] = 1.0
    
    if not 'phase' in box :
        box['phase'] = 0.0

def _function_sine_box (box, event_) -> List :     
    return box['amplitude'] * sin((event_.timing * box['pulsation']) + box['phase'] )