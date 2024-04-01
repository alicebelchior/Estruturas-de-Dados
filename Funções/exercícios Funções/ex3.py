# Escreva um script em Python onde uma função deverá receber um texto e contar o número de palavras nele contido. O programa deverá informar o resultado da contagem das palavras.

# função texto
def contador_palavra():
     palavra = 0
     
     # var do tipo string que lista cada palavra
     frase = str.split(input('Escreva uma frase: '))
     
     # loop para contar as palavras
     for word in frase:
          palavra += 1
     print(f'Nº de palavras = {palavra}')

# chamando a função
contador_palavra()