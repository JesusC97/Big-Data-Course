'''Escribir un programa que calcule la Circunferencia de un círculo y 
muestre por pantalla el resultado. Si puedes con eso, hazlo para que también calcule el diámetro.
'''

'''
Autor: Jesus Cies Fernandez | jesusciefer1997@gmail.com
Fecha 29/09/20
Objetivo calcular circunferencia y diametro
'''

import math # Para importar pi pues va a ser una variable que necesito

print('Por favor, utiliza en las siguientes entradas el sistema internacional de medidas')
r=int(input('Por favor, dame el valor del radio del círculo en metros: r = '))
pi = math.pi # necesito definir pi como si de una variable se tratase

c=0 #out (en python hay que establecer la variable de salida)
a=0

# 5. Algoritmo
c=2*pi*r

a=pi*r**2
# 6. Resultado
print(f'El valor de la circunferencia es de {round(c,2)} metros')
print(f'El valor del area es de {round(a,2)} metros cuadrados')