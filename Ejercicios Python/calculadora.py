
'''
Autor: Jesus Cies Fernandez | jesusciefer1997@gmail.com
Fecha 29/09/20
Objetivo: Hacer una calculadora
'''
# Le pido al usuario que me de los valores de entrada
a=float(input('Por favor, dame el valor de a: '))
b=float(input('Muchas gracias, ahora necesito que me des el valor de b: '))
op=int(input('Muchas gracias, ahora necesito que me definas la operacion que quieras hacer (1:+, 2:*, 3:-, 4:/): '))

if op<=0 or op>4:
    print('Lo siento, pero necesito que me elijas dentro de esas operaciones que te he comentado') # si me da un valor erroneo se lo comento al usuario

if op==1:
    print(f'El resultado es {a+b}')
elif op==2:
    print(f'El resultado es {a*b}')
elif op==3:
    print(f'El resultado es {a-b}')
elif op==4: # la operacion division puede ser problematica, establezco diferentes posibilidades para que sea mas facil de entender
    if b==0 and a>0:
        print('El resultado es +inf')
        
    elif b==0 and a<0:
        print('El resultado es -inf')
        
    elif b==0 and a==0:
        print('Es una indeterminación')
    else:
        print(f'El resultado es {a/b}')
