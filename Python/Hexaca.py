
def calculadora_bi(n):
    bi=[]
    condicion= True
    while condicion:
        res=str(n%2)
        n=n//2
        bi.insert(0,res)
        if n == 0 or n == 1:
            condicion = False
    bi.insert(0, str(n))
    numero = "".join(bi)
    numero=int(numero)
    return numero 

def completar(n):
    numero=list(str(n))
    m=len(numero)
    z=4-(m%4)+1

    for i in range(z):
        numero.insert(0,"0")
    print(numero)
    x="".join(numero)
    return x

#print(completar(1100100))

def calculadora_hexa(n):
    contador=0
    Hexa=[]
    condicion = True
    while condicion:
        res=n%16
        Hexa.insert(0,res)
        n=n//16
        if n <16:
            condicion=False
        contador+=1
    
    Hexa.insert(0,n)
    Hexa_new=[]
    for cifra in Hexa:
        if cifra >= 10:
            cifra=chr(ord(str(cifra)[0])+16)
        else:
            Hexa_new.append(str(cifra))
    
    trad= "".join(Hexa_new)

    return trad

print(calculadora_hexa(100))
