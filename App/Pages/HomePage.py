from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from App.Classes.Components import FooterWidget
from App.Classes.Utility import ConfigManager

class HomePage(QWidget):
    '''Displays the starting view of the application'''
    def __init__(self, parent):
        super().__init__(parent)
        self.setObjectName("HomePage")
        
        config = ConfigManager()

        LEFT_W = 120
        RIGHT_W = 120
        container = QHBoxLayout()
        container.setAlignment(Qt.AlignTop | Qt.AlignCenter)
        container.setContentsMargins(0, 0, 0, 0)
        container.setSpacing(0)

        left_widget = QWidget()
        left_widget.setFixedWidth(LEFT_W)
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
        title.setObjectName("title")
        title.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        title.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        
        hero = QVBoxLayout()
        hero.setSpacing(16)
        hero.setContentsMargins(0, 32, 0, 32)
        
        HEADLINE = 'Take youtube with you!'
        headline = QLabel(HEADLINE, self)
        headline.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        headline.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        headline.setStyleSheet('font-size: 32px;')
        
        PARAGRAPH = 'Grubber makes it easy to download high-quality YouTube videos up to 4K.\nYou can also easily trim the video to download only the parts you want!'
        paragraph = QLabel(PARAGRAPH, self)
        paragraph.setWordWrap(True)
        paragraph.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        paragraph.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        paragraph.setStyleSheet('font-size: 16px; color: #9F9F9F;')
        
        hero.addWidget(headline)
        hero.addWidget(paragraph)
        
        actions = QVBoxLayout()
        actions.setSpacing(16)
        actions.setContentsMargins(0, 32, 0, 32)
        input = QLineEdit(self)
        input.setObjectName("video_url")
        input.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        input.setAlignment(Qt.AlignmentFlag.AlignLeft)
        input.setPlaceholderText("Video URL...")
        input.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        actions.addWidget(input)

        buttons = QVBoxLayout()
        buttons.setSpacing(16)
        buttons.setContentsMargins(0, 0, 0, 0)
        buttons.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        
        TRIM = 'Download && Trim'
        trim_btn = QPushButton(TRIM, self)
        trim_btn.setObjectName("trim_btn")
        trim_btn.setFont(QFont(config.font, 16, QFont.Medium))
        trim_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        trim_btn.setCursor(Qt.PointingHandCursor)
        
        DOWNLOAD = 'Full Video Download'
        down_btn = QPushButton(DOWNLOAD, self)
        down_btn.setObjectName("down_btn")
        down_btn.setFont(QFont(config.font, 16, QFont.Medium))
        down_btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        down_btn.setCursor(Qt.PointingHandCursor)
        
        buttons.addWidget(trim_btn)
        buttons.addWidget(down_btn, alignment=Qt.AlignCenter)
        actions.addLayout(buttons)
        
        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        footer = FooterWidget(self)
        
        center_layout.addWidget(title)
        center_layout.addLayout(hero)
        center_layout.addLayout(actions)
        center_layout.addItem(spacer)
        center_layout.addWidget(footer)

        right_widget = QWidget()
        right_widget.setFixedWidth(RIGHT_W)
        right_widget.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        right_layout = QVBoxLayout(right_widget)
        right_layout.setContentsMargins(0, 0, 0, 0)
        right_layout.setSpacing(0)
        right_layout.setAlignment(Qt.AlignTop | Qt.AlignCenter)

        container.addWidget(left_widget)
        container.addWidget(center_widget)
        container.addWidget(right_widget)

        self.setLayout(container)

