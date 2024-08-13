import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from pages import *

class AppGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.startUI()

    def startUI(self):
        self.setWindowTitle("Hewow")
        self.body = QVBoxLayout()
        self.body.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.body)

        # Load the default page
        self.loadPage(LandingPage(self)) 

    def cleanPage(self):
        '''Clear the current layout'''
        for i in reversed(range(self.body.count())):
            widget = self.body.itemAt(i).widget()
            if widget is not None:
                widget.setParent(None)

    def loadPage(self, page_widget):
        '''Load the provided page widget'''
        self.cleanPage()  # Clear existing page
        self.body.addWidget(page_widget)  # Add the new page

def main():
    app = QApplication(sys.argv)

    viewport = AppGUI()
    viewport.setContentsMargins(0, 0, 0, 0)
    viewport.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
