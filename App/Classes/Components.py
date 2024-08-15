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
        
class LayoutComponents:
    def __init__(self):
        pass
    
    def WidgetContainer(self, parent=None, direction=Qt.Horizontal):
        """Creates a container that can hold the side and center widgets.
        
        Args:
            parent (QWidget): The parent widget for this container.
            direction (Qt.AlignmentFlag): Direction of the layout (Qt.Horizontal or Qt.Vertical).
            
        Returns:
            QLayout: The container layout (either QHBoxLayout or QVBoxLayout).
        """
        if direction == Qt.Horizontal:
            container = QHBoxLayout(parent)
        else:
            container = QVBoxLayout(parent)
        
        container.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignCenter)
        container.setContentsMargins(0, 0, 0, 0)
        container.setSpacing(0)
        return container
    
    def SideWidget(self, parent=None, width=120):
        """Creates a reusable side widget (left or right) with a fixed width."""
        side_widget = QWidget(parent)
        side_widget.setFixedWidth(width)
        side_widget.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)

        side_layout = QVBoxLayout(side_widget)
        side_layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        side_layout.setContentsMargins(0, 32, 0, 32)
        side_layout.setSpacing(0)

        side_widget.setLayout(side_layout)
        side_widget.layout = side_layout  # Store the layout reference
        return side_widget

    def CenterWidget(self, parent=None):
        """Creates a reusable center widget that expands."""
        center_widget = QWidget(parent)
        center_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        center_layout = QVBoxLayout(center_widget)
        center_layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        center_layout.setContentsMargins(0, 0, 0, 0)
        center_layout.setSpacing(0)

        center_widget.setLayout(center_layout)
        center_widget.layout = center_layout  # Store the layout reference
        return center_widget

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
        
class CustomWidgets:
    def __init__(self):
        pass

    def SettingsList(self, parent=None):
        """Creates a reusable settings list widget (list items container)."""
        settings_list = QWidget(parent)
        settings_list_layout = QVBoxLayout(settings_list)
        settings_list_layout.setSpacing(8)
        settings_list_layout.setContentsMargins(0, 0, 0, 0)
        settings_list_layout.setObjectName('settings_list')
        settings_list.setStyleSheet('font-size: 12px;')
        
        settings_list.setLayout(settings_list_layout)
        settings_list.layout = settings_list_layout  # Store the layout reference
        return settings_list

    def SettingsListItem(self, parent=None):
        """Creates a reusable settings list item widget."""
        settings_list_item = QWidget(parent)
        settings_list_item.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        settings_list_item.setStyleSheet('border-bottom: 1px solid rgba(128, 128, 128, 64);')
        
        settings_list_item_layout = QHBoxLayout(settings_list_item)
        settings_list_item_layout.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        settings_list_item_layout.setContentsMargins(0, 4, 0, 4)
        settings_list_item_layout.setSpacing(24)
        
        settings_list_item.setLayout(settings_list_item_layout)
        settings_list_item.layout = settings_list_item_layout  # Store the layout reference
        return settings_list_item
