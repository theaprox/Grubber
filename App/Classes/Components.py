from PySide6.QtWidgets import QLabel, QWidget, QSpacerItem, QHBoxLayout, QSizePolicy, QVBoxLayout, QPushButton, QLineEdit
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QFont, QIcon, QPixmap, QPainter, QColor, QMovie
from PySide6.QtSvg import QSvgRenderer
from App.Classes.Utility import ConfigManager

config = ConfigManager()

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
        
class CHLayout(QHBoxLayout):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName('CHLayout')
        self.setContentsMargins(0, 0, 0, 0)
        self.setSpacing(0)

class CVLayout(QVBoxLayout):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName('CVLayout')
        self.setContentsMargins(0, 0, 0, 0)
        self.setSpacing(0)

class CWidget(QWidget):
    def __init__(self, direction=Qt.Vertical, width: int = None, height: int = None, spacing: int = 0, parent=None, hpolicy=QSizePolicy.Expanding, vpolicy=QSizePolicy.Expanding):
        super().__init__(parent)
        self.setObjectName('CWidget')
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        if direction == Qt.Vertical:
            layout = QVBoxLayout(self)
        else:
            layout = QHBoxLayout(self)

        layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(spacing)

        if width is not None:
            self.setFixedWidth(width)
            self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)

        if height is not None:
            self.setFixedHeight(height)
            self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        if width and height is not None:
            self.setFixedWidth(width)
            self.setFixedHeight(height)
            self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        self.setLayout(layout)

class CLabel(QLabel):
    '''Custom global QLabel variant.'''
    def __init__(self, text: str = "", parent=None, size: int = 12):
        super().__init__(text, parent)
        self.setObjectName('CLabel')
        self.setFont(QFont(config.font, size, QFont.Normal))
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setText(text)

class CButton(QPushButton):
    '''Custom global QPushButton variant.'''
    def __init__(self, text: str = "", parent=None):
        super().__init__(text, parent)
        self.setObjectName('CButton')
        self.setCursor(Qt.PointingHandCursor)
        self.setFont(QFont(config.font, 16, QFont.Medium))
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.setIconSize(QSize(16, 16))
        self.setFlat(True)
        
        # set loading animation vars
        self.loading_movie = QMovie('Assets/Animated/small_wave.gif')
        self.loading_movie.setScaledSize(QSize(24, 24))
        
    def save_state(self):
        self.original_text = self.text()
        self.original_icon = self.icon()
        
    def restore_state(self):
        if self.original_text != "":
            self.setText(self.original_text)
        if self.original_icon is not None:
            self.setIcon(self.original_icon)
        self.setEnabled(True)
        
    def clear_state(self):
        self.setText("")
        self.setIcon(QIcon())
        
    def set_loading(self):
        self.save_state()
        self.clear_state()
        self.setEnabled(False)
        self.loading_movie.start()
        self.setIcon(QIcon(self.loading_movie.currentPixmap()))
        self.loading_movie.frameChanged.connect(self.update_loading_icon)

    def unset_loading(self):
        self.loading_movie.stop()
        self.loading_movie.frameChanged.disconnect(self.update_loading_icon)
        self.restore_state()
        
    def update_loading_icon(self):
        self.setIcon(QIcon(self.loading_movie.currentPixmap()))

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
