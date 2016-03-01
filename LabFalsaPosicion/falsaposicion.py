import math
import numpy as np
import pylab as pl
valoresx = []
valoresy = []
valoresejex=[]
valoresejey=[]
o=[]
ok=[]

g=9.8
m=68.1
t=10
v=40
Xl=12.0
Xu=16.0
x=12        
i=0

def f(c):
    return ((g*m/c)*(1-math.exp(-(c/m)*t)))-v

def fxr(xl,xu):
    return xu-((f(xu)*(xl-xu))/(f(xl)-f(xu)))

if((f(Xl)*f(Xu))<0):
    Xr=fxr(Xl,Xu)

print "Xl\t\tXu\t\tXr"
print '{0:3}  {1:12}   {2:12}'.format(Xl,Xu,Xr)

aux=0
while((f(Xl)*f(Xr))!=0):
    if((f(Xl)*f(Xr))<0):
        Xu=Xr
        Xr=fxr(Xl,Xu)
        #print xl," ",xu," ",xr
        print '{0:3}  {1:12}   {2:12}'.format(Xl,Xu,Xr)
        
    else:
        if((f(Xl)*f(Xr))>0):
            Xl=Xr
            Xr=fxr(Xl,Xu)
            #print xl," ",xu," ",xr
            print '{0:3}  {1:12}   {2:12}'.format(Xl,Xu,Xr)


while(i<=20):
    valoresejex.append(i)
    valoresejey.append(0)
    i+=1
while(x<=16):
    valoresx.append(x)
    valoresy.append(f(x))
    x=x+0.01



o.append(0)   
ok.append(Xr )   
            
f1=  pl.plot(valoresx,valoresy,"g")
f2=  pl.plot(valoresejex,valoresejey,"k")
f3=  pl.plot(ok,o,".")


pl.title("Falsa Posicion")
pl.xlabel("c")
pl.ylabel("f(c)")
f=["funcion"]
pl.legend(f,loc=4)
pl.xlim(11,17)
pl.ylim(-4, 7)
pl.grid(True)

pl.show()
