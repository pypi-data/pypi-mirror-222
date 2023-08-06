from muphyn.packages.core.application.box_library.plci_core_boxes_libraries import BoxesLibraries
from muphyn.packages.core.application import SchedulersLibrariesManager
from muphyn.packages.interface.dialogs import DialogsHolder


boxesLibraries = BoxesLibraries()
schedulersLibraries = SchedulersLibrariesManager()
dialogsHolder = DialogsHolder(None)
dialog = dialogsHolder.show_dialog(name = 'library', modal = False, boxes_libraries = boxesLibraries, solvers_libraries = schedulersLibraries)