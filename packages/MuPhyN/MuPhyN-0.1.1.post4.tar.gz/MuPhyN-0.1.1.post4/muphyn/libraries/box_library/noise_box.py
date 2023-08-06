#-----------------------------------
# Imports
#-----------------------------------

from typing import List
from random import seed
from random import random

#-----------------------------------
# Functions
#-----------------------------------

def _init_noise_box (box, simulation_params) -> List : 
    
    if box['apply_seed'] :
        seed(box['seed'])

    box['min'] = box['mean_value'] - (box['amplitude'] / 2)

def _function_noise_box (box, event_) -> List :
    return box['amplitude'] * random() + box['min']