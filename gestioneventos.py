import datetime

evento=[]
matrizevento=[]
fechascargadas=[]
listainvitados=[]
dicinvitados={}
costoporpersona=20000

'''
1. Gestion de eventos:

    .Fecha evento-
    .Persona evento-
    .Tipo de evento
    .horario de evento
    -valor del evento
    -cantidad de personas
    -contacto
    .no se superponga dos eventos
    .tope capacidad de personas
    .precio variable depende la cantidad de persona, fecha,
    .dispibilidad de fecha, en caso de no haber preguntar si desea una nueva fecha
    .dispobilidad de comida
    .funcion de presupuesto con ticket
    .contacto
    .metodo de pago
    .cancelar el contrato
    .agregar al diccionario como key el fechaevento de la persona

'''
def checkfecha(cantdias, mes, year): #generamos una funcion para chequear que la fecha sea correcta

    if year>=2024:
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
            return False
    else: return False

def fechadisponible(fecha, tdfechas):
    
    if fecha in tdfechas:
        return True
    else:
        return False

def ques(letra):
    if letra=='yes' or letra =='YES':
        return True
    elif letra=='Y' or letra=='y':
        return True
    else: return False

while True:

    print('Sistema de gestion de eventos: \n\n 1. Gestion de eventos \n 2. Agregue un evento nuevo \n 3. Lista de invitados \n 4. Facturacion \n 5. Salir del menu\n\n ')
    sis=int(input('Ingrese el numero de programa a utilizar: '))

    match sis: #usamos un match case para seleccionar el menu a utilizar


        case 1:
            print('Panel sistema de gestion de eventos: ')




        case 2:

            confirmacion=True
            print('Panel agregado evento nuevo: ')
            while confirmacion:

                
                nombre=str(input('Ingrese el nombre del evento: '))
                evento.append(nombre)
                fechaevento= input('Ingrese la fecha del evento (DD-MM-AAAA): ')
                dia, mes, anio= map(int, fechaevento.split('-')) #mediante una funcion map separamos la fecha ingresada en la variable fechaevento
                fechavalida= checkfecha(dia, mes, anio)
                yacargado= fechadisponible(fechaevento,fechascargadas)
            
                if fechavalida and not yacargado:
                    date= datetime.date(anio, mes, dia) #utilizamos la libreria datetime para poder mostrar la fecha de una manera mas profesional, y pensando en cuando actualicemos el programa
                while fechavalida==False or yacargado:
                    fechaevento= input('Ingrese la fecha del evento correctamente (DD-MM-AAAA): ')
                    dia, mes, anio= map(int, fechaevento.split('-'))
                    fechavalida= checkfecha(dia, mes, anio)
                    yacargado= fechadisponible(fechaevento, fechascargadas)
                    date= datetime.date(anio, mes, dia)
                
                evento.append(date.strftime('%m/%d/%y'))
                fechascargadas.append(fechaevento)

                nombrepersona= str(input('Ingrese el nombre de la persona: '))
                evento.append(nombrepersona)
                dnipersona= int(input('Ingrese el dni de la persona: '))
                evento.append(dnipersona)
                cantinvitados= int(input('Ingrese la cantidad de invitados: '))
                evento.append(cantinvitados)
                valorevento=cantinvitados*costoporpersona
                print(f'El valor del evento es {valorevento}')
                evento.append(valorevento)
                acepta= str(input('Acepta el contrato Y (YES) / N (NO)?: '))
                acepta=ques(acepta)
                if acepta:
                    matrizevento.append(evento)#guardamos la lista evento generando asi una matriz con los eventos
                    evento=[]
                else:
                    evento=[]#limpiamos la lista remplazandola por una lista vacia dado que el clear funciona insitu y borra la lista evento
                confirmacion= str(input('Desea agregar otro evento Y (YES) / N (NO)?: '))
                confirmacion=ques(confirmacion)

        case 3:
            print('Lista de invitados: ')
            
            dnis= list(dicinvitados.keys)
            for l in range(len(dnis)):
                print(dnis[l])
                print('')

            n=int(input('Ingrese '))

        case 4:
            print('Facturacion')

            if len(matrizevento)==0:
                print('-'*40)
                print('\nNo hay eventos proximos\n')
                print('-'*40)
            else:
                for c in range(len(matrizevento)):
                    for f in range(len(matrizevento[0])):
                        pass
                    print(f'{c} -',matrizevento[c][0])
                nroevento=int(input('Elija uno de los eventos para realizar la factura: '))
                nombre=matrizevento[nroevento][0]
                valorevento=matrizevento[nroevento][5]
                nombrepersona=matrizevento[nroevento][2]
                dnipersona=matrizevento[nroevento][3]

                print('-'*40)
                print('Facturacion Eventos'.center(40)) 
                print()
                print()
                print(str(f'Sr/a {nombrepersona}').ljust(30))
                print(str(f'DNI: {dnipersona}'.rjust(10)))
                print()
                print(str(nombre).ljust(30,'.'),end='')
                print(str(valorevento).rjust(10,'.'))
                print('-'*40)
            
            


        case 5:
            print('Salir')
            break


