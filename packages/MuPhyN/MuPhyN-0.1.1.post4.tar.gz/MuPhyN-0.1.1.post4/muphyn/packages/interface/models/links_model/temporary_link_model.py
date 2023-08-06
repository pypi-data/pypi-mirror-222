#-----------------------------------
# Imports
#-----------------------------------

# General Imports

# Project Imports
from PyQt6.QtCore import QPointF
from PyQt6.QtGui import QMouseEvent
from PyQt6.QtWidgets import QGraphicsSceneMouseEvent

# Project Imports
from muphyn.packages.interface.models.links_model.abstract_link_model import AbstractLinkModel
from muphyn.packages.interface.models.links_model.link_type import LinkType
from muphyn.packages.interface.models.signals_model.abstract_connection_model import AbstractConnectionModel
# from muphyn.packages.interface.models.editable_models.simulation_model import SimulationModel

#-----------------------------------
# Class
#-----------------------------------
class TemporaryLinkModel(AbstractLinkModel):
    def __init__(self, signal_creator: AbstractConnectionModel):

        # Get output position
        outputPosition = signal_creator.absolute_connector_center

        super().__init__(outputPosition, outputPosition, LinkType.SQUARE)

    def mouseMoveEvent(self, event: QGraphicsSceneMouseEvent) -> None:
        self.endPoint = event.scenePos()
        return super().mouseMoveEvent(event)
        
