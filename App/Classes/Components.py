from PySide6.QtWidgets import QLabel, QSizePolicy
from PySide6.QtCore import *

class HyperlinkLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setParent(parent)
        self.setOpenExternalLinks(True)
        self.setContentsMargins(0, 0, 0, 0)