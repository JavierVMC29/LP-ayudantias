import sys

from PySide6.QtWidgets import (QApplication, QMainWindow, QFileDialog)

from gui import *
from lexico import *
from sintactico import *


class Main(QMainWindow):

    def __init__(self):

        QMainWindow.__init__(self)

        self.home = Ui_MainWindow()
        self.home.setupUi(self)

        self.home.bt_lexico.clicked.connect(self.ev_lexico)
        self.home.bt_sintactico.clicked.connect(self.ev_sintactico)

        self.home.bt_archivo.clicked.connect(self.ev_archivo)
        self.home.bt_limpiar.clicked.connect(self.ev_limpiar)

    def ev_lexico(self):
        '''
        Manejo de analisis de expresion lexemas
        '''

        self.home.tx_lexico.setPlainText('')

        datos = self.home.tx_ingreso.toPlainText().strip()

        resultado_lexico = analisis_lexico(datos)

        cadena = ''
        for lex in resultado_lexico:
            cadena += lex + "\n"
        self.home.tx_lexico.setPlainText(cadena)

    def ev_sintactico(self):
        '''
        Manejo de analisis sintactico
        '''

        self.home.tx_sintactico.setPlainText('')

        datos = self.home.tx_ingreso.toPlainText().strip()

        resultado_sintactico = analisis_sintactico(datos)
        cadena = ''

        for item in resultado_sintactico:
            cadena += item + "\n"

        self.home.tx_sintactico.setPlainText(cadena)

    def ev_archivo(self):
        '''
        Manejo de subir archivo
        '''
        dlg = QFileDialog()

        if dlg.exec():
            filenames = dlg.selectedFiles()
            f = open(filenames[0], 'r')

            with f:
                data = f.read().strip()
                if data:
                    self.home.tx_ingreso.setPlainText(data + "\n")

    def ev_limpiar(self):
        '''
        Manejo de limpieza de campos
        '''
        self.home.tx_ingreso.setPlainText('')
        self.home.tx_lexico.setPlainText('')
        self.home.tx_sintactico.setPlainText('')


def iniciar():

    app = QApplication(sys.argv)

    ventana = Main()

    ventana.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    iniciar()