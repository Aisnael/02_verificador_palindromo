from funcao_palindromo import palindromo

frase = input('Digite uma palavra ou frase: ')
if palindromo(frase):
    print('É um palíndromo!')
else:
    print('não é um palíndromo!')

