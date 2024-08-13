import os
from winreg import *
from configparser import ConfigParser
from PySide6.QtGui import QFontDatabase

class LoadCustomFonts():
    def load_fonts(self):
        FONTS_DIR = './Assets/fonts/'
        FONTS_LIST = [ 'PasseroOne-Regular.ttf' ]
        for font in FONTS_LIST:
            QFontDatabase.addApplicationFont(f"{FONTS_DIR}/{font}")

class ConfigManager:
    def __init__(self, filename='Grubber.ini'):
        self.filename = filename
        self.config = ConfigParser()
        
        if not os.path.exists(self.filename):
            self.build_default_config()
        self.load_config()

    def build_default_config(self):
        """Creates default config file."""
        default_font = 'Ubuntu'
        
        # Fetch default download directory from Windows registry
        with OpenKey(HKEY_CURRENT_USER, 'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Shell Folders') as key:
            default_dldir = QueryValueEx(key, '{374DE290-123F-4565-9164-39C4925E467B}')[0] + '\\Grubber'
        
        self.config['DEFAULT'] = {
            'font': default_font,
            'dldir': default_dldir
        }
        
        with open(self.filename, 'w') as configfile:
            self.config.write(configfile)

    def load_config(self):
        """Reads config file & stores values."""
        self.config.read(self.filename)
        self.font = self.config.get('DEFAULT', 'font')
        self.dldir = self.config.get('DEFAULT', 'dldir')

    def save_config(self):
        """Saves the current configuration to the file."""
        self.config['DEFAULT']['font'] = self.font
        self.config['DEFAULT']['dldir'] = self.dldir
        
        with open(self.filename, 'w') as configfile:
            self.config.write(configfile)

    def update_config(self, key, value):
        """Updates a specific config value and saves the config file."""
        self.config['DEFAULT'][key] = value
        self.save_config()
        
