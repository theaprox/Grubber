from PySide6.QtWidgets import QLabel, QWidget, QHBoxLayout
from PySide6.QtCore import Qt

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
