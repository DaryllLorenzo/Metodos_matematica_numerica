# optimizacion con restricciones

import math

def eval_funcion(x): # evaulamos la funcion para un valor de x
    #return pow(math.e, pow(x,4))
    #print( "el valor de la f(x) es ", math.sin(x))
    return pow(math.e , x) * math.cos(x)
    #return x * math.sin(x)
    #return pow(math.e , pow(x , 2))
    #return math.exp( pow (x , 2))

def eval_funcion_negativo(x): # multiplicar la funcion por -1 para la evaluacion de hallar el minimo
    #return pow(math.e, pow(x,4))
    #print( "el valor de la f(x) es ", math.sin(x))
    return -1 * (x * math.sin(x) )
    #return pow(math.e , pow(x , 2))
    #return math.exp( pow (x , 2))


def calcular_distancia_puntos_experimentales(tolerancia):
    return 0.1 * tolerancia

def valor_exacto_aprox_y_error(a, b):
    punto_medio = (a + b) / 2
    error = (b - a) / 2

    return punto_medio, error

def biseccion_minimo(a,b,dist_exp,tolerancia):
    n = 0
    print("")
    print("Biseccion para buscar el minimo")
    print("----------------------------------------------------------------")
    while True:
        x1 = (a + b) / 2 - dist_exp / 2
        x2 = (a + b) / 2 + dist_exp / 2

        y1 = eval_funcion_negativo(x1)
        y2 = eval_funcion_negativo(x2)

        #if y1 < y2:
        #    a = x1
        #    comparacion = f"f(x1): {y1} < f(x2): {y2}"
        #else:
        #    b = x2
        #    comparacion = f"f(x1): {y1} > f(x2): {y2}"

        #print("----------------------------------------------------------------")
        #print(f"Iteracion: {n} / a: {a} / b: {b} / x1: {x1} / x2: {x2} / ", comparacion)

        if y1 < y2:
            comparacion = f"f(x1): {y1} < f(x2): {y2}"
        else:
            comparacion = f"f(x1): {y1} > f(x2): {y2}"

        print(f"Iteracion: {n} / a: {a} / b: {b} / x1: {x1} / x2: {x2} / ", comparacion)

        if y1 < y2:
            a = x1
        else:
            b = x2


        L = b-a
        if L < tolerancia:
            n +=1
            print(f"Iteracion: {n} / a: {a} / b: {b}")
            break
        n+=1

    print(f"Con {n} iteraciones. El punto minimo de X aproximada se encuentra en [{a} , {b}]")

    punto_medio , error_cometido = valor_exacto_aprox_y_error(a,b)
    print("")
    print(f"El error cometido fue de {error_cometido} utilizando la tecnica del punto medio")
    print(f"El valor de la X aproximada es: {punto_medio} utilizando la tecnica del punto medio")
    print(f"El punto minimo es: [{punto_medio} , {eval_funcion(punto_medio)}]")

def biseccion(a,b, dist_exp , tolerancia):
    n = 0
    print("")
    print("Biseccion para buscar el maximo")
    print("----------------------------------------------------------------")
    while True:
        x1 = (a + b) / 2 - dist_exp / 2
        x2 = (a + b) / 2 + dist_exp / 2
        y1 = eval_funcion(x1)
        y2 = eval_funcion(x2)
        if y1 < y2:
            comparacion = f"f(x1): {y1} < f(x2): {y2}"
        else:
            comparacion = f"f(x1): {y1} > f(x2): {y2}"
        print(f"Iteracion: {n} / a: {a} / b: {b} / x1: {x1} / x2: {x2} / ", comparacion)
        if y1 < y2:
            a = x1
        else: 
            b = x2
        L = b - a
        if L < tolerancia:
            n +=1
            print(f"Iteracion: {n} / a: {a} / b: {b}")
            break
        n+=1
    print(f"Con {n} iteraciones. El punto maximo de X aproximada se encuentra en [{a} , {b}]")
    punto_medio , error_cometido = valor_exacto_aprox_y_error(a,b)
    print("")
    print(f"El error cometido fue de {error_cometido} utilizando la tecnica del punto medio")
    print(f"El valor de la X aproximada es: {punto_medio} utilizando la tecnica del punto medio")
    print(f"El punto maximo es: [{punto_medio} , {eval_funcion(punto_medio)}]")

def numero_de_experimentos(a,b,tolerancia):
    L0 = b - a
    resultado = L0 / tolerancia
    # y aplicando logaritmos
    n = 2 * (math.log(resultado) / math.log(2))

    print("")
    print("Numero de experimentos")
    print("----------------------------------------------------------------")
    print("Si n = 12.01 se aproxima a 14 si es 12 no se aproxima si es 13.56 se aproxima a 14")
    print("Y la cantidad de iteraciones se saca dividiendo el n ya aproximado / 2. Si son 14 experimentos serian 7 iteraciones")
    print(f"El resultado fue {n} FALTA APROXIMAR !")

#biseccion(2, 2.1 , calcular_distancia_puntos_experimentales(0.001) , 0.001)


biseccion(0.7 , 0.9 , calcular_distancia_puntos_experimentales(0.005) , 0.005)

#biseccion_minimo(4.85 , 4.95, calcular_distancia_puntos_experimentales(0.001) , 0.001)

#numero_de_experimentos(2,2.1,0.001)

#biseccion(1.9,2.5,calcular_distancia_puntos_experimentales(0.001),0.001)
#numero_de_experimentos(1.9,2.5,0.001)