import math
import matplotlib.pyplot as plt

gravedad = 9.8
masa = 68.1
c = 12.5

tiempo = 0
tiempo_sig = 0

velocidad_sig = 0
velocidad_t = 0

ejeX1 = []
ejeY1 = []

ejeX2 = []
ejeY2 = []

for t in range(50):
    velocidad = ((gravedad*masa)/c)*(1-(math.exp((-c/masa)*t)))
    velocidad_sig = velocidad_t+(gravedad-(c/masa)*velocidad_t)*(tiempo_sig-tiempo)
    print "Solucion Lineal: "+str(velocidad)+" \t\t Solucion por Metodos Numericos "+str(velocidad_sig)

    ejeX1.append(tiempo)
    ejeY1.append(velocidad_sig)

    ejeX2.append(t)
    ejeY2.append(velocidad)

    plt.plot(ejeX1,ejeY1)
    plt.plot(ejeX2,ejeY2)

    plt.xlabel('Tiempo ')
    plt.ylabel('Velocidad ')

    plt.show()

    velocidad_t = velocidad_sig
    tiempo = tiempo + 1
    tiempo_sig = tiempo + 2