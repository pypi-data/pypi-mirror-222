from datetime import date

from muphyn.packages.interface.models.editable_models.abstract_editable_model import AbstractEditableModel
from muphyn.packages.core.application import AbstractBoxData

class BoxDataModel(AbstractEditableModel):

    def __init__(self, boxData: AbstractBoxData):
        super().__init__(boxData.box_name, boxData.path, boxData.creator, date.today(), boxData.version)

        self._boxData: AbstractBoxData = boxData

    @property
    def boxData(self) -> AbstractBoxData:
        return self._boxData
    
    
    @property
    def editor_type (self) -> str :
        """Permet de récuperer le type d'éditeur à utiliser."""
        return 'box-data-editor'
