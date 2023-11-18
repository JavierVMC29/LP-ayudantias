# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ayudantia_2023SbsnPT.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLayout,
    QMainWindow, QMenuBar, QPlainTextEdit, QPushButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1125, 770)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_6 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setSizeConstraint(QLayout.SetNoConstraint)
        self.verticalLayout_5.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(25)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetMaximumSize)
        self.horizontalLayout_2.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.bt_archivo = QPushButton(self.centralwidget)
        self.bt_archivo.setObjectName(u"bt_archivo")
        self.bt_archivo.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.bt_archivo)

        self.bt_limpiar = QPushButton(self.centralwidget)
        self.bt_limpiar.setObjectName(u"bt_limpiar")
        self.bt_limpiar.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.bt_limpiar)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.tx_ingreso = QPlainTextEdit(self.centralwidget)
        self.tx_ingreso.setObjectName(u"tx_ingreso")

        self.verticalLayout_3.addWidget(self.tx_ingreso)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.bt_lexico = QPushButton(self.centralwidget)
        self.bt_lexico.setObjectName(u"bt_lexico")
        self.bt_lexico.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.bt_lexico)

        self.tx_lexico = QPlainTextEdit(self.centralwidget)
        self.tx_lexico.setObjectName(u"tx_lexico")

        self.verticalLayout.addWidget(self.tx_lexico)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.bt_sintactico = QPushButton(self.centralwidget)
        self.bt_sintactico.setObjectName(u"bt_sintactico")
        self.bt_sintactico.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_sintactico.setAutoFillBackground(False)

        self.verticalLayout_2.addWidget(self.bt_sintactico)

        self.tx_sintactico = QPlainTextEdit(self.centralwidget)
        self.tx_sintactico.setObjectName(u"tx_sintactico")

        self.verticalLayout_2.addWidget(self.tx_sintactico)


        self.verticalLayout.addLayout(self.verticalLayout_2)


        self.verticalLayout_4.addLayout(self.verticalLayout)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1125, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Proyecto LP", None))
        self.bt_archivo.setText(QCoreApplication.translate("MainWindow", u"Cargar archivo", None))
        self.bt_limpiar.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.bt_lexico.setText(QCoreApplication.translate("MainWindow", u"Analisis lexico", None))
        self.bt_sintactico.setText(QCoreApplication.translate("MainWindow", u"Analisis sintactico", None))
    # retranslateUi



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())