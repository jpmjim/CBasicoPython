def imprimir_mensaje():
  print('Mensaje especial: ')
  print('Estoy aprendiendo a usar funciones')

imprimir_mensaje()



def conversacion(mensaje):
  print('Hola')
  print('Cómo estás')
  print(mensaje)
  print('Adiós')

opcion = int(input('Elige un opción (1, 2, 3): '))

if opcion == 1:
  conversacion('Elegiste la opción 1')
elif opcion == 2:
  conversacion('Elegiste la opción 2')
elif opcion == 3:
  conversacion('Elegiste la opción 3')
else:
  print('Escribe la opción correcta')