import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout
from PyQt5.QtWidgets import QPushButton,QLineEdit, QSizePolicy

class Calculadora(QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setWindowTitle('CAlC PYTHON')
        self.setFixedSize(400,400)
        self.cw= QWidget()
        self.grid =QGridLayout(self.cw)

        """Cria display """
        self.display = QLineEdit()
        self.grid.addWidget(self.display, 0, 0, 1,5)
        self.setDisabled(True)
        self.setStyleSheet(
            '* {background : #FFF; color : #000; font-size:30px}'
        )
        self.display.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        self.setCentralWidget(self.cw)

if __name__ == '__main__':

    qt =QApplication(sys.argv)
    calc = Calculadora()
    calc.show()
    qt.exec_()