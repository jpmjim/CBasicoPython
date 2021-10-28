def conversor(moneda, valor_dolar):
  tipo_moneda = input('¿Cúantos ' + moneda +  ' tienes?: ')
  tipo_moneda = float(tipo_moneda)
  dolares = tipo_moneda / valor_dolar
  dolares = round(dolares, 2)
  dolares = str(dolares)
  print('Tienes $' + dolares + ' dólares')

menu = """
Bienvenido al conversor de monedas \U0001F4B5

1 - Soles
2 - Pesos Argentinos
3 - Pesos Mexicanos

Elige una opción: """

opcion = int(input(menu))

if opcion == 1:
  conversor("soles", 3.99)
elif opcion == 2: 
  conversor("pesos argentinos", 65)
elif opcion == 3:
  conversor("pesos mexicanos", 24)
else:
  print('Ingresa una opción correcta por favor')


