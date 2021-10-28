soles = input('¿Cúantos soles tienes?: ')
soles = float(soles)
valor_dolar = 3.99
dolares = soles / valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)
print('Tienes $' + dolares + ' dólares')