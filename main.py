from kivy.core.window import Window

from src.db.DbUtils import init_tables
from src.gui.MainApp import MainApp

Window.size = (1200, 700)
Window.minimum_heigh, Window.minimum_width = Window.size
Window.left = 10
Window.top = 10
# Window.fullscreen = True


if __name__ == '__main__':
    init_tables()
    app = MainApp()
    app.run()
