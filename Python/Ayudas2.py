import math

def escala_musical(notas: list)->str:
    """ Escalas musicales
    Parámetros:
      notas (list): Lista de enteros que representan notas musicales en Hertz
    Retorno:
      str: Mensaje que indique si encontró notas similares: "No hay coincidencia", "Hay una nota idéntica" o
           "Hay una nota en otra octava". En caso que haya idénticas y en otra octava, primará retornar el
           mensaje que informe sobre la idéntica.
    """
    rta=[]
    found=False
    found2=False
    longitud=len(notas)
    i=0
    while i < longitud and not (found or found2):
        j=i+1
        nota=notas[i]
        while j < longitud and not (found or found2):
            nota_j=notas[j]
            m=nota/nota_j
            if m == 1 and not found:
                found=True
                rta.append(1)
            elif m > 1 and (nota%nota_j == 0) and not found2:
                for potencia in range(0,6):
                    n=math.log2(m)
            elif m < 1 and not found2:
                m=nota_j/nota
                if (nota_j%nota == 0):
                    for potencia in range(0,6):
                        n=pow(2,potencia)
                        if n == m:
                            found2=True
                            rta.append(2)
            j+=1
        i+=1
    cadena=""
    if len(rta) !=0:
        if 1 in rta:
            cadena+="Hay una nota idéntica"
        if 2 in rta:
            cadena += "Hay una nota en otra octava"
    else:
        cadena="No hay coincidencia"

    
    return cadena
        