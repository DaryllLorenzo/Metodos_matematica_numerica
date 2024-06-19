# la 4ta columna son los terminos independientes

a = [
     [10, -1, 2,    6],
     [1, -5, 1,    -10],
     [2, -1, 8,      -8]
]

b = [
     [7, 10, 2],
     [2, -1, 8],
    [10, -5, 1]
]

c = [
     [7, 10, 20],
     [10, -5, 1],
     [2, 7, 3]
]

d = [
     [7, 10, 2,   10],
     [10, -5, 1,    8],
     [2, -1, 8,      9]
]

e = [
    [9, -1, 2, 9],
    [1, 8, 2, 19],
    [1, -1, 11, 10]
]


f = [
    [-1, 1, 5, 10],
    [5, -1, 1, 10],
    [2, -1, 1, 10]
]

def cambiarSegundaFila(matriz, fila):
    for i in range(4):
        swap = matriz[fila][i]
        matriz[fila][i] = matriz[1][i]
        matriz[1][i] = swap


def cambiarTerceraFila(matriz, fila):
    for i in range(4):
        swap = matriz[fila][i]
        matriz[fila][i] = matriz[2][i]
        matriz[2][i] = swap


def Despeje(matriz):
    for i in range(3):
        divisor = matriz[i][i]
        for j in range(4):
            if j != 3:
                matriz[i][j] = matriz[i][j] / divisor * -1
            else:
                matriz[i][j] = matriz[i][j] / divisor
    return matriz

def HallarBeta(matriz):
    P = [
        [0, 0, 0],
        [matriz[1][0], 0, 0],
        [matriz[2][0], matriz[2][1], 0]
    ]
    Q = [
        [0, matriz[0][1], matriz[0][2]],
        [0, 0, matriz[1][2]],
        [0, 0, 0]
    ]
    arreglosP = []
    arreglosQ = []

    for i in range(3):
        valorP = 0
        valorQ = 0
        for j in range(3):
            valorP += abs(P[i][j])
            valorQ += abs(Q[i][j])
        arreglosP.append(valorP)
        arreglosQ.append(valorQ)

    beta = []

    beta.append(arreglosQ[0] / (1-arreglosP[0]))
    beta.append(arreglosQ[1] / (1 - arreglosP[1]))
    beta.append(arreglosQ[2] / (1 - arreglosP[2]))

    beta.sort()
    return beta[2]

def calcularSolus(matriz, vector):
    Vresult = []
    vectMult = []
    copia = vector.copy()

    temp = [0,0,0]
    for i in range(3):
        valor = 0
        for j in range(3):
            temp[j] = matriz[i][j] * copia[j]
            #print("multiplicacion: ",matriz[i][j] * vector[j])
            #print("valor tempo suma: ",temp[j])
        for l in temp:
            valor += l
        vectMult.append(valor)

        Vresult.append(matriz[i][3] + vectMult[i])
        # asigno nueva X
        copia[i] = Vresult[i]

    return Vresult


def buscarMayorPositivo(soluciones:list, soluciones_ant:list):
    Arr = []
    for i in range(3):
        temp1 = abs(soluciones[i])
        temp2 = abs(soluciones_ant[i])
        Arr.append(abs(temp1 - temp2))
    Arr.sort()
    return Arr[2]

def Seidel(matriz, beta, Err):
    XV = [0, 0, 0]
    Error = 0
    print("Iteracion 0 :", XV)
    o = 1
    while True:
        soluciones = calcularSolus(matriz, XV)
        absS = buscarMayorPositivo(soluciones, XV)
        Error = absS * (beta / (1 - beta))
        print("Iteracion ", o, " Soluciones: ", soluciones, " Error: ", Error)
        if (Error < Err):
            print("La solucion del sistema es: ", soluciones, " con error absoluto menor que: ", Error)
            break

        XV = soluciones
        # for i in range(3):
        #    XV[i] = soluciones[i]
        o += 1

def comprobarDiagoPredominante(a):
    if abs(a[0][0]) < abs(a[0][1]) + abs(a[0][2]) :
        cambiarSegundaFila(a,0) #el segundo argumento fila a cambiar
        if abs(a[0][0]) < abs(a[0][1]) + abs(a[0][2]) :
            cambiarTerceraFila(a,0)
    if abs(a[1][1]) < abs(a[1][0]) + abs(a[1][2]) :
        cambiarTerceraFila(a,1)
    if abs(a[2][2]) < abs(a[2][0]) + abs(a[2][1]):
        print("Algo mal")
        return False , None

    if abs(a[0][0]) < abs(a[0][1]) + abs(a[0][2]):
        return False, None
    if abs(a[1][1]) < abs(a[1][0]) + abs(a[1][2]):
        return False, None
    if abs(a[2][2]) < abs(a[2][0]) + abs(a[2][1]):
        return False, None

    #print(a)
    for i in range(3):
        for j in range(4):
            print(a[i][j], end="     ")
        print("")
    print("Tiene diago predominante")
    return True, a


TieneDiago,matriz = comprobarDiagoPredominante(e)
if TieneDiago is True:
    matriz = Despeje(matriz)
    letras = ("X", "Y", "Z")

    # print la x
    print(letras[0], "= ", end="")
    for j in range(1, 4):
        print(matriz[0][j], end="     ")
    print("")

    #  print la y
    print(letras[1], "= ", end="")
    print(matriz[1][0], end="     ")
    print(matriz[1][2], end="     ")
    print(matriz[1][3], end="     ")
    print("")

    #  print la z
    print(letras[2], "= ", end="")
    print(matriz[2][0], end="     ")
    print(matriz[2][1], end="     ")
    print(matriz[2][3], end="     ")
    print("")

    print("")
    print("Nueva matriz:")

NuevaMatriz = [[0, matriz[0][1], matriz[0][2] , matriz[0][3] ],
               [matriz[1][0], 0, matriz[1][2] , matriz[1][3]],
               [matriz[2][0], matriz[2][1], 0 , matriz[2][3]]
]

for i in range(3):
        for j in range(4):
            print(NuevaMatriz[i][j], end="     ")
        print("")

beta = HallarBeta(NuevaMatriz)
Seidel(NuevaMatriz, beta, 0.00005)
## LLAMAR A Seidel