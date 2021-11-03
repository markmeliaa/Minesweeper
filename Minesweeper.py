import pygame
from pygame.locals import *
import sys

from random import randint

# Constantes
C0='0'
C1='1'
C2='2'
C3='3'
C4='4'
C5='5'
C6='6'
C7='7'
C8='8'
CBOMBA='B'
CFLAG='F'
COCULTA='-'

def crear_tablero_visible(filas, columnas):
    # El código de la función debe ir aquí
    tablero_visible=[]
    for f in range(filas):
        tablero_visible.append([COCULTA]*columnas)

    return tablero_visible

def crear_tablero_oculto(filas, columnas):
    # El código de la función debe ir aquí
    tablero_oculto=[]
    for f in range(filas):
        tablero_oculto.append([C0]*columnas)

    return tablero_oculto

def poner_bombas_tablero_oculto(toculto, bombas):
    # El código de la función debe ir aquí
    while bombas>0:
        f=randint(0,len(toculto)-1)
        c=randint(0,len(toculto)-1)
        
        if toculto[f][c]!=CBOMBA:
            toculto[f][c]=CBOMBA
            bombas-=1
        else:
            bombas=bombas

    return toculto
            
def poner_info_tablero_oculto(toculto):
    filas = len(toculto)
    columnas = len(toculto[0])
    
    for f in range(filas):
        for c in range(columnas):
            if toculto[f][c] != CBOMBA:
                adyacentes = []
                ## Añadir a adyacentes las tres casillas superiores, si las hay
                ## (solo cuando f>0, teniendo en cuenta que para la superior izda
                ## c>0, y que para la superior dcha c<columnas-1)
                if f>0:
                    if toculto[f-1][c]==CBOMBA:
                        adyacentes.append(toculto[f-1][c])
                    if c>0 and toculto[f-1][c-1]==CBOMBA:
                        adyacentes.append(toculto[f-1][c-1])
                    if c<columnas-1 and toculto[f-1][c+1]==CBOMBA:
                        adyacentes.append(toculto[f-1][c+1])
                
                ## Añadir a adyacentes las casillas a la izda y la dcha, si las
                ## hay (teniendo en cuenta que para la izda c>0, y que para la
                ## dcha c<columnas-1)             
                if c>0 and toculto[f][c-1]==CBOMBA:
                    adyacentes.append(toculto[f][c-1])
                if c<columnas-1 and toculto[f][c+1]==CBOMBA:
                    adyacentes.append(toculto[f][c+1])
                    
                ## Añadir a adyacentes las tres casillas inferiores, si las hay                
                ## (solo cuando f<filas-1, teniendo en cuenta que para la inferior
                ## izda c>0, y que para la inferior dcha c<columnas-1)
                if f<filas-1:
                    if toculto[f+1][c]==CBOMBA:
                        adyacentes.append(toculto[f-1][c])
                    if c>0 and toculto[f+1][c-1]==CBOMBA:
                        adyacentes.append(toculto[f+1][c-1])
                    if c<columnas-1 and toculto[f+1][c+1]==CBOMBA:
                        adyacentes.append(toculto[f+1][c+1])
                        
                toculto[f][c] = len(adyacentes)

def imprimir_tablero(tablero):
    # El código de la función debe ir aquí
    for f in range(len(tablero)):
        for c in range(len(tablero[f])):
            print('{0}\t'.format(tablero[f][c]),end='')
        print()

def tablero_visible_destapar(tvisible, toculto, fila, columna):
    # El código de la función debe ir aquí
    if fila>(len(tvisible)-1) or fila>(len(toculto)-1):
        return
    elif columna>(len(tvisible[0])-1) or columna>(len(toculto[0])-1):
        return
    elif tvisible[fila][columna]==toculto[fila][columna]:
        return
    else:
        tvisible[fila][columna]=toculto[fila][columna]
        if toculto[fila][columna]==CBOMBA:
            return True
        else:
            return False
        
def tablero_visible_marcar(tvisible, fila, columna, onoff):
    # El código de la función debe ir aquí
    if fila>(len(tvisible)-1) or columna>(len(tvisible[0])-1):
        return
    else:
        if onoff==True:
            if tvisible[fila][columna]==CFLAG:
                return
            else:
                tvisible[fila][columna]=CFLAG
                return +1
        else:
            if tvisible[fila][columna]!=CFLAG:
                return
            else:
                tvisible[fila][columna]=COCULTA
                return -1

def comprobar_tablero_visible(tvisible, toculto, bombas):
    # El código de la función debe ir aquí
    for f in range(len(toculto)):
        for c in range(len(toculto[0])):
            if toculto[f][c]==CBOMBA:
                if tvisible[f][c]==CFLAG:
                    bombas-=1
    if bombas==0:
        return True
    else:
        return False

def menu_buscaminas():
    # El código de la función debe ir aquí
    opcion=0
    while opcion not in [1,2,3,4,5]:
        opcion=int(input('Elije una opción de las siguientes:\n 1.Destapar casilla\n 2.Marcar casilla\n 3.Desmarcar casilla\n 4.Bombas por detectar\n 5.Salir\n'))
    return opcion
    
def main():
    # El código de la función debe ir aquí
    print('¡Bienvenido al Buscaminas!')
    dificultad='D'
    while dificultad not in ['E','M','H']:
        dificultad=input('Elija un nivel de dificultad (E, M o H): ')
    if dificultad=='E':
        filas=8
        columnas=8
        bombas=10
    elif dificultad=='M':
        filas=16
        columnas=16
        bombas=40
    else:
        filas=16
        columnas=30
        bombas=99
    w=crear_tablero_visible(filas,columnas)
    k=crear_tablero_oculto(filas,columnas)
    poner_bombas_tablero_oculto(k,bombas)
    poner_info_tablero_oculto(k)
    print('¡Buena suerte!')
    perder=False
    ganar=False
    while perder==False and ganar==False:
        imprimir_tablero(w)
        Opcion=menu_buscaminas()
        #Vemos las diferentes opciones para el usuario
        if Opcion==1:
            fila=int(input('Introduzca la fila de la casilla que quiera destapar: '))
            columna=int(input('Introduzca la columna de la casilla que quiera destapar: '))
            Jugada=tablero_visible_destapar(w,k,fila,columna)
            if Jugada==True:
                print('¡Acaba de destapar una bomba!')
                perder=True
            elif Jugada==None:
                print('Ha introducido algun dato incorrecto, vuelva a probar')
            else:
                print('Casilla ({0},{1}) destapada'.format(fila,columna))
        elif Opcion==2:
            fila=int(input('Introduzca la fila de la casilla que quiere marcar: '))
            columna=int(input('Introduzca la columna de la casilla que quiere marcar: '))
            Jugada=tablero_visible_marcar(w,fila,columna,True)
            if Jugada==+1:
                print('Casilla ({0},{1}) marcada'.format(fila,columna))
            else:
                print('La casilla ({0},{1}) ya ha sido marcada'.format(fila,columna))
        elif Opcion==3:
            fila=int(input('Introduzca la fila de la casilla que quiere marcar: '))
            columna=int(input('Introduzca la columna de la casilla que quiere marcar: '))
            Jugada=tablero_visible_marcar(w,fila,columna,False)
            if Jugada==-1:
                print('Casilla ({0},{1}) desmarcada'.format(fila,columna))
            else:
                print('La casilla ({0},{1}) no está marcada, no la puede desmarcar'.format(fila,columna))
        elif Opcion==4:
            Jugada=comprobar_tablero_visible(w,k,bombas)
            if Jugada==True:
                print('Ha marcado las {0} bombas con éxito'.format(bombas))
                ganar=True
            else:
                print('Aún le faltan bombas por marcar')
        else:
            perder=None

        #Vemos las diferentes respuestas cuando el jugador no ha ganado
        if perder==True:
            imprimir_tablero(w)
            print('Lo siento, ha perdido esta ronda')
        elif perder==None:
            print('Gracias por jugar, vuelva pronto')

        #Vemos la respuesta cuando el jugador ha ganado
        if ganar==True:
            imprimir_tablero(w)
            print('¡¡¡Felicidades, ha ganado!!!')

           
# –- Programa principal –-
# Ejecutar el test sólo al ejecutar el fichero (y no al importarlo)
if __name__ == "__main__":
    main()
