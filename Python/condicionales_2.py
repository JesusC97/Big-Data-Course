'''Imaginemos que en nuestra tienda hay un carné por puntos y que alguien debe pagar el precio_final_de_compra. 
Si tienes menos de 100 puntos realizaremos un descuento del 10%. 
Si es mayor a 100 y menor a 150 aplicamos un 12%. 
Si tienes 150 un 15% y sino, el resto de los casos de más de 150, un 20%. ¡Crea la variable puntos y juega con ella!'''

# Definicion de las variables
puntos=int(input('Dime los puntos que tienes '))
precio=int(input('¿Cuanto es el precio de la cesta? Respuesta: '))
desc=0
precio_final_de_compra=precio*(1-desc)


if 100<puntos<150:
    desc=0.12
elif puntos==150:
    desc=0.15
elif puntos>150:
    desc=0.20
else:
    desc=0

print(f'El precio final de compra es {precio_final_de_compra} €')
