import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from App.Pages.Base import Base

from App.Classes.Utility import LoadCustomFonts, ConfigManager, Router

def main():
    app = QApplication(sys.argv)

    with open("./App/Styles.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)

    config = ConfigManager()
    customFonts = LoadCustomFonts()
    customFonts.load_fonts()

    main_window = QWidget()
    main_window.setObjectName("viewport")
    main_window.setFont(QFont(config.font, 16, QFont.Normal))
    main_window.setWindowIcon(QIcon('./assets/public/grubber-color.png'))
    main_window.setWindowTitle('Grubber')

    main_layout = QVBoxLayout(main_window)
    main_layout.setContentsMargins(0, 0, 0, 0)
    main_layout.setSpacing(0)
    
    router = Router(main_layout)
    initial_page = Base(router, main_window)
    router.load_initial(initial_page)

    main_window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()


