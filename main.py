from kivy.core.window import Window
from kivy.config import Config

from src.db.DbUtils import init_tables
from src.gui.MainApp import MainApp

Config.set('input', 'mouse', 'mouse,disable_multitouch')

Window.size = (1200, 700)
Window.minimum_heigh, Window.minimum_width = Window.size

# FIXME: убрать ручное выставление координат, сделать автоматически на основе размера экрана
Window.left = 10
Window.top = 10

# задний цвет
# Window.clearcolor = (0.93,0.93,0.93,1)
# Window.fullscreen = True


if __name__ == '__main__':
    init_tables()
    app = MainApp()
    app.run()
