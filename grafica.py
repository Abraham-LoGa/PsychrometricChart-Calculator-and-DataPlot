import matplotlib.pyplot as plt
from matplotlib import rc
import numpy as np
from manejo_datos import informacion_dias
def P_V_S(t):
        a1=-5.8002206*(pow(10,3))
        a2=1.3914993
        a3=-4.8640239*(pow(10,-2))
        a4=4.1764768*(pow(10,-5))
        a5=-1.4452093*(pow(10,-8))
        a6=6.5459673
        pvs=np.exp(a1/t+a2+a3*t+a4*(pow(t,2))+a5*(pow(t,3))+a6*np.log(t))
        return pvs

def grafica(z,tbsc,W,Ws,tpr,tbh):
        p_atm = 101.325*pow(1-2.25577*(pow(10,-5)*(z)),5.2559)
        # Matrices de apoyo
        T_c = np.zeros(36)
        pres = np.zeros(36)
        h_r = np.zeros((19,10))
        wr = np.zeros((19,10))
        Vesp = np.zeros((19,10))
        ve = np.zeros(19)
        w = np.zeros(19)
        h_ent = np.zeros((36,16))
        h = np.zeros(36) 
        c = 0.0
        prc = 1
        lr = 0.8
        aux = 10
        for i in range(0,36):
            if i == 0:
                T_c[i] = 0.1
                pres[i] = P_V_S(T_c[i]+273.15)*0.007501
            else:
                c+=5.0
                T_c[i]=c
                pres[i] = P_V_S(T_c[i]+273.15)*0.007501
              
        for i in range(10):
            for j in range(19):
                h_r[j][i] = pres[j]*prc
                wr[j][i] = (h_r[j][i]*0.622)/(p_atm*7.501-h_r[j][i])
                Vesp[j][i] = 18*(lr*((p_atm*1000)/101325)/(0.082*(T_c[j]+273.15))-1/29)
            lr +=0.05
            prc -=0.1
        
        for i in range(16):
            for j in range(36):
                h_ent[j][i] = ((aux)/4.18-(0.24*T_c[j]))/(0.46*T_c[j]+597.2)
            aux+=10

        x = np.linspace(-10,200)
        y = -0.00039*(x-tbsc)+W
        plt.figure()
        plt.title('Carta Psicrométrica', fontsize=10)
        axis= plt.gca()
        axis_ = plt.gca()
		  # Configuración de gráfica 
        axis.grid(True)
        axis.set_xticks(np.linspace(0,90,19))
        axis.set_xlim(0,50)
        axis.set_xlabel("Tbs(°C)")
        axis.set_yticks(np.linspace(0,120,11))
        axis.set_ylim(0,130)
        axis.set_ylabel(f"h(kJ/kg)")
        axis_ = axis.twinx()
        axis_.set_ylabel(r"W Kg/Kg" )
        axis_.set_ylim(0,0.05,11)
        axis_.plot(x,y,"g-.", linewidth=2, label ='H')
        axis_.axhline(W,color="#00ff0a",linewidth=2, label = 'W' )
        axis_.axhline(Ws,color="#ff41ce",linewidth=2,label = 'Ws' )
        axis_.axvline(tpr,color="#FFF043", linewidth=2, label = 'TPR' )
        axis_.axvline(tbh,color="brown", linewidth=2, label = 'TBH' )
        for i in range (16):
            for j in range (36):
                h[j]=h_ent[j][i]
            axis_.plot(T_c,h,"k--",linewidth=1)
        
        for i in range (10):
            for j in range (19):
                ve[j]=Vesp[j][i]
                w[j]=wr[j][i]
            axis_.plot(T_c[:19],ve,"k-.",linewidth=1)
            axis_.plot(T_c[:19],w,"k-",linewidth=1)
        
        axis_.plot(tbsc,W,"bo")
        axis_.legend(loc = "upper right")
        plt.show()

def graficar_datos(alt, path):
        t_c, rW = informacion_dias().manejo_informacion(alt, path)
        p_atm = 101.325*pow(1-2.25577*(pow(10,-5)*(alt)),5.2559)
        # Matrices de apoyo
        T_c = np.zeros(36)
        pres = np.zeros(36)
        h_r = np.zeros((19,10))
        wr = np.zeros((19,10))
        Vesp = np.zeros((19,10))
        ve = np.zeros(19)
        w = np.zeros(19)
        h_ent = np.zeros((36,16))
        h = np.zeros(36) 
        c = 0.0
        prc = 1
        lr = 0.8
        aux = 10
        for i in range(0,36):
            if i == 0:
                T_c[i] = 0.1
                pres[i] = P_V_S(T_c[i]+273.15)*0.007501
            else:
                c+=5.0
                T_c[i]=c
                pres[i] = P_V_S(T_c[i]+273.15)*0.007501
              
        for i in range(10):
            for j in range(19):
                h_r[j][i] = pres[j]*prc
                wr[j][i] = (h_r[j][i]*0.622)/(p_atm*7.501-h_r[j][i])
                Vesp[j][i] = 18*(lr*((p_atm*1000)/101325)/(0.082*(T_c[j]+273.15))-1/29)
            lr +=0.08
            prc -=0.1
        
        for i in range(16):
            for j in range(36):
                h_ent[j][i] = ((aux)/4.18-(0.24*T_c[j]))/(0.46*T_c[j]+597.2)
            aux+=10

        plt.figure()
        plt.title('Carta Psicrométrica', fontsize=10)
        axis= plt.gca()
        axis_ = plt.gca()
		  # Configuración de gráfica 
        axis.grid(True)
        axis.set_xticks(np.linspace(0,90,19))
        axis.set_xlim(0,50)
        axis.set_xlabel("Tbs(°C)")
        axis.set_yticks(np.linspace(0,120,11))
        axis.set_ylim(0,130)
        axis.set_ylabel(f"h(kJ/kg)")
        axis_ = axis.twinx()
        axis_.set_ylabel(r"W Kg/Kg" )
        axis_.set_ylim(0,0.05,11)
        for i in range (16):
            for j in range (36):
                h[j]=h_ent[j][i]
            axis_.plot(T_c,h,"k--",linewidth=1)
        
        for i in range (10):
            for j in range (19):
                ve[j]=Vesp[j][i]
                w[j]=wr[j][i]
            axis_.plot(T_c[:19],ve,"k-.",linewidth=1)
            axis_.plot(T_c[:19],w,"k-",linewidth=1)
        
        axis_.plot(t_c[:30],rW[:30],"r*", label = 'Mes 1')
        axis_.plot(t_c[31:60],rW[31:60],"g*", label = 'Mes 2')
        axis_.plot(t_c[61:],rW[61:],"b*", label = 'Mes 3')
        axis_.legend(loc = "upper right")
        plt.show()
        