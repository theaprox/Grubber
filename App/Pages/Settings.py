from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from App.Classes.Components import FooterWidget, LayoutComponents, CustomWidgets, CIcon, CLabel, CButton, CSpacer

class Settings(QWidget):
    '''Displays the starting view of the application'''
    def __init__(self, router, parent=None):
        super().__init__(parent)
        self.setObjectName("settings")
        self.router = router
        
        layout = LayoutComponents()
        container = layout.WidgetContainer(self, direction=Qt.Horizontal)
        custom_widgets = CustomWidgets()

        left_widget = layout.SideWidget(self, width=120)
        center_widget = layout.CenterWidget(self)
        right_widget = layout.SideWidget(self, width=120)
        spacer = CSpacer()
        
        page_title = CLabel("Settings", self)
        page_title.setStyleSheet('font-size: 24px; font-weight: "Medium"; padding: 48px 0;')
        page_title.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        page_title.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        center_widget.layout.addWidget(page_title)
        
        settings_list = custom_widgets.SettingsList(self)

        # Create and add items to the settings list
        item1 = custom_widgets.SettingsListItem(self)
        ITEM1_LABEL = CLabel('Select font for the application.', self)
        ITEM1_LABEL.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        ITEM1_BUTTON = CButton("Configure", self)
        item1.layout.addWidget(ITEM1_BUTTON)
        item1.layout.addWidget(ITEM1_LABEL)
        
        item2 = custom_widgets.SettingsListItem(self)
        ITEM2_LABEL = CLabel('Some other segging.', self)
        ITEM2_LABEL.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        ITEM2_BUTTON = CButton("Configure", self)
        item2.layout.addWidget(ITEM2_BUTTON)
        item2.layout.addWidget(ITEM2_LABEL)

        # Add items to the settings list
        settings_list.layout.addWidget(item1)
        settings_list.layout.addWidget(item2)
        center_widget.layout.addWidget(settings_list)
        
        center_widget.layout.addItem(spacer)
        
        footer = FooterWidget(self)
        center_widget.layout.addWidget(footer)
        
        back_btn = CButton(self)
        back_btn_icon = CIcon.SVG('./assets/icons/angle-left.svg', '#9F9F9F', QSize(24, 24))
        back_btn.setIcon(back_btn_icon)
        back_btn.clicked.connect(lambda: self.router.go_back())
        
        left_widget.layout.addWidget(back_btn, alignment=Qt.AlignmentFlag.AlignHCenter)
        left_widget.layout.addItem(spacer)
        
        container.addWidget(left_widget)
        container.addWidget(center_widget)
        container.addWidget(right_widget)

        self.setLayout(container)

