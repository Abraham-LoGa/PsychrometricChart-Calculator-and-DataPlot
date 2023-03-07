import pandas as pd
import numpy as np
class informacion_dias:
    def manejo_informacion(self,alt,path):
        
        alt = 2320
        atm = 101.325*pow(1-2.25577*(pow(10,-5)*(alt)),5.2559)
        excel = pd.read_excel(path)
        h_r = np.array(excel['Humedad relativa (%)'])
        t_b_s = np.array(excel['Temperatura del Aire (°C)'])
        filas = excel.shape[0]
        filas_d = int(filas/90)
        a_hr = 0
        a_c = 0
        cont = 1
        T_c = []
        T_k = []
        H_r = []
        Wr = []
        for i in range(filas):
            a_c = t_b_s[i]+a_c
            a_hr =h_r[i] + a_hr
            cont +=1
            if cont== filas_d:
                T_c.append(a_c/filas_d)
                T_k.append((a_c/filas_d)+273.15)
                H_r.append(a_hr/filas_d)
                a_hr = 0
                a_c = 0
                cont = 1
        for i in range(len(T_c)):
            pvs_ = self.pvs(T_k[i])
            pv_ = self.pv(pvs_,H_r[i])
            w_ = self.wr(pv_/1000,atm)
            Wr.append(w_)
    
        return T_c, Wr
    
    def pvs(self,tk):
        a1=-5.8002206*(pow(10,3))
        a2=1.3914993
        a3=-4.8640239*(pow(10,-2))
        a4=4.1764768*(pow(10,-5))
        a5=-1.4452093*(pow(10,-8))
        a6=6.5459673
        pvs=np.exp(a1/tk+a2+a3*tk+a4*(pow(tk,2))+a5*(pow(tk,3))+a6*np.log(tk))
        return pvs
    
    def pv(self,pvs,hr):
        pv = (pvs)*(hr/100)
        return pv
    
    def wr(self,pv,atm):
        W = 0.622*(pv/(atm-pv))
        return W
    





