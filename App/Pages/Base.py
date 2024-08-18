from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from App.Classes.Components import FooterWidget, VideoInput, LayoutComponents, CIcon, CButton, CLabel, CHLayout, CVLayout, CSpacer
from App.Pages.Settings import Settings

class Base(QWidget):
    '''Displays the starting view of the application'''
    def __init__(self, router, parent):
        super().__init__(parent)
        self.setObjectName("base")
        self.router = router
        
        layout = LayoutComponents()
        
        container = CHLayout(self)
        left_widget = layout.SideWidget(self, width=120)
        center_widget = layout.CenterWidget(self)
        right_widget = layout.SideWidget(self, width=120)
        
        spacer = CSpacer()
        
        title = CLabel("Grubber", self)
        title.setObjectName("title")
        center_widget.layout.addWidget(title)
        
        hero = CVLayout()
        hero.setContentsMargins(0, 32, 0, 32)
        hero.setSpacing(16)
        center_widget.layout.addLayout(hero)
        
        HEADLINE = 'Take youtube with you!'
        headline = CLabel(HEADLINE, self)
        headline.setObjectName("headline")
        
        PARAGRAPH = 'Grubber makes it easy to download high-quality YouTube videos up to 4K.\nYou can also easily trim the video to download only the parts you want!'
        paragraph = CLabel(PARAGRAPH, self)
        paragraph.setObjectName("paragraph")
        
        hero.addWidget(headline)
        hero.addWidget(paragraph)
        
        actions = VideoInput(self)
        center_widget.layout.addWidget(actions)
        
        center_widget.layout.addItem(spacer)
        
        footer = FooterWidget(self)
        center_widget.layout.addWidget(footer)
        
        settings_btn = CButton(self)
        settings_btn_icon = CIcon.SVG('./assets/icons/gear.svg', '#9F9F9F', QSize(24, 24))
        settings_btn.setIcon(settings_btn_icon)
        settings_btn.clicked.connect(lambda: self.router.go_to_page(Settings))
        
        left_widget.layout.addItem(spacer)
        left_widget.layout.addWidget(settings_btn, alignment=Qt.AlignmentFlag.AlignHCenter)
        
        container.addWidget(left_widget)
        container.addWidget(center_widget)
        container.addWidget(right_widget)

        self.setLayout(container)

