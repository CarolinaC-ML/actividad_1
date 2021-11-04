'''
hacer función solicitando datos personales
definir dos variables numericas, que sean parámetros de entrada que realice las 4 operaciones aritméticas mediante condicionales.
haciendo uso de <>!= ==
retornar e invocar dos funciones
'''
#Recabar e imprimir datos
variables = ['name', 'surname', 'age', 'address', 'date of birth (DD/MM/YYYY)', 'email', 'phone number'] 
resultados = [] 
def datos():
    for i in variables:
        resultados.append(input(f'What is your {i}?\n'))
    print(f'\nYour info:\n')
    for i in range(len(variables)):
        print(f'Your {variables[i]} is {resultados[i]}')
    return resultados
datos()
#función con parámetros numéricos
#fecha usuario
myDay, myMonth, myYear = map(int, resultados[4].split('/'))
age = int(resultados[2])
#fecha real
from datetime import date
today = str(date.today())
year, month, day = map(int, today.split('-'))
#fecha comprobada aplicando las 4 diferentes operaciones condicionales (< > == !=)
currentYear = 0
def calculo(a,b):
    if month > myMonth:
        currentYear = b + age
    elif month < myMonth:
        currentYear = b + age + 1
    else:
        if day >= myDay:
            currentYear = b + age
        elif day < myDay:
            currentYear = b + age + 1
    #imprimiendo resultados
    if currentYear == a:
        print(f'\nPerfect, the dates make sense. The current year is {a}')
    elif currentYear != a:
        print(f'\nWe might have traveled accross time. The date or the age does not make sense. Do you think we are in {currentYear}?\n')
calculo(year,myYear)





#función calculo optimizada:
'''
myData = [myDay, myMonth]
Data = [month, day]

for i in Data:
    if Data[i] >= myData[i]:
        if Data[i+1] >= myData[i+1]:
            currentYear = myYear + age
        else:
            currentYear = myYear + age + 1
    else: currentYear = myYear + age + 1
    break
if currentYear == a:
    print(f'\nPerfect, the dates make sense. The current year is {a}')
elif currentYear != a:
    print(f'\nWe might have traveled accross time. The date or the age does not make sense. Do you think we are in {currentYear}?\n')

'''

