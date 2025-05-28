## Descrição do Projeto
Este projeto é um script simples em Python desenvolvido uma função que verifique se uma palavra ou frase é um palíndromo (ou seja, se pode ser lida da mesma forma de trás para frente, ignorando espaços e maiúsculas/minúsculas).

## Funcionalidades
- Verifica se uma palavra ou frase é um palíndromo
- Ignornar espaços em branco
- Ignorar letras maiúsculas e minúsculas
- Mostrar no terminal para usuário
- (Em breve) Interface gráfica

## Tecnologias
- Python
- lower(): para deixar tudo em minúsculo
- split(): para remover espaços
- Lógica de comparação entre texto normal e invertido

## 1. Estrutura do Projeto 
- Criada pasta do módulo verificador_palindromo
 - mkdir verificador_palindromo
 - cd verificador_palindromo
- Criada ambiente virtual
 - python -m venv venv
- Ativar ambiente venv
 - venv\Scripts\activate

## 2. Criada pacote com arquivos python
- init.py -> arquivo para marcar(iniciar) o pacote
- funcao_palindromo.py -> função que faz a verificação
- main.py -> script principal que interage com usúario

## 3. Desenvolvimento da função_palindromo()

- Definição da função - def palindromo(texto):
 - Criada uma função chamada palindromo que recebe o parâmetro texto que pode ser uma palavra ou frase
 - Toda vez que chamar essa função, vai passar o que quer verificar
 - texto.lower() -> Converte todas as letras para minúsculas
 - .split() -> Separa o texto por espaços, gerando uma lista de palavras
 - .join(...) -> Junta todas as palavras da lista em uma única string, sem espaços
 - return texto == texto[:: -1] -> Inverte o texto usando fatiamento

 