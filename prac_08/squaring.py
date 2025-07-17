from kivy.app import App
from kivy.core.window import Window

__author__ = 'Zheng Zhicong'


class SquareNumberApp(App):
    """ SquareNumberApp is a Kivy App for squaring a number """
    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (500, 100)
        self.title = "Square Number 2"