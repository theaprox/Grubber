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
        left_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
        left_layout.setContentsMargins(0, 0, 0, 0)
        left_layout.setSpacing(0)
        
        
        center_widget = QWidget()
        center_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        center_layout = QVBoxLayout(center_widget)
        center_layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        center_layout.setContentsMargins(0, 0, 0, 0)
        center_layout.setSpacing(0)
        
        title = QLabel("Grubber", self)
        title.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        title.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        title.setStyleSheet("font: 64px 'Passero One'; color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0,stop: 0 #FFA400, stop: 1 #DB00FF); padding: 48px 0;")
        
        hero = QVBoxLayout()
        hero.setSpacing(16)
        hero.setContentsMargins(0, 32, 0, 32)
        HEADLINE = 'Take youtube with you!'
        headline = QLabel(HEADLINE, self)
        headline.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        headline.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        headline.setStyleSheet("font: 32px 'Ubuntu Medium'; color: #FEFEFE;")
        
        PARAGRAPH = 'Grubber makes it easy to download high-quality YouTube videos up to 4K.\nYou can also easily trim the video to download only the parts you want!'
        paragraph = QLabel(PARAGRAPH, self)
        paragraph.setWordWrap(True)
        paragraph.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        paragraph.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        paragraph.setStyleSheet("font: 16px 'Ubuntu'; color: #9F9F9F;")
        
        hero.addWidget(headline)
        hero.addWidget(paragraph)
        
        center_layout.addWidget(title)
        center_layout.addLayout(hero)

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

