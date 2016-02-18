import math

gravedad = 9.8
masa = 68.1
c = 12.5

for t in range(60):
    velocidad = ((gravedad*masa)/c)*(1-(math.exp((-c/masa)*t)))
    print "Tiempo: "+str(t) + "\tVelocidad " + str(velocidad)