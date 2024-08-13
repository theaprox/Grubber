from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class LandingPage(QWidget):
    def __init__(self, parent):
        super().__init__()
        
        content = QVBoxLayout()
        content.setContentsMargins(0, 0, 0, 0)
        
        container = QVBoxLayout()
        container.setContentsMargins(32, 32, 32, 32)
        
        header = QLabel("Homepage", self)
        header.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        header.setAlignment(Qt.AlignCenter)
        header.setFont(QFont("Ubuntu", 24))
        
        paragraph = QLabel("This is the landing page for the app.", self)
        paragraph.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        paragraph.setAlignment(Qt.AlignCenter)
        paragraph.setFont(QFont("Ubuntu", 12))
        
        nav = buttonsComponent(parent)
        
        container.addWidget(header)
        container.addWidget(paragraph)
        
        content.addLayout(container)
        content.addWidget(nav)
        
        self.setLayout(content)
        
class SettingsPage(QWidget):
    def __init__(self, parent):
        super().__init__()
        
        content = QVBoxLayout()
        content.setContentsMargins(0, 0, 0, 0)
        
        container = QVBoxLayout()
        container.setContentsMargins(32, 32, 32, 32)
        
        header = QLabel("Settings", self)
        header.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        header.setAlignment(Qt.AlignCenter)
        header.setFont(QFont("Ubuntu", 24))
        
        paragraph = QLabel("Manage settings and preferences.", self)
        paragraph.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        paragraph.setAlignment(Qt.AlignCenter)
        paragraph.setFont(QFont("Ubuntu", 12))
        
        nav = buttonsComponent(parent)
        
        container.addWidget(header)
        container.addWidget(paragraph)
        
        content.addLayout(container)
        content.addWidget(nav)
        
        self.setLayout(content)
        
class buttonsComponent(QWidget):
    def __init__(self, parent):
        super().__init__()
        
        bg = QWidget(self)
        bg.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        bg.setStyleSheet("background-color: rgba(128, 128, 128, 0.2);")
        
        content = QHBoxLayout(bg)
        content.setContentsMargins(0, 0, 0, 0)
        
        btn1 = QPushButton("Home")
        btn2 = QPushButton("Settings")
        
        btn1.clicked.connect(lambda: parent.loadPage(LandingPage(parent)))
        btn2.clicked.connect(lambda: parent.loadPage(SettingsPage(parent)))
        
        content.addWidget(btn1)
        content.addWidget(btn2)

        # Set the layout for this widget (buttonsComponent)
        layout = QVBoxLayout(self)
        layout.addWidget(bg)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)