from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from App.Classes.Components import *
from App.Pages.Settings import Settings
from App.Pages.Download import Download
from functools import partial

class Base(QWidget):
    '''Displays the starting view of the application'''
    
    '''
    You will create several classes/functions like "download_video", "validate_url", "extract_video_code", and others if needed...
    
    0) when user clicks "trim" or "down" buttons execute a download_video function.
    This function doesnt actually download a video but instead performas an extensive check to validate provided information.
    If all validation checks pass, it will then redirtect user to the actual Download page (Download.py) where the user will opt to download video/audio in variaus formats and qualities.
    
    1) when the function is called - disable the button that called the function for the duration of the check,
    and replace it's text with a rotating loading throbber while validation (next steps) is taking place.
    THEN
    2) validate that the user input from "input.CInput()" is a valid YouTube video, or youtube short url.
    3) if the video input validation fails:
        * if the input url is of a playlist - set "feedback_msg" variable to "Playlists are not yet supported."
        and execute a page reload using the "router" function (e.g.: "lambda: self.router.go_to_page(Base(feedback=feedback_msg))")
        * if validation fails set "feedback_msg" variable to "Invalid URL."
        and execute a page reload using the "router" function (e.g.: "lambda: self.router.go_to_page(Base(feedback=feedback_msg))")
        
    4) if validation passes:
        * create an object "video_contents" with the following keys and values:
            - "content type": "video" or "short"
            - "url": user input url
            - "code": video code extracted from the user input url (using yt-dlp, or pytube, or any other method/library)
    5) using the "router" function open the imported "Download" page (from App.Pages.Download) (e.g.: "lambda: self.router.go_to_page(Download(contents=video_contents))") 
    '''
    
    
    def download_ckicled(self, button):
        button.set_loading()
        QTimer.singleShot(1000, button.unset_loading)
    
    def __init__(self, router, parent, feedback: str = ''):
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
        INPUT = 'Video URL...'
        input = CInput(self)
        input.setPlaceholderText(INPUT)
        input.setObjectName("video_url")
        
        TRIM = 'Download && Trim'
        trim = CButton(TRIM, self)
        trim.setObjectName("trim_btn")
        trim.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        trim.clicked.connect(partial(self.download_ckicled, trim))
        
        DOWNLOAD = 'Full Video Download'
        down = CButton(DOWNLOAD, self)
        down.setObjectName("down_btn")
        
        if feedback != '':
            input_error_message = CLabel(feedback, self, size=10)
            input_error_message.setAlignment(Qt.AlignmentFlag.AlignLeft)
            input_error_message.setStyleSheet('color: red')
            cta.layout().addWidget(input_error_message)
            
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