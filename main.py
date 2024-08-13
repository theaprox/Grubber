import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from App.Pages.HomePage import HomePage
from App.Classes.Utility import LoadCustomFonts, ConfigManager
from App.Classes.Router import Router

class GUI(QWidget):
    def __init__(self):
        super().__init__()
        
        self.config = ConfigManager()
        self.customFonts = LoadCustomFonts()
        
        self.body = QVBoxLayout()
        self.body.setSpacing(0)
        self.body.setContentsMargins(0, 0, 0, 0)
        self.setFixedSize(800, 640)
        self.setFont(QFont(self.config.font, 16))
        self.setWindowIcon(QIcon('./assets/public/grubber-color.png'))
        self.setWindowTitle('Grubber')
        self.setLayout(self.body)
        
        self.router = Router(self.body)
        self.router.load_initial(HomePage(self))

def main():
    app = QApplication(sys.argv)
    
    with open("./App/Styles.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)

    viewport = GUI()
    viewport.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
