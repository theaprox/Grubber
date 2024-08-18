from PySide6.QtWidgets import QLabel, QWidget, QSpacerItem, QHBoxLayout, QSizePolicy, QVBoxLayout, QPushButton, QLineEdit
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QFont, QIcon, QPixmap, QPainter, QColor
from PySide6.QtSvg import QSvgRenderer
from App.Classes.Utility import ConfigManager

config = ConfigManager()

'''Create custom globa components defined here and imported from PySide6:
CInput (inherit QLineEdit),
'''

class CInput(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName('CInput')
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.setPlaceholderText("Input Field...")

class CSpacer(QSpacerItem):
    def __init__(self, parent=None):
        super().__init__(0, 0, QSizePolicy.Expanding, QSizePolicy.Expanding)

class CHWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setLayout(CHLayout(self))
        self.setObjectName('CWidget')
        self.setContentsMargins(0, 0, 0, 0)
        
class CVWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setLayout(CVLayout(self))
        self.setObjectName('CWidget')
        self.setContentsMargins(0, 0, 0, 0)
        
class CHLayout(QHBoxLayout):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setContentsMargins(0, 0, 0, 0)
        self.setSpacing(0)

class CVLayout(QVBoxLayout):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setContentsMargins(0, 0, 0, 0)
        self.setSpacing(0)

class CLabel(QLabel):
    '''Custom global QLabel variant.'''
    def __init__(self, text: str = "", parent=None):
        super().__init__(text, parent)
        self.setObjectName('CLabel')
        self.setFont(QFont(config.font, 16, QFont.Normal))
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setWordWrap(True)
        self.setText(text)

class CButton(QPushButton):
    '''Custom global QPushButton variant.'''
    def __init__(self, text: str = "", parent=None):
        super().__init__(text, parent)
        self.setObjectName('CButton')
        self.setCursor(Qt.PointingHandCursor)
        self.setFont(QFont(config.font, 16, QFont.Medium))
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.setIconSize(QSize(24, 24))
        self.setFlat(True)

class CIcon:
    '''Custom QIcon variant for inserting colored SVG icons.'''
    def SVG(svg_path, color, size):
        """Creates a colored icon from an SVG file."""
        svg_renderer = QSvgRenderer(svg_path)
        pixmap = QPixmap(size)
        pixmap.fill(QColor("transparent"))

        painter = QPainter(pixmap)
        svg_renderer.render(painter)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter.fillRect(pixmap.rect(), color)
        painter.end()

        return QIcon(pixmap)

class HyperlinkLabel(QLabel):
    '''Custom QLabel variant used as a clickable hyperlinks.'''
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setParent(parent)
        self.setOpenExternalLinks(True)
        self.setContentsMargins(0, 0, 0, 0)
        

class LayoutComponents:
    def __init__(self):
        pass
    
    def WidgetContainer(self, parent=None, direction=Qt.Horizontal):
        """Creates a directional QWidget container."""
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
        side_widget.layout = side_layout
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
        center_widget.layout = center_layout
        return center_widget

class FooterWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("footer")
        
        # Create the layout for the footer
        footer_layout = QHBoxLayout()
        footer_layout.setSpacing(4)
        footer_layout.setContentsMargins(0, 32, 0, 32)
        footer_layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)

        FOOTER_TEXT = 'This is an open-source project. Code base can be found on GitHub:'
        footer_msg = QLabel(FOOTER_TEXT, self)

        GITHUB_URL = 'https://github.com/theaprox/Grubber'
        source_link = HyperlinkLabel(self)
        linkTemplate = '<a style="text-decoration:none" href="{0}">{1}</a>'
        source_link.setText(linkTemplate.format(GITHUB_URL, 'grubber'))

        footer_layout.addWidget(footer_msg)
        footer_layout.addWidget(source_link)

        self.setLayout(footer_layout)

class VideoInput(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        actions = CVLayout()
        actions.setSpacing(16)
        actions.setContentsMargins(0, 32, 0, 32)
        input = CInput(self)
        input.setObjectName("video_url")
        input.setPlaceholderText("Video URL...")
        actions.addWidget(input)

        buttons = CVLayout()
        buttons.setSpacing(0)
        buttons.setContentsMargins(0, 0, 0, 0)
        buttons.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        
        TRIM = 'Download && Trim'
        trim_btn = CButton(TRIM, self)
        trim_btn.setObjectName("trim_btn")
        trim_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        
        DOWNLOAD = 'Full Video Download'
        down_btn = CButton(DOWNLOAD, self)
        down_btn.setObjectName("down_btn")
        
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
        
        settings_list.setLayout(settings_list_layout)
        settings_list.layout = settings_list_layout
        return settings_list

    def SettingsListItem(self, parent=None):
        """Creates a reusable settings list item widget."""
        settings_list_item = QWidget(parent)
        settings_list_item.setObjectName('settings_list_item')
        settings_list_item.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        settings_list_item.setStyleSheet('''#settings_list_item { border-bottom: 1px solid rgba(128, 128, 128, 64);}''')
        
        settings_list_item_layout = QHBoxLayout(settings_list_item)
        settings_list_item_layout.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        settings_list_item_layout.setContentsMargins(0, 4, 0, 4)
        settings_list_item_layout.setSpacing(24)
        
        settings_list_item.setLayout(settings_list_item_layout)
        settings_list_item.layout = settings_list_item_layout
        return settings_list_item
