IVA = 0.16

precios_sin_IVA = [376, 576, 384, 672, 648, 720, 640, 576]

for precio in precios_sin_IVA:
    resultado = precio * (1 + IVA)
    resultado = round(resultado, 2 )
    resultado_impreso = f'${precio} con IVA incluido: {resultado}'
    print(resultado_impreso)