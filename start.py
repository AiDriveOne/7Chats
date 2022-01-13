from gui import Ui_MainWindow
from PyQt5 import QtCore,QtWidgets,QtGui
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import 7Chats

class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()
        
    def run(self):
        7Chats.security()

startfunctions = MainThread()


class Gui_start(QMainWindow):
    def __init__(self):
        super().__init__()
        self.7Chats_ui = Ui_MainWindow()
        self.7Chats_ui.setupUi(self)

    def startfun(self):
        self.7Chats_ui.movies_2 = QtGui.QMovie("src/__1.gif")
        self.7Chats_ui.sm.setMovie(self.7Chats_ui.movies_2)
        self.7Chats_ui.movies_2.start()

        self.7Chats_ui.movies_3 = QtGui.QMovie("src/Jarvis_Gui (1).gif")
        self.7Chats_ui.middle.setMovie(self.7Chats_ui.movies_3)
        self.7Chats_ui.movies_3.start()

        self.7Chats_ui.movies_4 = QtGui.QMovie("src/Earth.gif")
        self.7Chats_ui.earth.setMovie(self.7Chats_ui.movies_4)
        self.7Chats_ui.movies_4.start()

        self.7Chats_ui.movies_5 = QtGui.QMovie("src/dribbble.gif")
        self.7Chats_ui.percent.setMovie(self.7Chats_ui.movies_5)
        self.7Chats_ui.movies_5.start()

        self.7Chats_ui.movies_6 = QtGui.QMovie("src/200.gif")
        self.7Chats_ui.code.setMovie(self.7Chats_ui.movies_6)
        self.7Chats_ui.movies_6.start()

        self.7Chats_ui.movies_7 = QtGui.QMovie("src/0baf79ba59be86610edc1f810a79f2b7.gif")
        self.7Chats_ui.loadpic.setMovie(self.7Chats_ui.movies_7)
        self.7Chats_ui.movies_7.start()

        self.7Chats_ui.movies_8 = QtGui.QMovie("src/initial.gif")
        self.7Chats_ui.initialize.setMovie(self.7Chats_ui.movies_8)
        self.7Chats_ui.movies_8.start()

        startfunctions.start()

    def cls(self):
        self.close()


gui_app = QApplication(sys.argv)
gui_7Chats = Gui_start()
gui_7Chats.startfun()
gui_7Chats.show()
exit(gui_app.exec_())
