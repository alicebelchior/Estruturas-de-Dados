# Escreva um script em Python onde uma função deverá receber uma string como entrada e retorne ao fluxo principal do programa a contagem de vogais e consoantes da string, o programa deverá informar o número de vogais e consoantes

# função contador 
def contador_letra():  
     consoante = 0
     vogal = 0
     
     # var do tipo string convertendo todas as letras para o minusculo 
     palavra = str.lower(input("Escreva uma palavra: "))
     
     # loop para contar vogal/consoante
     for i in palavra:
          if i in 'aeiou':
               vogal += 1
          else:
               consoante +=1
     print(f'Vogal: {vogal} \nConsoante: {consoante}')

# chamando a função
contador_letra()