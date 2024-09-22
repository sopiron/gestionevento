import datetime
import re

#Funcion para validar la fecha
def validarfecha(dia,mes,anio):
    if anio>=2024:
        if mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:
            if dia<=31 and dia>0:
                return True
            else:
                return False
        elif mes==4 or mes==6 or mes==9 or mes==11:
            if dia<=30 and dia>0:
                return True
            else:
                return False
        elif mes==2:
            if anio%4==0 and anio%100!=0 or anio%400==0: #Se verifica si es año bisiesto
                if dia<=29 and dia>0:
                    return True
                else:
                    return False
            elif dia<=28 and dia>0:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

#Funcion para validar que la fecha solo tenga numeros
def validar_numeros(valor_variable,nombre_variable):
    valido_variable = valor_variable.isdigit()
    while valido_variable == False:
        print(f"Error, {nombre_variable} solo puede contener numeros enteros")
        valor_variable = input(f'Ingrese {nombre_variable}: ')
        valido_variable = valor_variable.isdigit()
    return int(valor_variable)


#Funcion para verificar si la fecha ya esta reservada
def validar_fecha_cargada(fecha_evento,evento):
    fechaok = True
    if fecha_evento in evento:
        fechaok = False
        print(f"Lo lamento, la fecha {fecha_evento} ya esta reservada.")
        pregunta_reserva = input("¿Desea reservar otra fecha(1=Si y 2=No)?: ")
        valor_variable = validar_numeros(pregunta_reserva,"la respuesta con 1=Si o 2=No")
        while valor_variable != 1 or valor_variable != 2:
            print("Error, la respuesta solo admite los numeros 1=Si y 2=No")
            pregunta_reserva = input("Ingrese la respuesta con 1=Si o 2=No: ")
            valor_variable = validar_numeros(pregunta_reserva,"la respuesta con 1=Si o 2=No")
        if valor_variable == 1:
            pass
        else:
            fechaok = True
            print('Sistema de gestion de eventos: \n\n 1. Gestion de eventos \n 2. Agregue un evento nuevo \n 3. Cantidad de invitados de invitados \n 4. Facturacion \n 5. Salir del menu\n\n ')
            print("*"*40)
            menu = int(input('Ingrese el numero de programa a utilizar: '))
            validarmenu(menu)
    else:
        evento.append(fecha_evento)
    return fechaok

#Funcion para verificar que la cadena solo contenga letras
def validar_cadena_de_caracteres(valor_cadena,nombre_cadena):
    aux= str(valor_cadena).replace(' ', '')
    valido_cadena = aux.isalnum()
    while not valido_cadena:
        print("Solo puede contener caracteres alfanmericos")
        print("-"*40)
        valor_cadena = input(f'Ingrese {nombre_cadena}: ')
        aux= str(valor_cadena).replace(' ', '')
        valido_cadena = valor_cadena.isalnum()
    return valor_cadena

#Funciona para verificar la cadena Nombre Persona
def validar_cadena_nombre_persona(valor_cadena, nombre_cadena):
    aux= str(valor_cadena).replace(' ', '')
    valido_cadena = aux.isalpha()
    while not valido_cadena:
        print("Solo puede contener caracteres alfabeticos")
        print("-"*40)
        valor_cadena = input(f'Ingrese {nombre_cadena}: ')
        aux= str(valor_cadena).replace(' ', '')
        valido_cadena = aux.isalpha()
    return valor_cadena
#Funcion para validar menu
def validarmenu(menu):
    menu = validar_numeros(menu,"el numero de programa a utilizar")
    while menu < 1 or menu > 5:
        print("El numero de menu solicitado no esta disponible, por favor eliga un menu correcto: ")
        print("\n 1. Gestion de eventos \n 2. Agregue un evento nuevo \n 3. Cantidad de invitados de invitados \n 4. Facturacion \n 5. Salir del menu")
        print("*"*40)
        menu = input('Ingrese el numero de programa a utilizar: ')
        menu = validar_numeros(menu,"el numero de programa a utilizar")
    elegirmenu(menu)
    return int(menu)

#Funcion para validar string y para validar el tipo de evento
def validarevento(tipoevento):
    listatipoevento = dictipoevento.keys()
    valido = tipoevento.isalpha()
    
    while valido == False:
        print("Solo puede contener caracteres alfabeticos")
        tipoevento = input('Ingrese el tipo de evento: ')
        tipoevento = tipoevento.capitalize()
        valido = tipoevento.isalpha()

    while tipoevento not in listatipoevento:
        print("*Error, el evento solicitado no esta en las opciones. Por favor, seleccionee nuevamente el tipo de evento: *")
        for x in dictipoevento:
            print("-",x,":","$",dictipoevento[x])
        print()
        tipoevento = input('Ingrese el tipo del evento: ')
        tipoevento = tipoevento.capitalize()
    return tipoevento


#Funcion para agregar evento nuevo
def agregarnuevoevento(dictipoevento,evento):
    cantidad_invitados = []

    # Ingresar tipo de evento
    print("Seleccione el tipo de evento: ")
    for x in dictipoevento:
        print("-",x,":","$",dictipoevento[x])
    print()
    tipoevento = input('Ingrese el tipo de evento: ')
    tipoevento = tipoevento.capitalize()
    tipoevento = validarevento(tipoevento)
    evento.append(tipoevento)
    
    
    # Ingresar nombre de evento
    print()
    nombreevento = input("Ingrese el nombre del evento: ")
    nombreevento = validar_cadena_de_caracteres(nombreevento,"el nombre del evento")
    evento.append(nombreevento)
    
    # Ingresa fecha del evento
    fechaok = False
    while fechaok == False:
        print()
        dia = input("Ingrese dia del evento: ")
        dia = validar_numeros(dia,"el dia del evento")
        

        mes = input("Ingrese mes del evento: ")
        mes = validar_numeros(mes,"el mes del evento")
       
        
        anio = input("Ingrese anio del evento: ")
        anio = validar_numeros(anio,"el año del evento")
        
        
        #Se llama a la funcion validar fecha
        if validarfecha(dia,mes,anio):
            fechaok = True
            fecha_evento = datetime.date(anio,mes,dia)
            fechaok = validar_fecha_cargada(fecha_evento,evento)
            print (f"La fecha {fecha_evento} esta disponible")
        else:
            print("Error, la fecha es incorrecta, por favor vuelva a ingresar")
            
    #Ingresa nombre de la persona
    nombre_persona = input("Ingrese nombre: ")
    nombre_persona = validar_cadena_nombre_persona(nombre_persona,"el nombre: ")
    evento.append(nombre_persona)
    
    #Ingresa DNI de la persona
    dni_persona = input("Ingrese DNI: ")
    dni_persona = validar_numeros(dni_persona,"el DNI")
    while len(str(dni_persona)) != 8:
        print("El DNI no es correcto.")
        print("-"*40)
        dni_persona = input("Ingrese DNI: ")
        dni_persona = validar_numeros(dni_persona,"el DNI")
    evento.append(dni_persona)
    
    #Ingresa cantidad de invitados
    cantidad_jubilados = input("Ingrese la cantidad de personas mayores de 60 años: ")
    cantidad_jubilados = validar_numeros(cantidad_jubilados,"la cantidad de personas mayores de 60")
    cantidad_invitados.append(cantidad_jubilados)
    
    cantidad_adultos = input("Ingrese la cantidad de adultos: ")
    cantidad_adultos = validar_numeros(cantidad_adultos,"la cantidad de adultos")
    cantidad_invitados.append(cantidad_adultos)
    
    cantidad_menores = input("Ingrese la cantidad de menores: ")
    cantidad_menores = validar_numeros(cantidad_menores,"la cantidad de menores")
    cantidad_invitados.append(cantidad_menores)
    evento.append(cantidad_invitados)
    costo_evento=calcular_costo(cantidad_jubilados,cantidad_adultos,cantidad_menores,tipoevento)
    acepta= str(input(f'El costo del evento es de {costo_evento}, acepta el contrato? Y(YES) - N(NO)'))
    contrato= acepta_contrato(acepta)
    if contrato:
        print('acepta')
    if not contrato:
        print('no acepta')
    
        
        
    

#Funcion para elegir el menu
def elegirmenu(menu):
    match menu:
        case 1:
            pass
        case 2:
            print("• Panel para agregar un evento nuevo: \n")
            nuevoevento = agregarnuevoevento(dictipoevento,evento)
            
            
def calcular_costo(pers_may, pers_med, pers_men, event_type):
    total=0
    total= total+(pers_may*dicprecios["Jubilados"])
    total= total+(pers_med*dicprecios["Adultos"])
    total= total+(pers_men*dicprecios["Menores"])
    total= total+dictipoevento[str(event_type).capitalize()]
    return(total)
            
def acepta_contrato(respuesta):
    
    respuesta= validar_cadena_nombre_persona(respuesta, 'respuesta valida Y(YES) - N(NO)')
    while str(respuesta).lower != 'y' and str(respuesta).lower != 'n':
        respuesta= str(input('Ingrese una respuest valida Y(YES) - N(NO): '))
        respuesta= validar_cadena_nombre_persona(respuesta, 'respuesta valida Y(YES) - N(NO)')

    
    if str(respuesta).lower== 'y':
        acepta=True
    elif str(respuesta).lower=='n':
        acepta=False
    
    return acepta


################################################### Programa principal ###############################################################
evento=[]
matrizevento=[]
fechascargadas=[]
listainvitados=[]
dicprecios={'Jubilados' : 2000 ,'Adultos': 5000 , 'Menores' : 3000}
dictipoevento = {'Casamiento' : 500000 , 'Fiesta de quince' : 600000 , 'Comunion' : 400000 , 'Evento personalizado' : 300000}

print('Sistema de gestion de eventos: \n\n 1. Gestion de eventos \n 2. Agregue un evento nuevo \n 3. Cantidad de invitados de invitados \n 4. Facturacion \n 5. Salir del menu\n\n ')
print("*"*40)
menu = input('Ingrese el numero de programa a utilizar: ')
print("-"*40)

#Llamar funciones
validarmenu(menu)