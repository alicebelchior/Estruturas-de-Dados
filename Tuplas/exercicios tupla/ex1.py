# Crie um script em Python onde deverá haver uma tupla com os nomes dos seus 5 filmes favoritos. O fluxo de programa deverá permitir que você acesse o terceiro elemento da tupla e verifique se o nome "Star Wars" está presente na tupla. O programa deve escrever “Está presente na lista” ou “Não está presente na lista”.

# declaração da tupla
tuplaFilme = ("Vicky Cristina Barcelona", "Imagina Eu & Você", "MadMax", "Velozes e Furiosos", "Transformers")

#verificação do filme 
filme = "Star Wars"
if filme in tuplaFilme[3]:
          print(f' {filme} está presente na lista')
else:
          print(f'{filme} não está presente \n')