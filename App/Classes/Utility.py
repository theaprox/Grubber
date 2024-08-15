import os
import sys
import platform
from pathlib import Path
from configparser import ConfigParser
from PySide6.QtGui import QFontDatabase, QIcon, QPixmap, QPainter, QColor
from PySide6.QtSvg import QSvgRenderer

# Import Windows registry functions only if on Windows
if platform.system() == 'Windows':
    from winreg import OpenKey, QueryValueEx, HKEY_CURRENT_USER

class LoadCustomFonts:
    def load_fonts(self):
        FONTS_DIR = './Assets/fonts/'
        FONTS_LIST = [ 'PasseroOne-Regular.ttf' ]
        for font in FONTS_LIST:
            QFontDatabase.addApplicationFont(f"{FONTS_DIR}/{font}")

class CustomRenderer:
    def ColorSVGIcon(svg_path, color, size):
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

class ConfigManager:
    def __init__(self, filename='Grubber.ini'):
        self.filename = filename
        self.config = ConfigParser()

        # Centralized default configuration
        self.default_config = {
            'font': 'Ubuntu',
            'dldir': self.get_default_download_folder(),
            'first_download': True
        }

        if not os.path.exists(self.filename):
            self.build_default_config()
        self.load_config()

    def build_default_config(self):
        """Creates default config file based on centralized defaults."""
        self.config['DEFAULT'] = self.default_config
        with open(self.filename, 'w') as configfile:
            self.config.write(configfile)

    def load_config(self):
        """Reads config file & stores values."""
        self.config.read(self.filename)
        for key in self.default_config:
            setattr(self, key, self.config.get('DEFAULT', key, fallback=self.default_config[key]))

    def save_config(self):
        """Saves the current configuration to the file."""
        for key in self.default_config:
            self.config['DEFAULT'][key] = getattr(self, key, str(self.default_config[key]))
        
        with open(self.filename, 'w') as configfile:
            self.config.write(configfile)

    def update_config(self, key, value):
        """Updates a specific config value and saves the config file."""
        self.config['DEFAULT'][key] = value
        self.save_config()

    def get_default_download_folder(self):
        """Attempt to get the default download folder based on the OS."""
        try:
            if platform.system() == 'Windows':
                with OpenKey(HKEY_CURRENT_USER, 'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Shell Folders') as key:
                    download_folder = QueryValueEx(key, '{374DE290-123F-4565-9164-39C4925E467B}')[0]
                    return os.path.join(download_folder, 'Grubber')

            elif platform.system() == 'Darwin':  # macOS
                download_folder = str(Path.home() / "Downloads")
                return os.path.join(download_folder, 'Grubber')

            elif platform.system() == 'Linux':
                download_folder = str(Path.home() / "Downloads")
                return os.path.join(download_folder, 'Grubber')

        except Exception as e:
            print(f"Error finding default download folder: {e}")
            return None
 
class Router:
    def __init__(self, layout):
        self.layout = layout
        self.current_page = None
        self.previous_page = None

    def clean(self):
        """Clear the current layout."""
        for i in reversed(range(self.layout.count())):
            widget = self.layout.itemAt(i).widget()
            if widget is not None:
                widget.setParent(None)

    def load(self, page_widget):
        """Load the provided page widget."""
        if self.current_page is not None:
            self.previous_page = self.current_page

        self.clean()
        self.current_page = page_widget
        self.layout.addWidget(page_widget)

    def load_initial(self, page_widget):
        """Load the initial page without setting a previous page."""
        self.clean()
        self.current_page = page_widget
        self.previous_page = None
        self.layout.addWidget(page_widget)

    def go_back(self):
        """Go back to the previous page if available."""
        if self.previous_page is not None:
            self.load(self.previous_page)

    def go_to_page(self, page_class, *args, **kwargs):
        """
        Load a new page dynamically.
        :param page_class: The page class to load.
        :param args: Positional arguments to pass to the page class constructor.
        :param kwargs: Keyword arguments to pass to the page class constructor.
        """
        page_widget = page_class(self, *args, **kwargs)
        self.load(page_widget)

