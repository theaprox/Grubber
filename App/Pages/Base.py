from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from App.Classes.Components import FooterWidget, VideoInput, LayoutComponents
from App.Classes.Utility import CustomRenderer, Router
from App.Pages.Settings import Settings

class Base(QWidget):
    '''Displays the starting view of the application'''
    def __init__(self, router, parent):
        super().__init__(parent)
        self.setObjectName("base")
        self.router = router
        
        layout = LayoutComponents()
        
        container = layout.WidgetContainer(self, direction=Qt.Horizontal)
        left_widget = layout.SideWidget(self, width=120)
        center_widget = layout.CenterWidget(self)
        right_widget = layout.SideWidget(self, width=120)
        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        title = QLabel("Grubber", self)
        title.setObjectName("title")
        title.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        title.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        center_widget.layout.addWidget(title)
        
        hero = QVBoxLayout()
        hero.setSpacing(16)
        hero.setContentsMargins(0, 32, 0, 32)
        center_widget.layout.addLayout(hero)
        
        HEADLINE = 'Take youtube with you!'
        headline = QLabel(HEADLINE, self)
        headline.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        headline.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        headline.setStyleSheet('font-size: 32px;')
        
        PARAGRAPH = 'Grubber makes it easy to download high-quality YouTube videos up to 4K.\nYou can also easily trim the video to download only the parts you want!'
        paragraph = QLabel(PARAGRAPH, self)
        paragraph.setWordWrap(True)
        paragraph.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        paragraph.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        paragraph.setStyleSheet('font-size: 16px; color: #9F9F9F;')
        
        hero.addWidget(headline)
        hero.addWidget(paragraph)
        
        actions = VideoInput(self)
        center_widget.layout.addWidget(actions)
        
        center_widget.layout.addItem(spacer)
        
        footer = FooterWidget(self)
        center_widget.layout.addWidget(footer)
        
        settings_btn = QPushButton(self)
        settings_btn_icon = CustomRenderer.ColorSVGIcon('./assets/icons/gear.svg', '#9F9F9F', QSize(24, 24))
        settings_btn.setIcon(settings_btn_icon)
        settings_btn.setIconSize(QSize(24, 24))
        settings_btn.setFlat(True)
        settings_btn.setStyleSheet('padding: 8;')
        settings_btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        settings_btn.clicked.connect(lambda: self.router.go_to_page(Settings))
        
        left_widget.layout.addItem(spacer)
        left_widget.layout.addWidget(settings_btn, alignment=Qt.AlignmentFlag.AlignHCenter)
        
        container.addWidget(left_widget)
        container.addWidget(center_widget)
        container.addWidget(right_widget)

        self.setLayout(container)

