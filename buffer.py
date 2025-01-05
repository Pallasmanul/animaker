from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QPushButton
from core.buffer import Buffer
from core.utils import *

class AppBuffer(Buffer):
    def __init__(self, buffer_id, url, arguments):
        Buffer.__init__(self, buffer_id, url, arguments, True)

        self.add_widget(QPushButton("Hello, EAF hacker, it's working!!!"))
        self.buffer_widget.setStyleSheet("background: {}; color: {}; font-size: 100px;".format(self.theme_background_color, self.theme_foreground_color))

    @interactive
    def update_theme(self):
        super().update_theme()

        self.background_color = QColor(self.theme_background_color)
        self.buffer_widget.setStyleSheet("background-color: {};".format(self.theme_background_color))
        self.buffer_widget.setStyleSheet("background: {}; color: {}; font-size: 100px;".format(self.theme_background_color, self.theme_foreground_color))

        self.update()
