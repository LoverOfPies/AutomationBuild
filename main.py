from kivy.core.window import Window

from gui.MainApp import MainApp

Window.minimum_height = 500
Window.minimum_width = 500


if __name__ == '__main__':
    app = MainApp()
    app.run()
