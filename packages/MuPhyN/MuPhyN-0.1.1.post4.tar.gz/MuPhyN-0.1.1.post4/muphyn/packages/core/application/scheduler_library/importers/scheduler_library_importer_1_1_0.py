#-----------------------------------
# Imports
#-----------------------------------

from typing import Dict
import importlib
import os
import sys
import yaml

from muphyn.packages.core.base import loadCode
from muphyn.packages.core.application.plci_core_parameter import Parameter
from muphyn.packages.core.application.scheduler_library.importers.abstract_scheduler_library_importer import AbstractSchedulerLibraryImporter
from muphyn.packages.core.application.scheduler_library.scheduler_library_data import SchedulerData
from muphyn.packages.core.base import LogManager

#-----------------------------------
# Class
#-----------------------------------

class SchedulerLibraryImporter (AbstractSchedulerLibraryImporter) : 
    """Est la V 1.1.0 de classes capable d'importer des planificateurs.
    
    Cette version supporte l'ajout de paramètres personnalisés pour un scheduler"""

    # -------------
    # Constructors
    # -------------
    
    def __init__ (self) :
        super().__init__()

    # -------------
    # Methods
    # -------------

    def import_scheduler_data (self, path : str, file_name : str, absolute_yaml_file : str, schedulers : Dict[str, SchedulerData]) -> Dict[str, SchedulerData] :
        
        absolute_py_file = path + '/' + file_name + '.py'

        with open(absolute_yaml_file) as yaml_file_data :
            
            file_data = yaml.load(yaml_file_data, Loader = yaml.FullLoader)

            if 'scheduler' in file_data:
                
                scheduler_data = file_data['scheduler']

                if scheduler_data['library'].startswith('Schedulers') :
                    
                    # Build library name
                    library_name = scheduler_data['library'] + "." + scheduler_data['name']

                    # Load Code
                    foo = loadCode(library_name, absolute_py_file)

                    # Define default scheduler method
                    if scheduler_data['scheduler_method'] == "None" : 
                        scheduler_method = lambda box : LogManager().error("No scheduler method")
                    else :
                        scheduler_method = getattr(foo, scheduler_data['scheduler_method'])

                    # Extract informations
                    schedulerName = "<UKNOWN NAME>" if "name" not in scheduler_data else scheduler_data['name']
                    schedulerLibrary = "<UKNOWN LIBRARY>" if "library" not in scheduler_data else scheduler_data['library']
                    schedulerCreator = "<UKNOWN CREATOR>" if "creator" not in scheduler_data else scheduler_data['creator']
                    schedulerCreationDate = "<UKNOWN CREATION DATE>" if "date_creation" not in scheduler_data else scheduler_data['date_creation']
                    schedulerVersion = "<UKNOWN VERSION>" if "version" not in scheduler_data else scheduler_data['version']

                    # Get parameters
                    if "parameters" in scheduler_data:
                        parameters = [Parameter.fromDict(parameter) for parameter in scheduler_data["parameters"]]
                    else:
                        parameters = []


                    return {
                        'library_name' : library_name, 
                        'scheduler_data' : SchedulerData(
                                path = os.path.join(path, file_name),
                                scheduler_name = schedulerName,
                                scheduler_library = schedulerLibrary,
                                scheduler_method = scheduler_method,
                                creator = schedulerCreator,
                                date_created = schedulerCreationDate,
                                version = schedulerVersion,
                                parameters = parameters
                            )
                    }