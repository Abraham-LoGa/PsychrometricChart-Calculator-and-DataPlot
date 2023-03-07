import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView, QFileDialog
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve
from PyQt5 import QtCore, QtWidgets
from PyQt5.uic import loadUi
import matplotlib.pyplot as plt
from matplotlib import rc
import numpy as np
import pandas as pd
from grafica import grafica, graficar_datos
class Main_Windows(QMainWindow):
    def __init__(self):
        super(Main_Windows, self).__init__()
        loadUi('CalculosPsicrometricos.ui', self)
        self.calcular.clicked.connect(self.calculo)
        self.graficar.clicked.connect(self.graficar_parametros)
        self.elegir.clicked.connect(self.seleccionar)
        self.graficar_.clicked.connect(self.graficar_varios_datos)
    
    def calculo(self):
        tbsc =float(self.tbsc_.text())
        hr = float(self.hr_.text())
        alt = float(self.z_.text())
        z = 101.325*pow(1-2.25577*(pow(10,-5)*(alt)),5.2559)
        t_k  = tbsc + 273.15

        # Presion de vapor saturado
        a1=-5.8002206*(pow(10,3))
        a2=1.3914993
        a3=-4.8640239*(pow(10,-2))
        a4=4.1764768*(pow(10,-5))
        a5=-1.4452093*(pow(10,-8))
        a7=6.5459673
        pvs=np.exp(a1/t_k+a2+a3*t_k+a4*(pow(t_k,2))+a5*(pow(t_k,3))+a7*np.log(t_k))

        # Presion de vapor
        pv = (pvs)*(hr/100)

        # Razón de Humedad
        pv_ = pv/1000
        w = 0.622*((pv_)/(z-pv_))
        
        # Razón de humedad Saturada
        pvs_ = pvs/1000
        ws = 0.622*((pvs_)/(z-pvs_))

        # Grado de Saturación
        u = w/ws
        
        # Volumen específico
        ve = (287.055*(t_k)/(z*1000))*((1+1.6078*w)/(1+w))

        # Punto de Rocío
        tpr = -35.957-1.8726*np.log(pv)+1.1689*(pow(np.log(pv),2))

        # Temperatura de Bulbo Húmedo
        tbh = tbsc-(0.0121*(tbsc)+0.2305)*(tbsc-tpr)

        # Entalpía
        h = 1.006*(tbsc)+w*(2501+1.805*(tbsc))

        self.params = [z, tbsc, pvs,  pv,  w,  ws,  u,  ve,  tpr,  tbh,  h]

        # Mostrar Datos
        self.pv_.setText("{:.6f}".format(pv))
        self.pvs_.setText("{:.6f}".format(pvs))
        self.u_.setText("{:.6f}".format(u))
        self.w_.setText("{:.6f}".format(w))
        self.ws_.setText("{:.6f}".format(ws))
        self.h_.setText("{:.6f}".format(h))
        self.tpr_.setText("{:.6f}".format(tpr))
        self.ve_.setText("{:.6f}".format(ve))
        self.tbh_.setText("{:.6f}".format(tbh))
    
    def graficar_parametros(self):

        grafica(self.params[0],self.params[1],self.params[4],self.params[5],self.params[8],self.params[9])
    
    def seleccionar(self):
        self.file = QFileDialog.getOpenFileName(self)
        name_file = self.file[0].split('/')[-1].split('.')[0]
        self.file_name.setText(name_file)
    def graficar_varios_datos(self):
        z = float(self.altura_.text())
        graficar_datos(z,self.file[0])







        




if __name__ == '__main__':
    app = QApplication(sys.argv)
    mi_app = Main_Windows()
    mi_app.show()
    sys.exit(app.exec_())