# optimizacion con restricciones

import math

def eval_funcion(x): # evaulamos la funcion para un valor de x
    #return pow(math.e, pow(x,4))
    #print( "el valor de la f(x) es ", math.sin(x))
    return x * math.sin(x)
    #return pow(math.e , pow(x , 2))
    #return math.exp( pow (x , 2))

def eval_funcion_negativo(x): # multiplicar la funcion por -1 para la evaluacion de hallar el minimo
    #return pow(math.e, pow(x,4))
    #print( "el valor de la f(x) es ", math.sin(x))
    return -1 * (x * math.sin(x) )
    #return pow(math.e , pow(x , 2))
    #return math.exp( pow (x , 2))

def valor_exacto_aprox_y_error(a, b):
    punto_medio = (a + b) / 2
    error = (b - a) / 2

    return punto_medio, error

def seccion_oro_minimo(a,b,tolerancia):
    n = 0
    print("")
    print("Seccion de oro para buscar el minimo")
    print("----------------------------------------------------------------")
    L = b - a
    Factor = 0.381966
    x1 = a + Factor * L
    x2 = b - Factor * L
    y1 = eval_funcion_negativo(x1)
    y2 = eval_funcion_negativo(x2)

    while True:
        ## Nuevo
        if y1 < y2:
            comparacion = f"f(x1): {y1} < f(x2): {y2}"
        else:
            comparacion = f"f(x1): {y1} > f(x2): {y2}"

        print(f"Iteracion: {n} / a: {a} / b: {b} / x1: {x1} / x2: {x2} / ", comparacion)


        if y1 < y2:
            #comparacion = f"f(x1): {y1} < f(x2): {y2}"
            a = x1
            x1 = x2
            y1 = y2
            L = b - a
            x2 = b - Factor * L
            y2 = eval_funcion_negativo(x2)
        else:
            #comparacion = f"f(x1): {y1} > f(x2): {y2}"
            b = x2
            x2 = x1
            y2 = y1
            L = b - a
            x1 = a + Factor * L
            y1 = eval_funcion_negativo(x1)
        
        #print(f"Iteracion: {n} / a: {a} / b: {b} / x1: {x1} / x2: {x2} / ", comparacion)
        
        if L < tolerancia:
            n+=1
            print(f"Iteracion: {n} / a: {a} / b: {b}")
            break
        n+=1
    
    print(f"Con {n} iteraciones. El punto minimo de X aproximada se encuentra en [{a} , {b}]")

    punto_medio , error_cometido = valor_exacto_aprox_y_error(a,b)
    print("")
    print(f"El error cometido fue de {error_cometido} utilizando la tecnica del punto medio")
    print(f"El valor de la X aproximada es: {punto_medio} utilizando la tecnica del punto medio")
    print(f"El punto minimo es: [{punto_medio} , {eval_funcion(punto_medio)}]")

def seccion_oro(a,b,tolerancia):
    n = 0
    print("")
    print("Seccion de oro para buscar el maximo")
    print("----------------------------------------------------------------")
    L = b - a
    Factor = 0.381966
    x1 = a + Factor * L
    x2 = b - Factor * L
    y1 = eval_funcion(x1)
    y2 = eval_funcion(x2)

    while True:
        ## Nuevo
        if y1 < y2:
            comparacion = f"f(x1): {y1} < f(x2): {y2}"
        else:
            comparacion = f"f(x1): {y1} > f(x2): {y2}"

        print(f"Iteracion: {n} / a: {a} / b: {b} / x1: {x1} / x2: {x2} / ", comparacion)

        if y1 < y2:
            #comparacion = f"f(x1): {y1} < f(x2): {y2}"
            a = x1
            x1 = x2
            y1 = y2
            L = b - a
            x2 = b - Factor * L
            y2 = eval_funcion(x2)
        else:
            #comparacion = f"f(x1): {y1} > f(x2): {y2}"
            b = x2
            x2 = x1
            y2 = y1
            L = b - a
            x1 = a + Factor * L
            y1 = eval_funcion(x1)
        
        #print(f"Iteracion: {n} / a: {a} / b: {b} / x1: {x1} / x2: {x2} / ", comparacion)
        
        if L < tolerancia:
            n+=1
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
    resultado = tolerancia / L0
    # y aplicando logaritmos
    G = 0.618034
    n = math.log(resultado) / math.log(G) + 1

    print("")
    print("Numero de experimentos")
    print("----------------------------------------------------------------")
    print("Si n = 12.01 se aproxima a 13 si es 12 no se aproxima si es 13.56 se aproxima a 14")
    print("Y la cantidad de iteraciones se saca n ya aproximado - 1. Si son 14 experimentos serian 13 iteraciones")
    print(f"El resultado fue {n} FALTA APROXIMAR !")

seccion_oro(2,2.1, 0.001)

seccion_oro_minimo(4.85 , 4.95, 0.001)

numero_de_experimentos(2,2.1, 0.001)