def escala_musical(notas: list)->str:
    """ Escalas musicales
    Parámetros:
      notas (list): Lista de enteros que representan notas musicales en Hertz
    Retorno:
      str: Mensaje que indique si encontró notas similares: "No hay coincidencia", "Hay una nota idéntica" o
           "Hay una nota en otra escala". En caso que haya idénticas y en otra escala, primará retornar el
           mensaje que informe sobre la idéntica.
    """
    if len(notas)==0:
        return "No hay coincidencia"
    
    i=0
    notas1={}
    for valor in notas:
        notas1[valor]= notas1.get(valor,0)+1
        i=i+1
        
    for llave, valor in notas1.items():
        if valor>1:
            return "Hay una nota idéntica"
    
    for valor in notas:
        inicial=-5
        control=True
        while control:
            calculo=valor*(pow(2,inicial))
            if calculo in notas:
                return "Hay una nota en otra escala"
            if inicial==-1:
                control=False
            inicial=inicial+1
        
        inicial2=2
        control2=True
        while control2:
            calculo2=valor*(pow(2,inicial2))
            if calculo2 in notas:
                return "Hay una nota en otra escala"
            if inicial2==5:
                control2=False
            inicial2=inicial2+1
        

    return "No hay coincidencia"
    
































