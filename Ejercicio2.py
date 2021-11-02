# Ejercicio2 = Ejercicio1_optimizado + ((año + edad) - mes ) *día) / año 

variables = ['name', 'surname', 'age', 'address', 'date of birth (DD/MM/YYYY)', 'email', 'phone number'] 
resultados = []
for i in variables:
   resultados.append(input(f'What is your {i}?\n')) 
day, month, year = map(int, resultados[4].split('/'))
age = int(resultados[2])
calculo=(((year+age)-month)*day)/year
print(f'\nThe results of the following ecuation ((year + age) - month)*day)/year is {calculo}\n')
print(f'Your info:\n')
for i in range(len(variables)):
    print(f'Your {variables[i]} is {resultados[i]}')
