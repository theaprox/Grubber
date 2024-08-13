from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QSizePolicy
from PySide6.QtCore import Qt

class HomePage(QWidget):
    '''Displays the starting view of the application'''
    def __init__(self, parent):
        super().__init__(parent)
        self.setObjectName("HomePage")

        container = QHBoxLayout()
        container.setAlignment(Qt.AlignTop | Qt.AlignCenter)
        container.setContentsMargins(0, 0, 0, 0)
        container.setSpacing(0)

        left_widget = QWidget()
        left_widget.setFixedWidth(80)
        left_widget.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        left_layout = QVBoxLayout(left_widget)
        left_layout.setAlignment(Qt.AlignTop | Qt.AlignCenter)
        left_layout.setContentsMargins(0, 0, 0, 0)
        left_layout.setSpacing(0)
        
        
        center_widget = QWidget()
        center_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        center_layout = QVBoxLayout(center_widget)
        center_layout.setAlignment(Qt.AlignTop | Qt.AlignCenter)
        center_layout.setContentsMargins(0, 0, 0, 0)
        center_layout.setSpacing(0)
        title = QLabel("Grubber", self)
        title.setStyleSheet("font: 64px 'Passero One'; color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0,stop: 0 #FFA400, stop: 1 #DB00FF); padding: 48px 0;")
        center_layout.addWidget(title)

        right_widget = QWidget()
        right_widget.setFixedWidth(80)
        right_widget.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        right_layout = QVBoxLayout(right_widget)
        right_layout.setContentsMargins(0, 0, 0, 0)
        right_layout.setSpacing(0)
        right_layout.setAlignment(Qt.AlignTop | Qt.AlignCenter)


        container.addWidget(left_widget)
        container.addWidget(center_widget)
        container.addWidget(right_widget)

        self.setLayout(container)

