from kivy.core.window import Window

from src.gui.MainApp import MainApp

Window.size = (1200, 700)
Window.minimum_heigh, Window.minimum_width = Window.size
#Window.fullscreen = True


if __name__ == '__main__':
    app = MainApp()
    app.run()
