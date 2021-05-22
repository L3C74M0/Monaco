# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfaceGUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ventana(object):
    def setupUi(self, ventana):
        ventana.setObjectName("ventana")
        ventana.resize(853, 549)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icono/img/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ventana.setWindowIcon(icon)
        ventana.setWindowOpacity(1.0)
        ventana.setStyleSheet("background-color: rgb(43, 43, 43);\n"
"gridline-color: rgb(27, 27, 27);\n"
"selection-background-color: rgb(27, 27, 27);\n"
"selection-color: rgb(27, 27, 27);\n"
"border-top-color: rgb(27, 27, 27);\n"
"border-color: rgb(27, 27, 27);")
        self.filtroRural = QtWidgets.QPushButton(ventana)
        self.filtroRural.setGeometry(QtCore.QRect(680, 120, 161, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.filtroRural.setFont(font)
        self.filtroRural.setStyleSheet("color: rgb(230, 230, 230);")
        self.filtroRural.setObjectName("filtroRural")
        self.filtroUrbano = QtWidgets.QPushButton(ventana)
        self.filtroUrbano.setGeometry(QtCore.QRect(680, 90, 161, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.filtroUrbano.setFont(font)
        self.filtroUrbano.setStyleSheet("color: rgb(230, 230, 230);")
        self.filtroUrbano.setObjectName("filtroUrbano")
        self.graficoDeBarras = QtWidgets.QPushButton(ventana)
        self.graficoDeBarras.setGeometry(QtCore.QRect(680, 150, 161, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.graficoDeBarras.setFont(font)
        self.graficoDeBarras.setStyleSheet("color: rgb(230, 230, 230);")
        self.graficoDeBarras.setObjectName("graficoDeBarras")
        self.graficoDeDispercion = QtWidgets.QPushButton(ventana)
        self.graficoDeDispercion.setGeometry(QtCore.QRect(680, 180, 161, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.graficoDeDispercion.setFont(font)
        self.graficoDeDispercion.setStyleSheet("color: rgb(230, 230, 230);")
        self.graficoDeDispercion.setObjectName("graficoDeDispercion")
        self.cargarMapa = QtWidgets.QPushButton(ventana)
        self.cargarMapa.setGeometry(QtCore.QRect(710, 310, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cargarMapa.setFont(font)
        self.cargarMapa.setStyleSheet("color: rgb(230, 230, 230);")
        self.cargarMapa.setObjectName("cargarMapa")
        self.graficoDeConfucion = QtWidgets.QPushButton(ventana)
        self.graficoDeConfucion.setGeometry(QtCore.QRect(680, 210, 161, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.graficoDeConfucion.setFont(font)
        self.graficoDeConfucion.setStyleSheet("color: rgb(230, 230, 230);")
        self.graficoDeConfucion.setObjectName("graficoDeConfucion")
        self.title = QtWidgets.QLabel(ventana)
        self.title.setGeometry(QtCore.QRect(230, 10, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(26)
        self.title.setFont(font)
        self.title.setStyleSheet("color: rgb(230, 230, 230);")
        self.title.setObjectName("title")
        self.labelUrbano = QtWidgets.QLabel(ventana)
        self.labelUrbano.setGeometry(QtCore.QRect(16, 62, 641, 451))
        self.labelUrbano.setStyleSheet("border-image: url(:/imagen/img/b5.tif);")
        self.labelUrbano.setText("")
        self.labelUrbano.setTextFormat(QtCore.Qt.AutoText)
        self.labelUrbano.setObjectName("labelUrbano")
        self.labelRural = QtWidgets.QLabel(ventana)
        self.labelRural.setGeometry(QtCore.QRect(16, 62, 641, 451))
        self.labelRural.setStyleSheet("border-image: url(:/imagen/img/b4.tif);")
        self.labelRural.setText("")
        self.labelRural.setObjectName("labelRural")
        self.labelBarras = QtWidgets.QLabel(ventana)
        self.labelBarras.setGeometry(QtCore.QRect(16, 62, 641, 451))
        self.labelBarras.setStyleSheet("border-image: url(:/graficoBarras/img/graficoBarras.png);")
        self.labelBarras.setText("")
        self.labelBarras.setObjectName("labelBarras")

        self.retranslateUi(ventana)
        QtCore.QMetaObject.connectSlotsByName(ventana)

    def retranslateUi(self, ventana):
        _translate = QtCore.QCoreApplication.translate
        ventana.setWindowTitle(_translate("ventana", "Clasificación del suelo Mónaco"))
        self.filtroRural.setText(_translate("ventana", "Filtro Rural"))
        self.filtroUrbano.setText(_translate("ventana", "Filtro Urbano"))
        self.graficoDeBarras.setText(_translate("ventana", "Grafico de Barras"))
        self.graficoDeDispercion.setText(_translate("ventana", "Grafico de Dispersión"))
        self.cargarMapa.setText(_translate("ventana", "Cargar Mapa"))
        self.graficoDeConfucion.setText(_translate("ventana", "Grafico de Confución"))
        self.title.setText(_translate("ventana", "Análisis Mónaco"))

import bandaSobreBanda_rc
import graficoBarras_rc
import graficoDispercion_rc
import icono_rc
import mapa1_rc
import mapa_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ventana = QtWidgets.QDialog()
    ui = Ui_ventana()
    ui.setupUi(ventana)
    ventana.show()
    sys.exit(app.exec_())

