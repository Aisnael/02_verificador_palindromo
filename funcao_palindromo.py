# Função

def palindromo(texto):
    texto = ''.join(texto.lower().split())
    return texto == texto [::-1]

