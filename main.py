from kivy.core.window import Window

from src.gui.MainApp import MainApp

Window.minimum_height = 500
Window.minimum_width = 1200
#Window.fullscreen = True


if __name__ == '__main__':
    app = MainApp()
    app.run()
