#-----------------------------------
# Imports
#-----------------------------------
import traceback
from dataclasses import dataclass, field
from os import listdir, path
from typing import List, Any, Dict

from PyQt6.QtCore import QFileInfo

from muphyn.packages.core.application.plci_core_data_type import DataType
from muphyn.packages.core.application.plci_core_diagram import Diagram
from muphyn.packages.core.application.plci_core_box import Box

from muphyn.packages.core.application.box_library.importers import AbstractBoxLibraryImporter, BoxLibraryImporter
from muphyn.packages.core.application.box_library.box_library_data import AbstractBoxData

from muphyn.packages.core.base import ManagerMetaClass, LogManager

#-----------------------------------
# Classes
#-----------------------------------
@dataclass
class BoxImportError:
    boxName: str
    error: Exception

    def __str__(self) -> str:
        return f"""
        \t- Box Name: {self.boxName}
        \t- Error: {''.join(traceback.format_exception(self.error))}
        """

@dataclass
class BoxLibraryImportError:
    library: str
    boxImportErrors: List[BoxImportError] = field(default_factory=list)

    def append(self, boxImportError: BoxImportError):
        if boxImportError not in self.boxImportErrors:
            self.boxImportErrors.append(boxImportError)

    def isEmpty(self) -> bool:
        return not bool(self.boxImportErrors)

    def __str__(self) -> str:
        count = len(self.boxImportErrors)
        boxImportErrorsString = '\n'.join([str(boxImportError) for boxImportError in self.boxImportErrors])
        return f"""Library: {self.library}
        {count} box{'es' if count > 1 else ''} has failed:
        {boxImportErrorsString}
        """

class BoxLibraryItem : 
    """Est la classe qui permet de stocker les éléments de bibliothèque dans la classe boxes."""

    # -------------
    # Constructors
    # -------------

    def __init__ (self, path : str) :
        self._path = path
        self._loaded = False
        self._boxes : Dict[str, AbstractBoxData] = {}

    # -------------
    # Properties
    # -------------
    
    @property
    def path (self) -> str : 
        """Permet de récuperer le lien vers le dossier de la bibliothèque de boxes.""" 
        return self._path

    @property
    def loaded (self) -> bool :
        """Permet de récuperer l'état de chargement de la bibliothèque de boxes."""
        return self._loaded

    @property
    def boxes (self) -> Dict[str, AbstractBoxData] :
        """Permet de récuperer le dictionnaire des nom de bibliothèque et leur éléments de création de boxes."""
        return self._boxes

    # -------------
    # Methods
    # -------------

    def load (self, box_importer : AbstractBoxLibraryImporter) -> BoxLibraryImportError :
        """Permet de charger la bibliothèque."""
        # Récuperation des fichiers dans le dossier

        boxLibraryImportErrors = BoxLibraryImportError(self.path)
        for current_file in listdir(self.path):

            if current_file.endswith('.yaml'):
                # Get base file name
                file_name = QFileInfo(current_file).completeBaseName()
                try:
                    # Build absolute yaml file path
                    absolute_yaml_file = self.path + '/' + file_name + '.yaml'
                    
                    imported_box_data = box_importer.import_box(self.path, file_name, absolute_yaml_file, self._boxes)

                    if imported_box_data is None : 
                        continue

                    if imported_box_data['box_data'] is None :
                        continue

                    self._boxes[imported_box_data['library_name']] = imported_box_data['box_data']

                except Exception as e: 
                    # Build error object
                    boxImportError = BoxImportError(file_name, e)
                    boxLibraryImportErrors.append(boxImportError)

        return boxLibraryImportErrors

class BoxesLibrariesManager(metaclass=ManagerMetaClass) :
    """Est la classe qui permet de construire les boxes.""" 

    # -------------
    # Constructors
    # -------------
    def __init__ (self) :
        self._libraries : List[BoxLibraryItem] = []
        self._current_box_index = 0
        self._box_importer = BoxLibraryImporter()
    
    # -------------
    # Properties
    # -------------

    @property
    def current_box_index (self) -> int :
        """Permet de retourner l'index actuelle de la création des boxes."""
        return self._current_box_index

    @property
    def libraries (self) -> List[BoxLibraryItem] :
        """Permet de retourner la liste des libraries."""
        return self._libraries

    @property 
    def box_importer (self) -> AbstractBoxLibraryImporter :
        """Permet de retourner l'importeur utilisé pour importer des boxes."""
        return self._box_importer

    @property
    def boxes (self) -> List[AbstractBoxData] :
        """Permet de retourner l'intégralité des boxes importées."""

        for library in self._libraries :
            for box_name in library.boxes :
                yield library.boxes[box_name]


    # -------------
    # Methods
    # -------------

    def add_library (self, library_folder : str) :
        """Permet d'ajouter une bibliothèque dans le répertoire des bibliothèque."""

        
        # Test if library_folder path format is string 
        if not (isinstance(library_folder, str)) :
            LogManager().error(f"Wrong path variable format {type(library_folder)} instead of str", is_global_message=True)
            return False

        # Test if library folder path exists
        if not path.exists(library_folder):
            LogManager().error(f"Library Path doesn't exists: {library_folder}", is_global_message=True)
            return False

        # Check if library has already been added
        if any(libraryElement.path == library_folder for libraryElement in self._libraries):
            LogManager().error(f"Library Folder already added: {library_folder}", is_global_message=True)
            return False

        # Append Scheduler Library
        self._libraries.append(BoxLibraryItem(library_folder))

        return True

    def load_libraries (self) -> list :
        """Permet de charger toutes les bibliothèques du répertoire."""

        # Init library errors 
        libraryErrors = []

        # Load all libraries
        for libraryElement in self._libraries :
            if not libraryElement.loaded:
                errors = libraryElement.load(self.box_importer)
                if not errors.isEmpty():
                    libraryErrors.append(errors)

        return libraryErrors

    def construct_box (self, box_library : str, box_name : str, **box_params) -> Any:
        """Permet de construire une box suivant son nom et sa librairie."""

        if not (isinstance(box_library, str) and isinstance(box_name, str)) :
            return None

        box_access = self._name_library(box_library, box_name)

        for libraryElement in self._libraries :
            
            if box_access in libraryElement.boxes :
                box = libraryElement.boxes[box_access].construct_box(self._current_box_index, box_params, self)
                
                if isinstance(box, Diagram) :
                    self._current_box_index = box._boxes[box._boxes.__len__() - 1].index + 1

                elif isinstance(box, Box) :
                    self._current_box_index += 1

                return box

    def get_required_params (self, box_library : str, box_name : str) -> Dict[str, DataType] :
        """Permet de retourner les paramètres nécessaires pour instancier une box dans une bibliothèque."""

        if not (isinstance(box_library, str) and isinstance(box_name, str)) :
            return None

        box_access = self._name_library(box_library, box_name)

        for libraryElement in self._libraries :
            
            if box_access in libraryElement.boxes :
                boxElement = libraryElement.boxes[box_access]
                return boxElement.params

        return None
        
    def _name_library (self, box_library : str, box_name : str) -> str :
        """Permet de rassembler le nom et la libraire en un seul string."""
        return box_library + "." + box_name

    def clear (self) -> None :
        """Permet d'éffacer le contenu des boxes chargées."""
        for libraryElement in self._libraries :

            libraryElement.boxes.clear()
            del libraryElement
        
        del self._libraries
        self._libraries : List[BoxLibraryItem] = []

    def get_box_data (self, box_library : str, box_name : str) -> AbstractBoxData : 
        """Permet de récuperer les données de construction d'une box en fonction de sa bibliothèque et de son nom."""

        for box_data in self.boxes :

            if box_data.box_library == box_library and box_data.box_name == box_name :
                return box_data

        return None