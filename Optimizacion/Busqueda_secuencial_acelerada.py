# optimizacion sin restricciones
# llega mas rapidamente a la solucion pero da como resultado un intervalo final mayor

import math

#print(math.e) numero euler
#print(math.log(math.e)) logaritmo natural
# pow() elevar

def eval_funcion(x): # evaulamos la funcion para un valor de x
    #return pow(math.e, pow(x,4))
    #print( "el valor de la f(x) es ", math.sin(x))
    #return math.sin(x)
    #return x * math.sin(x)
    return pow(math.e , x) * math.cos(x)
    #return pow(math.e , pow(x , 2))
    #return math.exp( pow (x , 2))

def valor_exacto_aprox_y_error(a, b):
    punto_medio = (a + b) / 2
    error = (b - a) / 2

    return punto_medio, error

# X0 punto inicial de la busqueda
# s el paso 
def bsa(X0 , s):
    n = 0
    k = 0
    x = []
    x.append(X0)
    print(f"Iteracion: {n} / xi: {X0} / f(xi): {eval_funcion(X0)}")
    while True:
        Y0 = eval_funcion(X0)
        k = k + 1
        Xk = X0 + s
        Yk = eval_funcion(Xk)
        s = 2 * s
        X0 = Xk
        x.append(X0)
        if Yk < Y0:
            n += 1
            print(f"Iteracion: {n} / xi: {Xk} / f(xi): {Yk}")    
            break
        n += 1
        print(f"Iteracion: {n} / xi: {Xk} / f(xi): {Yk}")
    print(f"X aproximada se encuentra entre {x[k-2]} y {Xk}")
  
    punto_medio , error_cometido = valor_exacto_aprox_y_error(x[k-2],Xk)
    print(f"El error cometido fue de {error_cometido} utilizando la tecnica del punto medio")
    print(f"El valor de la X aproximada es: {punto_medio} utilizando la tecnica del punto medio")
    print(f"El punto maximo es: [{punto_medio} , {eval_funcion(punto_medio)}]")

#bsa(1.8,0.1)


bsa( 0.5 , 0.1)

