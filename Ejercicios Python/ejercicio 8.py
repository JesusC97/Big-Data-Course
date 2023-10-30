'''Imagina que estamos en el CERN y nos han pedido diseñar un programa en Python 
para calcular el Peso Molecular. Para ello, nos dicen que 
el calculo se realiza de la siguiente manera: «pesoMolecuar = peso1 * atomo1 + peso2 * atomo2.
'''

'''
Autor: Jesus Cies Fernandez | jesusciefer1997@gmail.com
Fecha 29/09/20
Objetivo calcular peso molecular
'''
print('Por favor, utiliza en las siguientes entradas el sistema internacional de medidas')
peso1=int(input('Por favor, dame el valor del peso atomico del primer atomo considerado en umas: '))
atomo1=int(input('Por favor, ahora dame la cantidad de atomos que hay de este tipo en la molecula: '))
peso2=int(input('Muchas gracias, ahora necesito que me des el peso atomico del segundo atomo considerado en umas: '))
atomo2=int(input('Muchas gracias, para finalizar necesito ahora que me des la cantidad de atomos que hay de este tipo en la molecula: '))
PM=0 #out (en python hay que establecer la variable de salida)
# 5. Algoritmo
PM=peso1*atomo1+peso2*atomo2
# 6. Resultado
print(f'El valor del peso molecular es de {PM} umas')