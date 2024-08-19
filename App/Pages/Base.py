from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from App.Classes.Components import *
from App.Pages.Settings import Settings

class Base(QWidget):
    '''Displays the starting view of the application'''
    def __init__(self, router, parent):
        super().__init__(parent)
        self.router = router
        
        ### DEFINE LOCAL REUSABLE COMPONENTS
        body = CVLayout(self)
        container = CWidget(direction=Qt.Horizontal)
        spacer = CSpacer()
        
        widget_left = CWidget(direction=Qt.Vertical, width=120)
        widget_left.setContentsMargins(0, 32, 0, 32)
        
        widget_center = CWidget(direction=Qt.Vertical)
        widget_center.setContentsMargins(0, 32, 0, 32)
        widget_center.layout().setSpacing(48)
        widget_center.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        
        widget_right = CWidget(direction=Qt.Vertical, width=120)
        widget_right.setContentsMargins(0, 32, 0, 32)
        
        
        ### BRANDING SECTION (TITLE)
        title = CLabel("Grubber", self)
        title.setMargin(16)
        title.setObjectName("branding")
        widget_center.layout().addWidget(title)
        
        
        ### HERO SECTION
        hero = CWidget(direction=Qt.Vertical)
        hero.setContentsMargins(0, 0, 0, 0)
        hero.layout().setSpacing(8)
        HEADLINE = 'Take youtube with you!'
        headline = CLabel(HEADLINE, self)
        headline.setObjectName("headline")
        PARAGRAPH = 'Grubber makes it easy to download high-quality YouTube videos up to 4K.\nYou can also easily trim the video to download only the parts you want!'
        paragraph = CLabel(PARAGRAPH, self)
        paragraph.setObjectName("paragraph")
        hero.layout().addWidget(headline)
        hero.layout().addWidget(paragraph)
        widget_center.layout().addWidget(hero)
        
        
        ### CTA SECTION (ACTION TO DOWNLOAD)
        cta = CWidget(direction=Qt.Vertical)
        cta.layout().setSpacing(12)
        INPUT = 'Enter video URL...'
        input = CInput(self)
        input.setPlaceholderText(INPUT)
        input.setObjectName("video_url")
        TRIM = 'Download && Trim'
        trim = CButton(TRIM, self)
        trim.setObjectName("trim_btn")
        trim.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        DOWNLOAD = 'Full Video Download'
        down = CButton(DOWNLOAD, self)
        down.setObjectName("down_btn")
        cta.layout().addWidget(input)
        cta.layout().addWidget(trim)
        cta.layout().addWidget(down, alignment=Qt.AlignmentFlag.AlignHCenter)
        widget_center.layout().addWidget(cta)
        
        
        ### FOOTER STUFF      
        footer = CWidget(direction=Qt.Horizontal)
        footer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        GITHUB_URL = 'https://github.com/theaprox/Grubber'
        FOOTER_TEXT = 'This is an open-source project. Code base can be found on GitHub:'
        linkTemplate = '<a style="text-decoration:none" href="{0}">{1}</a>'
        footer_text = f'{FOOTER_TEXT} {linkTemplate.format(GITHUB_URL, "grubber")}'
        footer_msg = CLabel(footer_text, self)
        footer_msg.setObjectName("footer")
        footer_msg.setOpenExternalLinks(True) 
        footer.layout().addWidget(footer_msg)
        
        
        ### LEFT SIDE SECTION
        settings_btn = CButton(self)
        settings_btn_icon = CIcon.SVG('./assets/icons/gear.svg', '#9F9F9F', QSize(24, 24))
        settings_btn.setIcon(settings_btn_icon)
        settings_btn.clicked.connect(lambda: self.router.go_to_page(Settings))
        widget_left.layout().addWidget(settings_btn, alignment=Qt.AlignmentFlag.AlignHCenter)
        
        
        ### ADD ALL COMPONENTS TO BODY
        container.layout().addWidget(widget_left)
        container.layout().addWidget(widget_center)
        container.layout().addWidget(widget_right)
        
        body.addWidget(container)
        body.addItem(spacer)
        body.addWidget(footer)

        self.setLayout(body.layout())