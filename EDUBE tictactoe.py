#Tic-Tac-Toe
from random import randrange

def DisplayBoard(board):
    # La función acepta un parámetro el cual contiene el estado actual del tablero
    # y lo muestra en la consola.
    for row in board:
        print(row)

def EnterMove(board):
    # La función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento, 
    # verifica la entrada y actualiza el tablero acorde a la decisión del usuario.

    move_done = False

    while not move_done:
        mov = int(input("\nTe toca, indica posición donde colocar tu ficha: "))
        
        if mov < 1 or mov > 9:
            print('\nPosición no válida. Prueba otra vez')
            continue # Volver a pedir entrada

        # Obtener coordenadas de posición
        i = (mov - 1) // 3 # calcula la columna con la división entera
        j = (mov - 1) % 3 # cálculo de la posición de fila con el resto
            
        if board[i][j] == 'X' or board[i][j] == 'O':
            print('\nPosición ya ocupada. Prueba otra vez')
        else:
            board[i][j] = 'O'
            move_done = True

    return board    
    
def MakeListOfFreeFields(board):
    # La función examina el tablero y construye una lista de todos los cuadros vacíos.
    # La lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna.
    huecos_vacios = []

    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X' or board[i][j] == 'O':
                continue
            else:
                huecos_vacios.append((i, j))
    
    return huecos_vacios
    

def VictoryFor(board):
    # La función analiza el estatus del tablero para verificar si
    # el jugador que utiliza las 'O's o las 'X's ha ganado el juego.
    # Existen cuatro posibles veredictos:
    # el juego continua, el juego termina en empate, tu ganas, o la maquina gana.
    # pide entregar (board, sign) pero ignoro a qué se refiere con sign

    linea = False
    complete_board = True

    for row in board: # verifica filas
        if row[0] == row[1] == row[2] and row[0] in ['X', 'O']:
            linea = True
            if row[0] == 'X':
                print('\n¡He ganado! Ja, ja, ja')
            else:
                print('\n¡Maldita sea! Has ganado')
            return 'win'

    for j in range(3): # verifica columnas
        if board[0][j] == board[1][j] == board[2][j] and board[0][j] in ['X', 'O']:
            linea = True
            if board[0][j] == 'X':
                print('\n¡He ganado! Ja, ja, ja')
            else:
                print('\n¡Maldita sea! Has ganado')
            return 'win'

    # verifica diagonales
    if (board[0][0] == board[1][1] == board[2][2] in ['X', 'O']) or (board[0][2] == board[1][1] == board[2][0] in ['X', 'O']):
        linea = True
        if board[0][0] == 'X':
            print('\n¡He ganado! Ja, ja, ja')
        else:
            print('\n¡Maldita sea! Has ganado')
        return 'win'

   # comprobar si se puede hacer más movimientos
    for i in range(3):
        for j in range(3):
            if board[i][j] != 'X' and board[i][j] != 'O': # Si no es 'X' ni 'O', hay hueco vacío
                  complete_board = False
                  break
    
    if not linea:
        if complete_board:
            print('\nParece que hemos empatado')
        else:
            print('\nContinua el juego')

def DrawMove(board):
    # La función dibuja el movimiento de la máquina y actualiza el tablero.
    machine_mov = randrange(9)
    move_done = False
    i = (machine_mov - 1) // 3 # calcula la columna con la división entera
    j = (machine_mov - 1) % 3 # cálculo de la posición de fila con el resto

    move_done = False

    while not move_done:
        if board[i][j] == 'X' or board[i][j] == 'O':
            machine_mov = randrange(9)
            i = (machine_mov - 1) // 3
            j = (machine_mov - 1) % 3
            
        else:
            board[i][j] = 'X'
            move_done = True

    return board

# Creamos el tablero de 3x3 y numerado

#Usando bucles anidados
'''
board = []
num = 1
for i in range(3):
    row = []
    for j in range(3):
        row.append(num)
        num += 1
    board.append(row)
'''
# Usando comprensión de listas
board = [[i*3 + j + 1 for j in range(3)] for i in range(3)]

# Controlamos fin del juego con huecos vacíos
# huecos_vacios = MakeListOfFreeFields(board)

# Iniciamos juego
print("Tic-Tac-Toe\n")
DisplayBoard(board)
print("\nVamos a jugar al 3 en raya. Empiezo yo\n")

board[1][1] = 'X' # Máquina hace el primer movimiento

DisplayBoard(board)

game_over = False # controlar el fin del juego

while not game_over and MakeListOfFreeFields(board) != []: # continua juego
    # turno del jugador
    EnterMove(board)
    DisplayBoard(board)
    if VictoryFor(board) == "win":
        game_over = True
        break
    # Turno de la máquina
    if not game_over and MakeListOfFreeFields(board) != []:
        DrawMove(board)
        DisplayBoard(board)
        if VictoryFor(board) == "win":
            game_over = True  
    
else:
    print('\nFin del juego')


'''
players_data = [
    {"name": "Patrick Mahomes", "position": "Quarterback", "jersey_number": 15, "yards_gained": 400, "touchdowns": 3},
    {"name": "Tyreek Hill", "position": "Wide Receiver", "jersey_number": 10, "yards_gained": 150, "touchdowns": 2},
    # Add more players as needed
]
names = [player["name"] for player in players_data]
print("Players Names:", names)

# Task 2: Analyze Player Positions
positions = [player["position"] for player in players_data]
print("Player Positions:", positions)
'''
