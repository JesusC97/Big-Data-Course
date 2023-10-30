''' Calcular los intereses que tendrás si inviertes 100.000€ (capitalInicial) a un 2% (interes) 
de interés en 10 años (ciclos) debido a la fórmula del interés compuesto. 
Pista: Tienes un montón de información al respecto en Internet. Localiza la fórmula.

Paso 2: Intenta hacer que pida todos los datos al usuario.'''
'''

Autor: Jesus Cies Fernandez | jesusciefer1997@gmail.com
Fecha 29/09/20
Objetivo calcular capital final
'''


c_0=float(input('Por favor, dame el valor del capital inicial en euros: '))
i=float(input('Por favor, dame el valor del interes en porcentaje: '))
n=float(input('Por favor, dame el valor del numero de años: '))
i=i/100

# 5. Algoritmo
c_n=c_0*(1+i)**n

# 6. Resultado
print(f'El valor del capital final es {round(c_n,2)} €')
