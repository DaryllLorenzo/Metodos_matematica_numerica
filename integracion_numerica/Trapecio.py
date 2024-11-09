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

# n numero de intervalos
# h el paso
# a punto inicial del intervalo
# b punto final del intervalo

def obtener_aproximacion(n, a, b, h):
    # a medida de que el paso h se reduce a la mitad el error se reduce aprox a la 
    # cuarta parte 
    #suma = (eval_funcion(a) + eval_funcion(b)) / 2
    arreglo_x = []
    i = 0
    suma = 0
    for i in range(n + 1):
        if i == 0:
            suma += eval_funcion(a) / 2
            print( f"el valor de x{i} : " , a)
            arreglo_x.append(a)
        elif i == n:
            suma += eval_funcion(b) / 2
            print( f"el valor de x{i} : " , b)
            arreglo_x.append(b)
        else:
            x = a + i * h
            print( f"el valor de x{i} : " , x)
            suma += eval_funcion(x)
            arreglo_x.append(x)
    resultado = suma * h
    return resultado

def obtener_aproximacion2(n, a, b, h):
    # a medida de que el paso h se reduce a la mitad el error se reduce aprox a la 
    # cuarta parte 
    #suma = (eval_funcion(a) + eval_funcion(b)) / 2
    arreglo_x = []
    i = 0
    o = 0
    suma = 0
    for i in range(n + 1):
        if i == 0:
            #suma += eval_funcion(a) / 2
            suma += array[o]
            o += 1
            print( f"el valor de x{i} : " , a)
            arreglo_x.append(a)
        elif i == n:
            #suma += eval_funcion(b) / 2
            suma += array[o - 1]
            o +=1
            print( f"el valor de x{i} : " , b)
            arreglo_x.append(b)
        else:
            x = a + i * h
            print( f"el valor de x{i} : " , x)
            #suma += eval_funcion(x)
            suma = array[o]
            o+=1 
            arreglo_x.append(x)
            
    resultado = suma * h
    return resultado



def obtener_arreglo_x(n, a, b, h):
    # a medida de que el paso h se reduce a la mitad el error se reduce aprox a la
    # cuarta parte
    #suma = (eval_funcion(a) + eval_funcion(b)) / 2
    arreglo_x = []
    i = 0
    suma = 0
    for i in range(n + 1):
        if i == 0:
            suma += eval_funcion(a) / 2
            print( f"el valor de x{i} : " , a)
            arreglo_x.append(a)
        elif i == n:
            suma += eval_funcion(b) / 2
            print( f"el valor de x{i} : " , b)
            arreglo_x.append(b)
        else:
            x = a + i * h
            print( f"el valor de x{i} : " , x)
            suma += eval_funcion(x)
            arreglo_x.append(x)
    resultado = suma * h
    return arreglo_x


def error_doble_calculo_truncamiento(n, a, b):
    resultado = (obtener_aproximacion(n,a,b,paso(n,a,b)) - obtener_aproximacion(n//2,a,b, paso(n/2,a,b))) / 3
    return resultado 

def error_doble_calculo_truncamiento2(n, a, b):
    resultado = (obtener_aproximacion2(n,a,b,paso(n,a,b)) - obtener_aproximacion2(n//2,a,b, paso(n/2,a,b))) / 3
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


def error_doble_calculo_menor_que_un_error(n, a, b, errorCapeo):
    error = abs(error_doble_calculo_truncamiento(n, a, b))
    while error > errorCapeo:
        n = n * 2
        error = abs(error_doble_calculo_truncamiento(n, a, b))
    print(f"La aproximacion fue:{obtener_aproximacion(n, a, b, paso(n, a, b))}")
    print(f"El numero de intervalos fue:{n}")
    print(f"El error estimado fue:{error}")

def obtener_C(arreglo):
    dic = {}
    for a in arreglo:
        dic[a] = abs(eval_funcion(a))

    clave_maxima = max(dic, key=dic.get)

    return clave_maxima

def segunda_derivada_funcion(x):
    return -math.sin(x)


def error_por_truncamiento_doble_derivada(n,a,b,h,c):
    cota = -1 * (b-a)/12 * pow(h,2) * segunda_derivada_funcion(c)
    print("-----------------------")
    if cota > 0:
        print(f"la cota de error valida es 0 <= R <= {cota}")
    if cota < 0:
        print(f"la cota de error valida es {cota} <= R <= 0")


#print(obtener_aproximacion(10, 1, 2, paso(10, 1, 2)))
#print(obtener_aproximacion(10, 0, math.pi, paso(10, 0, math.pi)))
#print(error_doble_calculo_truncamiento(20,0,math.pi))
#print(error_doble_calculo_truncamiento(40,0,math.pi))
#error_doble_calculo_x_cifras_decimales_exactas(10,1,2,4)
#error_doble_calculo_menor_que_un_error(10,1,2,0.00001)

#arreglo = obtener_arreglo_x(10,0,math.pi,paso(10,0,math.pi))

#c = obtener_C(arreglo)
#error_por_truncamiento_doble_derivada(10,0,math.pi,paso(10,0,math.pi), c)

print(obtener_aproximacion2(8 , 0 , 60 , paso(8 , 0 , 60)) )

print("El error es: " ,error_doble_calculo_truncamiento2(8 , 0 , 60 ) )