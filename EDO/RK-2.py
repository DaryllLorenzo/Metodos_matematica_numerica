# el algoritmo obtiene la solucion aproximada del problema de cauchy
#dy/dx = f(x,y)
#y(x0) = y0

# en un intervalo x0 <= x <= xf con paso h > 0.
# Son conocidas la funcion f(x,y), condiciones iniciales (x0,y0) el valor final xf y el paso h

import math

#print(math.e) numero euler
#print(math.log(math.e)) logaritmo natural
# pow() elevar

def eval_funcion_problema(x , y): # evaulamos la funcion para un valor de x
    #return pow(math.e, pow(x,4))
    #print( "el valor de la f(x) es ", math.sin(x))
    #return math.sin(x)
    #return pow(math.e , pow(x , 2))
    #return 1/2 * y
    #return x- y
    #return (x - pow(y,2)) / (y + 3 * x)
    return -1 * 2 * x * y
    #return math.exp( pow (x , 2))s

def evaluar_sol_exacta(x):
    return 1/2 * pow(math.e , x / 2)

# h = (xf - x0) / N Siendo N cantdidad de subintervalos
def calcular_paso(x0,xf,n):
    return (xf - x0) / n

def rk2(x0,y0,xf,h):
    n = 0

    K1 = h * eval_funcion_problema(x0,y0)
    K2 = h * eval_funcion_problema(x0 + h , y0 + K1)

    Ysgt = y0 + 1/2 * (K1 + K2)
    Xsgt = x0 + h

    print(f"Cantidad de pasos n: {n} / Xn: {x0} / Yn: {y0} / f(Xn, Yn): {eval_funcion_problema(x0, y0)} / f(Xn + h,Yn + k1): {eval_funcion_problema(x0 + h, y0 + K1)}/ K1: {K1} / K2: {K2} / Xn+1: {x0 + h} / Yn+1: {y0 + (K1 + K2) / 2}")
    n = n + 1
    #x0 = Xsgt
    #y0 = Ysgt

    while x0 < xf:
        x0 = Xsgt
        y0 = Ysgt
        K1 = h * eval_funcion_problema(x0, y0)
        K2 = h * eval_funcion_problema(x0 + h, y0 + K1)

        Ysgt = y0 + 1 / 2 * (K1 + K2)
        Xsgt = x0 + h
        print(f"Cantidad de pasos n: {n} / Xn: {x0} / Yn: {y0} / f(Xn, Yn): {eval_funcion_problema(x0, y0)} / f(Xn + h,Yn + k1): {eval_funcion_problema(x0 + h, y0 + K1)}/ K1: {K1} / K2: {K2} / Xn+1: {x0 + h} / Yn+1: {y0 + (K1 + K2) / 2}")
        n = n + 1
        #x0 = Xsgt
        #y0 = Ysgt
    return y0

#recursivo por si acaso
"""""
def rk2(x0,y0,xf,h,iterN):
    K1 = h * eval_funcion_problema(x0, y0)
    K2 = h * eval_funcion_problema(x0 + h, y0 + K1)

    Ysgt = y0 + 1 / 2 * (K1 + K2)
    Xsgt = x0 + h

    print(f"n: {iterN} / Xn: {x0} / Yn: {y0} / f(Xn, Yn): {eval_funcion_problema(x0, y0)} / Xn+1: {x0 + h} / Yn+1: {y0 + h * eval_funcion_problema(x0, y0)}")
    iterN = iterN + 1

    if x0 < xf:
        rk2(Xsgt, Ysgt, xf, h, iterN)
"""""

# el error por doble calculo en un punto en especifico
def error_doble_calculo(x0,y0,xf,h):
    print("")
    error = ( rk2(x0,y0,xf,h) - rk2(x0,y0,xf,h * 2) ) / 3
    # el yn del segundo menos el del primero da el error en cada iteracion

    print("-------------------------------------------")
    print(f"El Error con x = {xf} de y{xf} es {error}")
    return error

# metodo auxiliar para def error_doble_calculo_intervalo
def rk2_error_iteracion(x0,y0,xf,h):
    y = []
    n = 0

    K1 = h * eval_funcion_problema(x0, y0)
    K2 = h * eval_funcion_problema(x0 + h, y0 + K1)

    Xsgt = x0 + h
    Ysgt = y0 + 1/2 * (K1 + K2)
    # como el libro
    # print(f"n: {n} / Xn: {x0} / Yn: {y0} / Y(Xn): {evaluar_sol_exacta(x0)} / error(Yn): {evaluar_sol_exacta(x0) - y0}")

    y.append(y0)
    # como la tabla de la profe
    print(f"Cantidad de pasos n: {n} / Xn: {x0} / Yn: {y0} / f(Xn, Yn): {eval_funcion_problema(x0, y0)} / f(Xn + h,Yn + k1): {eval_funcion_problema(x0 + h, y0 + K1)}/ K1: {K1} / K2: {K2} / Xn+1: {x0 + h} / Yn+1: {y0 + (K1 + K2) / 2}")
    n = n + 1
    # fuera del libro
    while x0 < xf:
        x0 = Xsgt
        y0 = Ysgt

        K1 = h * eval_funcion_problema(x0, y0)
        K2 = h * eval_funcion_problema(x0 + h, y0 + K1)

        Xsgt = x0 + h
        Ysgt = y0 + 1/2 * (K1 + K2)
        # como el libro
        # print(f"n: {n} / Xn: {x0} / Yn: {y0} / Y(Xn): {evaluar_sol_exacta(x0)} / error(Yn): {evaluar_sol_exacta(x0) - y0}")
        y.append(y0)
        # como la tabla de la profe
        print(f"Cantidad de pasos n: {n} / Xn: {x0} / Yn: {y0} / f(Xn, Yn): {eval_funcion_problema(x0, y0)} / f(Xn + h,Yn + k1): {eval_funcion_problema(x0 + h, y0 + K1)}/ K1: {K1} / K2: {K2} / Xn+1: {x0 + h} / Yn+1: {y0 + (K1 + K2) / 2}")
        n = n + 1
        # fuera del libro
        # x0 = Xsgt
        # y0 = Ysgt
    return y

# metodo para obtener el error punto (Error de toda la solucion el mayor de todos los errores del intervalo)
def error_doble_calculo_intervalo(x0,y0,xf,h):
    print("")

    yh = rk2_error_iteracion(x0,y0,xf,h)
    y2h = rk2_error_iteracion(x0,y0,xf,h * 2)
    arr_err = []
    dic = {}

    n = 0
    tam = len(yh)
    i = 0
    print("---------------------------------------------")
    while n != tam:
        if n % 2 == 0:
           print(f"Error de n = {n} es: {( yh[n] - y2h[i] ) / 3}")
           dic[(n,i)] = ( yh[n] - y2h[i] ) / 3
           arr_err.append(( yh[n] - y2h[i] ) / 3)
           i += 1

        n += 1
    copia = []
    for e in arr_err:
        elemento = abs(e)
        copia.append(elemento)
    copia.sort()
    ultimo = copia[len(copia) - 1]

    for clave in dic.keys():
        if abs(dic.get(clave)) == ultimo:
            print(f"El error punto, error de toda la solucion(mayor yi: y{clave[0]} con paso h:{h} y yi: y{clave[1]} con paso h:{2*h}) del intervalo es {ultimo} con nh = {clave[0]} y n2h = {clave[1]}")

def error_hasta_x_cifras_decimales_exactas(x0,y0,xf,h,cifras):
    elevacion = pow(10, cifras)
    cap = 1 / elevacion
    capeo = cap / 2

    error = abs(error_doble_calculo(x0,y0,xf,h))

    while error > capeo:
        h = h/2
        error = abs(error_doble_calculo(x0, y0, xf, h))
        print("------El error es: ",error,"------")


#recursivo por si acaso
#rk2(0,0.5,4,0.4, 0)
#rk2(0,1,2,1)
#error_doble_calculo(0,1,2,0.5)
error_doble_calculo_intervalo(0,1,2,0.5)
#rk2(0,4,4,1.0)
#error_doble_calculo(0,4,2,1.0)
#error_doble_calculo_intervalo(1,3,5,0.05)
#error_hasta_x_cifras_decimales_exactas(1,3,5,0.1,3)