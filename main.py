import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from App.Pages.HomePage import HomePage
from App.Classes.Utility import LoadCustomFonts, ConfigManager
from App.Classes.Router import Router

def main():
    app = QApplication(sys.argv)

    with open("./App/Styles.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)

    config = ConfigManager()
    customFonts = LoadCustomFonts()
    customFonts.load_fonts()

    viewport = QWidget()
    viewport.setObjectName("viewport")
    viewport.setFont(QFont(config.font, 16, QFont.Normal))
    viewport.setWindowIcon(QIcon('./assets/public/grubber-color.png'))
    viewport.setWindowTitle('Grubber')

    body = QVBoxLayout(viewport)
    body.setContentsMargins(0, 0, 0, 0)
    body.setSpacing(0)
    router = Router(body)
    router.load_initial(HomePage(viewport))

    viewport.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()