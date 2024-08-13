
        
'''class buttonsComponent(QWidget):
    def __init__(self, parent):
        super().__init__()
        
        bg = QWidget(self)
        bg.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        bg.setStyleSheet("background-color: rgba(128, 128, 128, 0.2);")
        
        content = QHBoxLayout(bg)
        content.setContentsMargins(0, 0, 0, 0)
        
        btn1 = QPushButton("Home")
        btn2 = QPushButton("Settings")
        
        btn1.clicked.connect(lambda: parent.loadPage(LandingPage(parent)))
        btn2.clicked.connect(lambda: parent.loadPage(SettingsPage(parent)))
        
        content.addWidget(btn1)
        content.addWidget(btn2)

        # Set the layout for this widget (buttonsComponent)
        layout = QVBoxLayout(self)
        layout.addWidget(bg)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)'''