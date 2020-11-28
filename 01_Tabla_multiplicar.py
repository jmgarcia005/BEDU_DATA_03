# Preguntar el numero que el usuario quería saber su tabla de multiplicar

numero = int(input('qué número quieres multiplicar?\t'))

print(f'A continuacion se muestra la tabla del {numero}')
print('------------------------------------------------')

for n in range(10):
    indice = n + 1
    resultado = numero * indice
    resultado_impreso = f'{numero} * {indice} = {resultado}'
    print(resultado_impreso)