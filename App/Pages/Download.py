from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from App.Classes.Components import *

class Download(QWidget):
    '''Displays the starting view of the application'''
    def __init__(self, router, parent, contents=None):
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
        
        
        ### TITLE SECTION
        title = CLabel("Download Video", self)
        title.setStyleSheet('font-size: 24px; font-weight: "Medium"; padding: 48px 0;')
        title.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        title.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        widget_center.layout().addWidget(title)
        
        
        ### VIDEO VARS SECTION        
        video_vars = CWidget(direction=Qt.Vertical, spacing=8)
        if contents is not None:
            for key in contents:
                text = f'{contents.key}: {contents.value}'
                print_label = CLabel(text, self)
                video_vars.addWidget(print_label)
        else:
            text = 'No video selected.'
            print_label = CLabel(text, self)
            video_vars.addWidget(print_label)
                
        widget_center.layout().addWidget(video_vars)
        
        
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
        back_btn = CButton(self)
        back_btn_icon = CIcon.SVG('./assets/icons/angle-left.svg', '#9F9F9F', QSize(24, 24))
        back_btn.setIcon(back_btn_icon)
        back_btn.clicked.connect(lambda: self.router.go_back())
        
        widget_left.layout().addWidget(back_btn)
        
        
        ### ADD ALL COMPONENTS TO BODY
        container.layout().addWidget(widget_left)
        container.layout().addWidget(widget_center)
        container.layout().addWidget(widget_right)
        
        body.addWidget(container)
        body.addItem(spacer)
        body.addWidget(footer)

        self.setLayout(body.layout())