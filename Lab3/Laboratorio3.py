import math
import pylab as plt

vertorx1 = []
vectory1 = []
vectorx = []
vectory = []

Error_relativo = 0
ver = 0
gravedad = 9.8
masa = 68.1
c = 12.5
ti = 0
tii = 0
ver2 = 0
v_an = 0

print("\t\tTiempo\t\tV_verdadero\t\tV_aproximado\t\tE_verdadero\t\tE_relativo\t\tE_R_Apoximado.")
print(" ")
for t in range(400):
    dos = t % 2
    if dos == 0:
        velocidad = round(((gravedad*masa)/c)*(1-math.exp((-c/masa)*t)),6)
        vectorx.append(t)
        vectory.append(velocidad)
        ti = ti+2
        ver = round(v_an,6)
        v_n = v_an + (gravedad-(c/masa)*v_an)*(ti-tii)
        v_an=v_n
        tii=ti
        if t > 0:
            Error_ver=round(velocidad-ver,6)
            Error_r_apro=round(((ver-ver2)/ver)*100,6)
            ver2=ver
            if str(Error_r_apro)<="0.005":
                break
            Error_relativo=round((Error_ver/ver)*100,6)
            vertorx1.append(abs(Error_relativo))
            vectory1.append(Error_r_apro)
            print '|{0:15} | {1:15} | {2:15} | {3:15}| {4:15}| {5:15}%|'.format(t,velocidad,ver,Error_ver,Error_relativo,Error_r_apro)
plt.plot(vertorx1,vectory1,'g')
plt.plot(vectorx,vectory,'*')
plt.xlabel('t')
plt.ylabel('V(t)')
plt.title('Laboratorio 3')
plt.grid(True)
plt.savefig("figura1.png")
plt.show()