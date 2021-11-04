'''
Programa que pregunta: nombre, apellido, edad, dirección, fecha de nacimiento, teléfono y correo electrónico.
Además, debe sumar la edad + año de nacimiento
'''
name = input('¿Cuál es su nombre de pila?')
surname = input('¿y su apellido?')
age = int(input('¿Cuántos años tiene?'))
address = input('¿Cuál es su dirección?')
print('Introduzca su fecha de nacimiento con el formato siguiente: día/mes/año')
date_entry = input()
day, month, year = map(int, date_entry.split('/'))
phone = input('¿Cuál es su teléfono?')
email = input('¿Cómo es su correo electrónico?')
yearNow = str(age+year)
print('Si ya ha sido mi cumple, estamos en el año ' + yearNow + 'Si no, un año más. Hola, me llamo ' + name +' '+ surname + '. vivo en '
 + address + '. Nací el ' + date_entry + '. Llámenme al número ' + phone + ' o escríbame a la dirección ' + email + '.')


