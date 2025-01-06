from PyQt5.QtGui import QIcon, QPalette, QColor
from PyQt5.QtWidgets import QPushButton, QComboBox, QWidget, QLabel, QLineEdit, QStackedWidget, QApplication, QHBoxLayout, QVBoxLayout, QGridLayout,  QSizePolicy
from PyQt5.QtCore import Qt, pyqtSignal, QSize
import sys
import os

from przejazdy import Stacja

class MenuWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(400, 300)
        self.initBody()
    
    def initBody(self):
        vertLayout = QVBoxLayout()
        vertLayout.setAlignment(Qt.AlignCenter)

        self.label = QLabel('Wyszukaj trase'); self.label.setStyleSheet('font-size: 30px')
        self.label.setAlignment(Qt.AlignCenter)

        self.startPoint = QComboBox(); self.startPoint.addItems(Stacja.__members__.keys())
        self.startPoint.setStyleSheet('font-size: 15px')
        self.startPoint.setMinimumSize(160, 20)
        self.endPoint = QComboBox(); self.endPoint.addItems(Stacja.__members__.keys())  
        self.endPoint.setStyleSheet('font-size: 15px') 
        self.endPoint.setMinimumSize(160, 20) 

        self.b1 = QPushButton('Szukaj'); self.b1.setStyleSheet('font-size: 30px')
        self.b1.clicked.connect(self.started)
        
        vertLayout.addWidget(self.label)
        vertLayout.addWidget(self.startPoint)
        vertLayout.addWidget(self.endPoint)
        vertLayout.addWidget(self.b1)

        self.setLayout(vertLayout)
    def started(self):
        start = self.startPoint.currentText()
        end = self.endPoint.currentText()
        pass



if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.WindowText, QColor(255, 255, 255))
    palette.setColor(QPalette.Base, QColor(25, 25, 25))
    palette.setColor(QPalette.Text, QColor(255, 255, 255))
    palette.setColor(QPalette.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ButtonText, QColor(255, 255, 255))
    app.setPalette(palette)
    
    win = QStackedWidget()
    menWin = MenuWindow()
    win.addWidget(menWin)
    win.setWindowTitle('KOLEO')
    win.show()

    sys.exit(app.exec_())
