print "Ingrese un valor"
v = input()

def fx():
    x=1
    i=0
 

    while i<=v:
        calculo=0
        if i==0:
            calculo+=-0.1*(x**4)-0.15*(x**3)-0.5*(x**2)-0.25*x+1.2            
        elif i==1:
            calculo+=(-0.4*(x**3)-0.45*(x**2)-1*(x**1)-0.25)
        elif i==2:
            calculo+=(-1.2*(x**2)-0.90*x-1)/2
        elif i==3:
            calculo+=(-2.4*x-0.90)/6
        elif i==4:
            calculo+=(-2.4)/24
        i+=1 
    print "el valor de la orden ",v," es",calculo
    
    
print fx()