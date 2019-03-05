import sys
from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import *
#from PyQt5.QtWebKit import *
from PyQt5.QtWebEngineWidgets import *

class motionWindow(QWidget):
    def Ui_Main(self, MainWindow):
        #super(motionWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("RoverCam")
        uic.loadUi('Motion.ui', self)

app=QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui=motionWindow()
ui.Ui_Main(MainWindow)
MainWindow.show()
sys.exit(app.exec_())