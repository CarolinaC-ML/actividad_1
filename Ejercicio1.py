'''
Programa que pregunta: nombre, apellido, edad, dirección, fecha de nacimiento, teléfono y correo electrónico.
Además, debe sumar la edad + año de nacimiento
'''

name = input('¿Cuál es su nombre de pila?')
surname = input('¿y su apellido?')
age = int(input('¿Cuántos años tiene?'))
address = input('¿Cuál es su dirección?')
year = int(input('¿Qué año nació?'))
phone = input('¿Cuál es su teléfono?')
email = input('¿Cómo es su correo electrónico?')
yearNow = str(age+year)
print('Estamos en el año ' + yearNow + '. Hola, ' + name +' '+ surname + '. Veo que vive en ' + address + 
'. Le llamaremos al número ' + phone + ' o le escribiremos un correo a la dirección ' + email + '.')