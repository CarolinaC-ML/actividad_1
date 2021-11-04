#aprendiendo condicionales
juanito=13
pepe=15
if juanito>pepe:
    print('juanito es mayor que pepe')
elif juanito<pepe:
    print('pepe es mayor que juanito')
else:
    print('pepe y juanito tienen la misma edad')

# bucle while
b = 0
while b <= 10:
    print(b)
    b = b+ 1

#bucle for
var1 = 'string'
for x,y in enumerate(var1):
    print(x,y)
numeros = [0,1,2,3,4,5]
for i in numeros:
    if i == 5:
        break
    else:
        print(i)

#funcion fibonacci
def fibonacci(numeros):
    a,b = 0,1
    resultado = []
    while b < numeros:
        resultado.append(b)
        a,b = b,a+b
    return resultado

print(fibonacci(7))




