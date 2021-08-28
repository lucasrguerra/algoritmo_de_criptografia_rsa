import random

def gerar_primo():
  while True:
    numero = random.randrange((2 ** 4), (2 ** 10))
    if ePrimo(numero) == True:
      return numero

def ePrimo(numero):
  if numero <= 1:
    return False
  if numero <= 3:
    return True
  if (numero % 2) == 0 or (numero % 3) == 0:
    return False
  index = 5
  while index * index <= numero:
    if (numero % index) == 0 or (numero % (index + 2)) == 0:
      return False
    index += 6
  return True

def totiente(numero): 
  if ePrimo(numero):
    return numero - 1
  else:
    return False

def modulo_condicionado(valor_1, valor_2):
  resto = 1
  while valor_2 != 0:
    resto = valor_1 % valor_2
    valor_1 = valor_2
    valor_2 = resto
  return valor_1    

def gerar_e(numero): 
  while True:
    e = random.randrange(2, numero) 
    if(modulo_condicionado(numero, e) == 1):
      return e

def modular(valor_1, valor_2):
  if valor_1 < valor_2 :
    return valor_1
  else:
    return (valor_1 % valor_2)

def encriptar(texto, e, comum):
  texto_encriptado = []

  for digito in texto:
    digito_encriptado = modular((ord(digito) ** e), comum)
    texto_encriptado.append(digito_encriptado)

  return texto_encriptado

def decriptar(texto_encriptado, f, comum):
  texto_decriptado = ''

  for digito_encriptado in texto_encriptado:
    digito_decriptado = chr(modular((digito_encriptado ** f), comum))
    texto_decriptado += (digito_decriptado)

  return texto_decriptado

def gerar_f(totiente_do_comum, e):
  f = 0
  while modular((f * e), totiente_do_comum) != 1:
      f += 1
  return f