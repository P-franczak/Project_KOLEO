from PyQt5.QtGui import QPalette, QColor, QPixmap
from PyQt5.QtWidgets import QPushButton, QComboBox, QWidget, QLabel, QStackedWidget, QApplication, QHBoxLayout, QVBoxLayout, QListWidget, QListWidgetItem, QLineEdit
from PyQt5.QtCore import Qt, QSize
from dikstra import tabu_search, lista_sasiedztwa_enum
import sys
import os

from baza_danych import mapa_stacji, Stacja

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

        self.startPoint = QComboBox(); self.startPoint.addItems(mapa_stacji.values())
        self.startPoint.setStyleSheet('font-size: 18px')
        self.startPoint.setMinimumSize(160, 20)
        self.endPoint = QComboBox(); self.endPoint.addItems(mapa_stacji.values())  
        self.endPoint.setStyleSheet('font-size: 18px') 
        self.endPoint.setMinimumSize(160, 20) 
        self.maxIter = QLineEdit(); self.maxIter.setPlaceholderText('Limit iteracji')
        self.maxIter.setFixedSize(90, 30)
        self.tabuLen = QLineEdit(); self.tabuLen.setPlaceholderText('Długość tabu')
        self.tabuLen.setFixedSize(90, 30)
        self.aspIter = QLineEdit(); self.aspIter.setPlaceholderText('Kryt. aspiracji')
        self.aspIter.setFixedSize(90, 30)

        self.b1 = QPushButton('Szukaj'); self.b1.setStyleSheet('font-size: 30px')
        self.b1.clicked.connect(self.started)
        
        menuLayout.addWidget(self.label)
        menuLayout.addWidget(self.startPoint)
        menuLayout.addWidget(self.endPoint)
        menuLayout.addWidget(self.maxIter)
        menuLayout.addWidget(self.tabuLen)
        menuLayout.addWidget(self.aspIter)
        menuLayout.addWidget(self.b1)


        self.resPath = QListWidget(); self.resPath.setStyleSheet('font-size: 25px')
        self.resPath.setMinimumSize(500, 200)
        self.resPath.setEnabled(False)
        self.iterImage = QLabel()
        resultImage = QPixmap('tlo.png')
        self.iterImage.setPixmap(resultImage)
        self.iterImage.setScaledContents(True)
        resultLayout.addWidget(self.resPath)
        resultLayout.addWidget(self.iterImage)
        
        vertLayout.addLayout(menuLayout)
        vertLayout.addLayout(resultLayout)

        self.setLayout(vertLayout)
    def started(self):
        start = self.startPoint.currentText()
        end = self.endPoint.currentText()
        maxIter = int(self.maxIter.text())
        tabuLen = int(self.tabuLen.text())
        aspIter = int(self.aspIter.text())
        finalPath, finalValue = tabu_search(start, end, lista_sasiedztwa_enum, max_iter=maxIter, dlugosc_tabu=tabuLen, aspiracja_iter = aspIter)
        #finalPath, finalValue = tabu_search("Balin", 'Kraków Łobzów', lista_sasiedztwa_enum, max_iter=50, dlugosc_tabu=10, aspiracja_iter = 10)
        self.resPath.clear()
        self.resPath.addItem('')
        for row, station in enumerate(finalPath):
            item = QListWidgetItem(station[0])
            item.setTextAlignment(Qt.AlignCenter)
            self.resPath.addItem(item)
        item = QListWidgetItem(finalPath[-1][1])
        item.setTextAlignment(Qt.AlignCenter)
        self.resPath.addItem(item)
        self.resPath.addItem('')
        self.resPath.addItem('')
        item = QListWidgetItem(f'Wartość funkcji celu: {finalValue}')
        item.setTextAlignment(Qt.AlignCenter)
        self.resPath.addItem(item)

        resultImage = QPixmap('wykres.jpg')
        self.iterImage.setPixmap(resultImage)


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
