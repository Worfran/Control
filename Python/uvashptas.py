def suficientes_uvas (cantidad_ivan: int, cantidad_nicolas: int,
                      cantidad_adriana:int,cantidad_verde: int,
                      cantidad_morada: int, cantidad_negra: int)-> str:
    ideal = 0
    solo_2 = False
    respuesta = ("al menos somos amigos")
    Disponibles_Ivan_Verdes = cantidad_verde
    if Disponibles_Ivan_Verdes >= cantidad_ivan:
        uvas_verdes_sobrantes = Disponibles_Ivan_Verdes - cantidad_ivan
        ideal += 1
        Disponibles_Nicolas = cantidad_morada + uvas_verdes_sobrantes
    else:
        Disponibles_Nicolas = cantidad_verde

    if cantidad_nicolas <= Disponibles_Nicolas:

        Consumidas_Nicolas = cantidad_nicolas- uvas_verdes_sobrantes
        Disponibles_Adriana = cantidad_morada - Consumidas_Nicolas + cantidad_negra

        ideal += 1
    else:
        Disponibles_Adriana = Disponibles_Nicolas + cantidad_morada

    if cantidad_adriana <= Disponibles_Adriana:

         ideal += 1
    solo_1 = False
    caso_1 = cantidad_verde +  cantidad_morada
    if cantidad_nicolas <= caso_1 : 
        solo_1 = True

        Disponibles_Adriana = caso_1 - cantidad_nicolas + cantidad_negra
        if Disponibles_Adriana >= cantidad_adriana :
            solo_2 = True 

    caso_2 = cantidad_morada + cantidad_negra
    if cantidad_ivan <= cantidad_verde :
        solo_1 = True
        Disponibles_Adriana = cantidad_verde -cantidad_ivan + caso_2
        if Disponibles_Adriana >= cantidad_adriana:
            solo_2 = True 

    caso_3 = cantidad_morada +  cantidad_verde 
    if cantidad_ivan <= cantidad_verde :
        solo_1 = True
        Disponibles_Nicolas = caso_3 - cantidad_ivan
        if Disponibles_Nicolas >= cantidad_nicolas :
            solo_2 = True 
    caso_4 = cantidad_verde + cantidad_morada + cantidad_negra 
    if cantidad_adriana <= caso_4 :
        solo_1 = True
        
    if ideal == 3:
        respuesta =("felices")

    elif solo_2 == True:
        respuesta = ("casi")
    elif solo_1 == True:
        respuesta = ("fallamos")

    return respuesta