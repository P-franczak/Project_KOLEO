from PyQt5.QtGui import QPalette, QColor, QPixmap
from PyQt5.QtWidgets import QPushButton, QComboBox, QWidget, QLabel, QStackedWidget, QApplication, QHBoxLayout, QVBoxLayout, QListWidget
from PyQt5.QtCore import Qt, QSize
from polaczone import tabu_search, lista_sasiedztwa_enum
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
        menuLayout = QHBoxLayout()
        resultLayout = QHBoxLayout()
        vertLayout.setAlignment(Qt.AlignCenter)

        self.label = QLabel('Wyszukaj trase'); self.label.setStyleSheet('font-size: 30px')
        self.label.setAlignment(Qt.AlignCenter)

        self.startPoint = QComboBox(); self.startPoint.addItems(Stacja.__members__.keys())
        self.startPoint.setStyleSheet('font-size: 18px')
        self.startPoint.setMinimumSize(160, 20)
        self.endPoint = QComboBox(); self.endPoint.addItems(Stacja.__members__.keys())  
        self.endPoint.setStyleSheet('font-size: 18px') 
        self.endPoint.setMinimumSize(160, 20) 

        self.b1 = QPushButton('Szukaj'); self.b1.setStyleSheet('font-size: 30px')
        self.b1.clicked.connect(self.started)
        
        menuLayout.addWidget(self.label)
        menuLayout.addWidget(self.startPoint)
        menuLayout.addWidget(self.endPoint)
        menuLayout.addWidget(self.b1)


        self.resPath = QListWidget(); self.resPath.setMinimumSize(500, 200)
        self.iterImage = QLabel()
        resultImage = QPixmap('tlo.png')
        self.iterImage.setPixmap(resultImage)
        self.iterImage.setScaledContents(True)
        resultLayout.addWidget(self.resPath, stretch = 1)
        resultLayout.addWidget(self.iterImage, stretch = 1)
        
        vertLayout.addLayout(menuLayout)
        vertLayout.addLayout(resultLayout)

        self.setLayout(vertLayout)
    def started(self):
        start = self.startPoint.currentText()
        end = self.endPoint.currentText()
        FinalPath = tabu_search(start, end, lista_sasiedztwa_enum, max_iter=50, dlugosc_tabu=10)
        resultImage = QPixmap('obrazek.png')
        self.iterImage.setPixmap(resultImage)
        


        '''
        game = ResultWindow(FinalPath, IterImage)
        win.addWidget(game)
        win.setCurrentIndex(win.currentIndex()+1)


class ResultWindow(QWidget):
    def __init__(self, FinalPath, IterImage):
        super().__init__()
        self.FinalPath
        self.initBody()
    def initBody(self):
        resultLayout = QHBoxLayout()
        resultLayout.setAlignment(Qt.AlignCenter)
        self.label = QLabel(self.FinalPath)
'''


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
