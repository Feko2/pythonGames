tablero = []

def vaciarTabla():
    global tablero

    if len(tablero) == 9:
        tablero = []
    
    for i in range (9):
        tablero.append(" ")

def imprimirTabla():
    global tablero

    print (f" {tablero[0]} | {tablero[1]} | {tablero[2]}")
    print ("-----------")
    print (f" {tablero[3]} | {tablero[4]} | {tablero[5]}")
    print ("-----------")
    print (f" {tablero[6]} | {tablero[7]} | {tablero[8]}")

def posicion(signo, pos):
    global tablero

    if (tablero[pos-1] == " "):
        tablero[pos - 1] = signo
        return True

    else:
        print("Celda ya ocupada")
        return False


def ganador(signo):

    if tablero[0] == signo and tablero[1] == signo and tablero[2] == signo: #primera fila
        return True
    elif tablero[3] == signo and tablero[4] == signo and tablero[5] == signo: #segunda fila
        return True
    elif tablero[6] == signo and tablero[7] == signo and tablero[8] == signo: #tercera fila
        return True


    elif tablero[0] == signo and tablero[3] == signo and tablero[6] == signo: #primera columna
        return True
    elif tablero[1] == signo and tablero[4] == signo and tablero[7] == signo: #segunda columna
        return True
    elif tablero[2] == signo and tablero[5] == signo and tablero[8] == signo: #tercera columna
        return True


    elif tablero[0] == signo and tablero[4] == signo and tablero[8] == signo: #diagonal derecha a izquierda
        return True
    elif tablero[2] == signo and tablero[4] == signo and tablero[6] == signo: #diagonal izquierda a derecha
        return True
    else:
        return False

jugando = True

while jugando: #seguir jugando

    vaciarTabla()
    turno = 1
    jugadores = ['o', 'x']

    while True: #paritda actual

        imprimirTabla()
        jugador = jugadores[turno%2]
        pos = int(input(f"turno del jugador {jugador}, elije la casilla en la que quieras colocar tu signo: "))
        while True:
            if pos < 1 or pos > 9:
                pos = int(input("Valor fuera de rango, ingrese uno entre 1 - 9: "))

            if posicion(jugador, pos) == True:
                turno += 1
                break
            else:
                pos = int(input(f"turno del jugador {jugador}, la celda ya esta ocupada, escoje una libre: "))
            
        if ganador(jugador):
            imprimirTabla()
            print(f"Jugador {jugador} ganó la partida.")
            break

        if turno == 10:
            imprimirTabla()
            print("GATO")
            break
    
    respuesta = input("Si quieres seguir jugando presiona y, para cerrarlo teclea cualquier letra: ")

    if respuesta != "y":
        jugando = False




    



