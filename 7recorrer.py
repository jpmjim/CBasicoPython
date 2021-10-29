def run():
  # Imprimir letra 
  nombre = input('Esxribe tu nombre: ')
  for letra in nombre:
    print(letra)

  # Imprimir caracter cada uno en mayusculas
  frase = input('Escribe una frase: ')
  for caracter in frase:
    print(caracter.upper())


if __name__ == '__main__':
  run()