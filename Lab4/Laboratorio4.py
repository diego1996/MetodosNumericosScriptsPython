import math

e=0.0
n=0
Et=0.0
et=0.0
ea=0.0
es=0.05
while True:
    e2=e
    e += (math.pow(1/2, n)) / math.factorial(n)
    Et = (math.exp(1/2)) - e
    et = (Et / e) * 100
    ea = ((e - e2) / e) * 100
    n = n + 1
    cont = n - 1
    print (str(cont)+"\t\t"+str(e)+"\t\t"+str(et)+"\t\t"+str(ea))
    if str(ea)<=str(es):
        break
