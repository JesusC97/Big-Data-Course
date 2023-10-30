'''Desarrollar un programa que calcula el voltaje que cae 
en una resistencia cuando los valores de la intensidad y la resistencia son conocidos.
La Ley de Ohm nos indica que voltaje = intensidad * resistencia
Ejemplo: Para un valor de la intensidad igual a 3 amperios y un 
valor de la resistencia de 4 ohmios el valor del voltaje es de 12 voltios.
'''

'''
Autor: Jesus Cies Fernandez | jesusciefer1997@gmail.com
Fecha 29/09/20
Objetivo calcular voltaje
'''

I=int(input('Por favor, dame el valor de la intensidad eléctrica en amperios I: '))
R=int(input('Muchas gracias, ahora necesito que me des el valor de la resistencia electrica en ohmios R: '))
V=0 #out (en python hay que establecer la variable de salida)
# 5. Algoritmo
V=I*R
# 6. Resultado
print(f'El valor del voltaje es {V} voltios')