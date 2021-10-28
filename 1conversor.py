menu = """
Bienvenido al conversor de monedas \U0001F4B5

1 - Soles
2 - Pesos Argentinos
3 - Pesos Mexicanos

Elige una opción: """

opcion = int(input(menu))

if opcion == 1:
  soles = input('¿Cúantos soles tienes?: ')
  soles = float(soles)
  valor_dolar = 3.99
  dolares = soles / valor_dolar
  dolares = round(dolares, 2)
  dolares = str(dolares)
  print('Tienes $' + dolares + ' dólares')
elif opcion == 2: 
  soles = input('¿Cúantos pesos argentinos tienes?: ')
  soles = float(soles)
  valor_dolar = 65
  dolares = soles / valor_dolar
  dolares = round(dolares, 2)
  dolares = str(dolares)
  print('Tienes $' + dolares + ' dólares')
elif opcion == 3:
  soles = input('¿Cúantos pesos mexicanos tienes?: ')
  soles = float(soles)
  valor_dolar = 24
  dolares = soles / valor_dolar
  dolares = round(dolares, 2)
  dolares = str(dolares)
  print('Tienes $' + dolares + ' dólares')
else:
  print('Ingresa una opción correcta por favor')


