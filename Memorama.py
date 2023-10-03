import random

cartas = []
estado = []
ls = [True]

def creaTablero():
    global cartas
    temp = []
    for x in range(1, 7):
        temp.append(x)
        temp.append(x)

    random.shuffle(temp)

    for filas in range(3):
        cartas.append([])
        for columnas in range(4):
            cartas[filas].append(temp.pop(0))
        
    for i in range(3):
        estado.append([])
        for j in range(4):
            estado[i].append(True)

def imprimeTablero():
    """
    Imprime el tablero
    █
    """
    global cartas, estado
    tablero = []
    
    for fila in range(len(estado)):
        tablero.append([])
        for columna in range(4):
            if estado[fila][columna] == True: #Si la carta ya etsá volteada
                tablero[fila].append("█")
            else:
                tablero[fila].append(cartas[fila][columna])

    print("    1   2   3   4")

    print(f" 1  {tablero[0][0]}   {tablero[0][1]}   {tablero[0][2]}   {tablero[0][3]}")
    print(f" 2  {tablero[1][0]}   {tablero[1][1]}   {tablero[1][2]}   {tablero[1][3]}")
    print(f" 3  {tablero[2][0]}   {tablero[2][1]}   {tablero[2][2]}   {tablero[2][3]}")


def checarPares(x1, y1, x2, y2):
    global cartas, estado
    if cartas[x1][y1] == cartas[x2][y2]: # sí son iguales los valores de las cartas
        print("\n Muy bien!")
    else: # en caso de que no sean iguales, se vuelven a voltear
        imprimeTablero()
        print("No fue par, intentalo otra vez!")
        estado[x1][y1] = True
        estado[x2][y2] = True

def checarEstado(x, y):
    """
    Checar si las filas estan ocultas o no.
    x -> filas
    y -> columnas
    """
    if estado [x][y] == False:  #Si ya esta descubierta
        print("la carta ya esta descubierta")
        return False
    else:
        estado[x][y] = False #se descubre la carta
        return True
    

jugando = True
ronda = True

while jugando:
    creaTablero()
    print("    Memorama    ")

    while ronda:
        imprimeTablero()
        pos = input("Ingresa la coordenada de la primera carta (utiliza espacios): ") #"2 1"
        coordenadas = pos.split()
        x1, y1 = int(coordenadas[0]) - 1, int(coordenadas[1]) - 1
        while True:
            if checarEstado(x1, y1):
                imprimeTablero()
                break
            else:
                pos = input("Ingresa la coordenada de la primera carta (utiliza espacios): ") #"2 1"
                coordenadas = pos.split()
                x1, y1 = int(coordenadas[0]) - 1, int(coordenadas[1]) - 1
        pos = input("Ingresa la coordenada de la segunda carta (utiliza espacios): ") 
        coordenadas = pos.split()
        x2, y2 = int(coordenadas[0]) - 1, int(coordenadas[1]) - 1
        while True:
            if checarEstado(x2, y2):
                break
            else:
                pos = input("Ingresa la coordenada de la primera carta (utiliza espacios): ") #"2 1"
                coordenadas = pos.split()
                x2, y2 = int(coordenadas[0]) - 1, int(coordenadas[1]) - 1
        checarPares(x1, y1, x2, y2)
