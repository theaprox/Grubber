from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from App.Classes.Components import *

class Settings(QWidget):
    '''Displays the starting view of the application'''
    def __init__(self, router, parent=None):
        super().__init__(parent)
        self.router = router
        
        ### DEFINE LOCAL REUSABLE COMPONENTS
        container = CHLayout(self)
        widget_left = CWidget(direction=Qt.Vertical, width=120, spacing=8)    
        widget_left.layout().setContentsMargins(0, 32, 0, 32)    
        widget_left.layout().setSpacing(8)
        widget_center = CWidget(direction=Qt.Vertical)
        widget_right = CWidget(direction=Qt.Vertical, width=120, spacing=8)    
        widget_right.layout().setContentsMargins(0, 32, 0, 32)    
        widget_right.layout().setSpacing(8)
        spacer = CSpacer()
        
        ### TITLE SECTION
        title = CLabel("Settings", self)
        title.setStyleSheet('font-size: 24px; font-weight: "Medium"; padding: 48px 0;')
        title.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        title.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        widget_center.layout().addWidget(title)

        ### SETTINGS LIST SECTION
        list_settings = CWidget(direction=Qt.Vertical, spacing=8)
        list_settings.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        list_settings.setStyleSheet('border-bottom: 1px solid #FFFFFF;')
        
        ### SETTING 1
        item1 = CWidget(direction=Qt.Horizontal, spacing=8)
        item1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        item1.setObjectName("settings_item")
        ITEM1_LABEL = CLabel('Select font for the application.', self)
        ITEM1_LABEL.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        ITEM1_BUTTON = CButton("Configure", self)
        item1.layout().addWidget(ITEM1_BUTTON)
        item1.layout().addWidget(ITEM1_LABEL)
        
        ### SETTING 2
        item2 = CWidget(direction=Qt.Horizontal, spacing=8)
        item2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        ITEM2_LABEL = CLabel('Some other segging.', self)
        ITEM2_LABEL.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        ITEM2_BUTTON = CButton("Configure", self)
        item2.layout().addWidget(ITEM2_BUTTON)
        item2.layout().addWidget(ITEM2_LABEL)

        list_settings.layout().addWidget(item1)
        list_settings.layout().addWidget(item2)
        widget_center.layout().addWidget(list_settings)
        widget_center.layout().addItem(spacer)
        
        back_btn = CButton(self)
        back_btn_icon = CIcon.SVG('./assets/icons/angle-left.svg', '#9F9F9F', QSize(24, 24))
        back_btn.setIcon(back_btn_icon)
        back_btn.clicked.connect(lambda: self.router.go_back())
        
        widget_left.layout().addWidget(back_btn, alignment=Qt.AlignmentFlag.AlignHCenter)
        widget_left.layout().addItem(spacer)
        
        container.addWidget(widget_left)
        container.addWidget(widget_center)
        container.addWidget(widget_right)

        self.setLayout(container)