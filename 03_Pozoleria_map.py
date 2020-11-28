# Como usar la funcion map de python 

IVA = 0.16

def aplicar_IVA(precio):
    resultado = precio * (1 + IVA)
    return round(resultado, 2)

precios_sin_IVA = [376, 576, 384, 672, 648, 720, 640, 576]
print(precios_sin_IVA)

#Usar Map   para una lista

precios_sin_IVA = list(map(aplicar_IVA,precios_sin_IVA))
print(precios_sin_IVA)