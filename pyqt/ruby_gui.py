# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\javie\Desktop\RUBY-LP\RUBYGUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 787)
        MainWindow.setMinimumSize(QtCore.QSize(1280, 720))
        MainWindow.setStyleSheet("background-color: rgb(35, 38, 46);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(35, 38, 46);")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 1261, 731))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.bt_archivo = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.bt_archivo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_archivo.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"border-color: rgb(35, 38, 46);\n"
"background-color: rgb(35, 38, 46);")
        self.bt_archivo.setObjectName("bt_archivo")
        self.horizontalLayout_2.addWidget(self.bt_archivo)
        self.bt_limpiar = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.bt_limpiar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_limpiar.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"border-color: rgb(35, 38, 46);\n"
"background-color: rgb(35, 38, 46);")
        self.bt_limpiar.setObjectName("bt_limpiar")
        self.horizontalLayout_2.addWidget(self.bt_limpiar)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.bt_lexico = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.bt_lexico.setFont(font)
        self.bt_lexico.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_lexico.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"border-color: rgb(35, 38, 46);\n"
"background-color: rgb(35, 38, 46);")
        self.bt_lexico.setObjectName("bt_lexico")
        self.horizontalLayout_4.addWidget(self.bt_lexico)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.gridLayout.addLayout(self.horizontalLayout_4, 1, 1, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.bt_sintactico = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.bt_sintactico.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_sintactico.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"border-color: rgb(35, 38, 46);\n"
"background-color: rgb(35, 38, 46);")
        self.bt_sintactico.setObjectName("bt_sintactico")
        self.horizontalLayout_5.addWidget(self.bt_sintactico)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.gridLayout.addLayout(self.horizontalLayout_5, 3, 1, 1, 1)
        self.tx_ingreso = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.tx_ingreso.setStyleSheet("color: rgb(255, 255, 255);")
        self.tx_ingreso.setObjectName("tx_ingreso")
        self.gridLayout.addWidget(self.tx_ingreso, 2, 0, 3, 1)
        self.tx_sintactico = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.tx_sintactico.setStyleSheet("color: rgb(255, 255, 255);")
        self.tx_sintactico.setObjectName("tx_sintactico")
        self.gridLayout.addWidget(self.tx_sintactico, 4, 1, 1, 1)
        self.tx_lexico = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.tx_lexico.setStyleSheet("color: rgb(255, 255, 255);")
        self.tx_lexico.setObjectName("tx_lexico")
        self.gridLayout.addWidget(self.tx_lexico, 2, 1, 1, 1)
        self.gridLayout.setColumnMinimumWidth(0, 1)
        self.gridLayout.setColumnMinimumWidth(1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Ruby IDE"))
        self.bt_archivo.setText(_translate("MainWindow", "Cargar archivo"))
        self.bt_limpiar.setText(_translate("MainWindow", "Limpiar"))
        self.bt_lexico.setText(_translate("MainWindow", "Analisis lexico"))
        self.bt_sintactico.setText(_translate("MainWindow", "Analisis sintactico"))
        self.tx_ingreso.setPlaceholderText(_translate("MainWindow", "Escribe tu codigo aqui o carga un archivo"))
        self.tx_sintactico.setPlaceholderText(_translate("MainWindow", "Aqui apareceran los errores sintacticos"))
        self.tx_lexico.setPlaceholderText(_translate("MainWindow", "Aqui apareceran los tokens reconocidos"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())