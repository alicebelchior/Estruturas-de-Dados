# Crie um script em Python onde deverá haver uma nova tupla ela deverá apresentar os mesmos elementos da tupla original, mas na ordem inversa(copie os elementos) da tupla do primeiro exercícios.

# declaração da tupla
tuplaFilme = ("Vicky Cristina Barcelona", "Imagina Eu & Você", "MadMax", "Velozes e Furiosos", "Transformers")

# tupla -> lista 
tuplaLista = list(tuplaFilme)

# faz o reverso
tuplaLista.reverse()

tuplaInversa = tuple(tuplaLista)
print(f'A lista reversa fica: {tuplaInversa} \n')