import math

#print(math.e) numero euler
#print(math.log(math.e)) logaritmo natural
# pow() elevar
array = [3.35 , 5.5 , 7 , 4.7 , 6.55 , 4.4 , 6.25 , 4.1]
def eval_funcion(x): # evaulamos la funcion para un valor de x
    #return pow(math.e, pow(x,4))
    #print( "el valor de la f(x) es ", math.sin(x))
    return math.sin(x)
    #return pow(math.e , pow(x , 2))
    #return math.exp( pow (x , 2))

def paso(n, a, b):
    resultado = (b - a)/n
    return resultado

def obtener_aproximacion(n,a,b,h):
    E = eval_funcion(a) + eval_funcion(b)
    I = 0
    i = 1
    x = a + i * h
    I = I + eval_funcion(x)
    i = i + 2
    while i < n:
        x = a + i * h
        I = I + eval_funcion(x)
        i = i + 2
    P = 0
    i = 2
    x = a + i * h
    P = P + eval_funcion(x)
    i = i + 2
    while i < n:
        x = a + i * h
        P = P + eval_funcion(x)
        i = i + 2
    Integral = h/3 * (E + 4 * I + 2 * P)
    return Integral

def obtener_arreglo_x(n,a,b,h):
    E = eval_funcion(a) + eval_funcion(b)
    I = 0
    i = 1
    arreglo_x = []
    arreglo_x.append(a)
    x = a + i * h
    arreglo_x.append(x)
    I = I + eval_funcion(x)
    i = i + 2
    while i < n:
        x = a + i * h
        arreglo_x.append(x)
        I = I + eval_funcion(x)
        i = i + 2
    P = 0
    i = 2
    x = a + i * h
    arreglo_x.append(x)
    P = P + eval_funcion(x)
    i = i + 2
    while i < n:
        x = a + i * h
        arreglo_x.append(x)
        P = P + eval_funcion(x)
        i = i + 2
    Integral = h/3 * (E + 4 * I + 2 * P)
    arreglo_x.append(b)
    return arreglo_x

def obtener_C(arreglo):
    dic = {}
    for a in arreglo:
        dic[a] = abs(eval_funcion(a))

    clave_maxima = max(dic, key=dic.get)

    return clave_maxima

def cuarta_derivada_funcion(x):
    return math.sin(x)


def error_por_truncamiento_cuarta_derivada(n,a,b,h,c):
    cota = -1 * (b-a)/180 * pow(h,4) * cuarta_derivada_funcion(c)
    print("-----------------------")
    if cota > 0:
        print(f"la cota de error valida es 0 <= R <= {cota}")
    if cota < 0:
        print(f"la cota de error valida es {cota} <= R <= 0")



def error_doble_calculo_truncamiento(n, a, b):
    resultado = (obtener_aproximacion(n,a,b,paso(n,a,b)) - obtener_aproximacion(n//2,a,b, paso(n/2,a,b))) / 15
    return resultado 

def error_doble_calculo_x_cifras_decimales_exactas(n,a,b, cifras):
    elevacion = pow(10, cifras)
    cap = 1 / elevacion
    capeo = cap / 2    
    
    error = abs(error_doble_calculo_truncamiento(n, a , b))
    while error > capeo:
        n = n * 2
        error = abs(error_doble_calculo_truncamiento(n , a, b) )
    print(f"La aproximacion fue:{obtener_aproximacion(n,a,b, paso(n,a,b))}")
    print(f"El numero de intervalos fue:{n}")
    print(f"El error estimado fue:{error}")


#print(obtener_aproximacion(40, 0 , math.pi, paso(40 , 0 , math.pi)))

#print(error_doble_calculo_truncamiento(40,0,math.pi))
#error_doble_calculo_x_cifras_decimales_exactas(10,1,2,4)

#arreglo = obtener_arreglo_x(10 , 0 , math.pi , paso(10,0,math.pi))
#C = obtener_C(arreglo)

#error_por_truncamiento_cuarta_derivada(10,0,math.pi,paso(10,0,math.pi),C)