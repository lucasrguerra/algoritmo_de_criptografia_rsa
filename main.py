import RSA

texto = input("Insira a mensagem: ")

p = RSA.gerar_primo()
q = RSA.gerar_primo()

comum = p * q
totiente_do_comum = RSA.totiente(p) * RSA.totiente(q)

e = RSA.gerar_e(totiente_do_comum)
chave_publica = (comum, e)

f = RSA.gerar_f(totiente_do_comum, e)
chave_privada = (comum, f)

print('\nChave Pública:', chave_publica)
print('Chave Privada:', chave_privada, '\n')

texto_encriptado = RSA.encriptar(texto, e, comum)
texto_decriptado = RSA.decriptar(texto_encriptado, f, comum)

print('Mensagem Encriptada:', texto_encriptado)
print('Mensagem decriptada:', texto_decriptado)