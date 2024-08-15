from PySide6.QtWidgets import QLabel, QWidget, QHBoxLayout, QSizePolicy, QVBoxLayout, QPushButton, QLineEdit
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from App.Classes.Utility import ConfigManager

config = ConfigManager()

class HyperlinkLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setParent(parent)
        self.setOpenExternalLinks(True)
        self.setContentsMargins(0, 0, 0, 0)

class FooterWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Create the layout for the footer
        footer_layout = QHBoxLayout()
        footer_layout.setSpacing(4)
        footer_layout.setContentsMargins(0, 32, 0, 32)
        footer_layout.setAlignment(Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignHCenter)

        # Footer message
        FOOTER_TEXT = 'This is an open-source project. Code base can be found on GitHub:'
        footer_msg = QLabel(FOOTER_TEXT, self)
        footer_msg.setStyleSheet("font-size: 12px; color: #6f6f6f; padding: 0;")

        # Hyperlink to GitHub
        GITHUB_URL = 'https://github.com/theaprox/Grubber'
        source_link = HyperlinkLabel(self)
        source_link.setStyleSheet("font-size: 12px; padding: 0; text-decoration: none;")
        linkTemplate = '<a style="text-decoration:none" href="{0}">{1}</a>'
        source_link.setText(linkTemplate.format(GITHUB_URL, 'grubber'))

        # Add the widgets to the footer layout
        footer_layout.addWidget(footer_msg)
        footer_layout.addWidget(source_link)

        # Set the layout for the FooterWidget
        self.setLayout(footer_layout)

class VideoInput(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
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
        
        self.setLayout(actions)