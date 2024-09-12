import datetime
'''
1. Gestion de eventos:

    .Fecha evento
    .Persona evento
    .Tipo de evento
    .horario de evento
    -valor del evento
    -cantidad de personas
    -contacto
'''
def checkfecha(cantdias, mes, year): #generamos una funcion para chequear que la fecha sea correcta

    if year<1900: #usamos el año 1900 dado que es el año a partir de donde funciona la libreria datetime
        return False
    else: return True

    if mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:
        if cantdias<=31 and cantdias>0:
            return True
        else: return False
    elif mes==4 or mes==6 or mes==9 or mes==11:
        if cantdias<=30 and cantdias>0:
            return True
        else: return False
    elif mes==2:
        if year%4==0 and year%100!=0 or year%400==0: #chequeamos los años biciestos
            if cantdias<=29 and cantdias>0:
                return True
            else: return False
        elif cantdias<=28 and cantdias>0:
            return True
        else: return False
    else:
        cantdias = False


def fechadisponible():

    pass


print('Sistema de gestion de eventos: \n\n 1. Gestion de eventos \n 2. Agregue un evento nuevo \n 3. Lista de invitados \n\n ')
sis=int(input('Ingrese el numero de programa a utilizar: '))

match sis: #usamos un match case para seleccionar el menu a utilizar

    case 1:
        print('Panel sistema de gestion de eventos: ')


    case 2:

        evento=[]
        matrizevento=[]
        print('Panel agregado evento nuevo: ')
        nombre=str(input('Ingrese el nombre del evento: '))
        evento.append(nombre)
        fechaevento= input('Ingrese la fecha del evento (DD-MM-AAAA): ')
        dia, mes, anio= map(int, fechaevento.split('-')) #mediante una funcion map separamos la fecha ingresada en la variable fechaevento
        fechavalida= checkfecha(dia, mes, anio)
        if fechavalida:
            date= datetime.date(anio, mes, dia) #utilizamos la libreria datetime para poder mostrar la fecha de una manera mas profesional, y pensando en cuando actualicemos el programa
        while fechavalida==False:
            fechaevento= input('Ingrese la fecha del evento (DD-MM-AAAA): ')
            dia, mes, anio= map(int, fechaevento.split('-'))
            fechavalida= checkfecha(dia, mes, anio)
            date= datetime.date(anio, mes, dia)
        evento.append(date.strftime('%m/%d/%y'))
        nombrepersona= str(input('Ingrese el nombre de la persona: '))
        evento.append(nombrepersona)
        cantinvitados= int(input('Ingrese la cantidad de invitados: '))
        evento.append(cantinvitados)
        valor= int(input('Ingrese el valor del evento: '))
        evento.append(valor)
        matrizevento.append(evento)#guardamos la lista evento generando asi una matriz con los eventos
        evento=[]#limpiamos la lista remplazandola por una lista vacia dado que el clear funciona insitu y borra la lista evento
        confirmacion= str(input('Desea agregar otro evento Y (YES) / N (NO)?: '))
        while confirmacion=='Y' or confirmacion=='y':
            nombre=str(input('Ingrese el nombre del evento: '))
            evento.append(nombre)
            fechaevento= input('Ingrese la fecha del evento (DD-MM-AAAA): ')
            dia, mes, anio= map(int, fechaevento.split('-'))
            fechavalida= checkfecha(dia, mes, anio)
            if fechavalida:
                date= datetime.date(anio, mes, dia)
            while fechavalida==False:
                fechaevento= input('Ingrese la fecha del evento (DD-MM-AAAA): ')
                dia, mes, anio= map(int, fechaevento.split('-'))
                fechavalida= checkfecha(dia, mes, anio)
                date= datetime.date(anio, mes, dia)
            evento.append(date.strftime('%m/%d/%y'))
            nombrepersona= str(input('Ingrese el nombre de la persona: '))
            evento.append(nombrepersona)
            cantinvitados= int(input('Ingrese la cantidad de invitados: '))
            evento.append(cantinvitados)
            valor= int(input('Ingrese el valor del evento: '))
            evento.append(valor)
            matrizevento.append(evento)
            evento=[]
            confirmacion= str(input('Desea agregar otro evento Y (YES) / N (NO)?: '))


        for fila in matrizevento: #mostramos la matriz (pero hay que corregir algunas de como lo mostramos)
            for elemento in fila:
                print(elemento, '\n')
            print('')
        


        
    
    case 3:
        print('Lista de invitados: ')


