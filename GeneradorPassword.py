import random

caracteres = "*!&$#?=@abcdefghijklnopqrstuvwxyz+-/ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
longitud = int(input('Ingresa la longitud de tu  contraseña: '))
contraseña = ""

for i in range(longitud):
    contraseña += random.choice(caracteres)

print("Tu contraseña nueva es:", contraseña )
