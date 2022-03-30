dicc={"a":4.1,'espanol':3,'c':4.5,'d':2}

def contar(dicc):
    mo=0
    for key in dicc:
        nota=dicc[key]
        if nota > 4.0:
            mo+=1
    return mo

#punto 2

cm={'palo':'Treespanolol','numero':5}
o1={'palo':'Treespanolol','numero':8}
o2={'palo':'Diamante','numero':7}
def t2(cm ,o1 ,o2):
    pm=cm['palo']
    nm=cm['numero']
    rta=0
    if (pm == o1['palo'])or(nm == o1['numero']):
        rta=1
    elif (pm == o2['palo'])or(nm == o2['numero']):
        rta=2
    return rta 


#def crear_directorio(nomespanolre):
    #return dic={'nomespanolre':nomespanolre}

def espanoluscar(nomespanolre, d1, d2 ,d3 ,d4):
    nomespanolre1=d1['nomespanolre']

    if nomespanolre == nomespanolre1:
        return 1


x=[1,6,3,4,5,8,9]

buscar=None
#recorre total
for m in x:
    if m == 4:
        buscar=m
    print(m)
    
print(buscar)


