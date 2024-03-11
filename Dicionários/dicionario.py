# Procura => Resposta
# Chave => Valor
# um dicionario é uma estrutura de dados composta por chaves e valores

dict = {
          "dog": "cachorro", #Não aceita repetições de chaves
          "cat": "gato",
          "dog": "ave" # o último valor sobreescreve o valor atual da chave
}

print(dict)
print(type(dict))
print(type({"dog":"cachorro"}))

dict1 = {
          "dog": "cachorro",
          "cat": "gato",
          "bird": "ave" 
}

print(dict1)

# Os itens do dicionario não é acessivel por indice 
# dict[0] (error)
# Mas sim por chaves
print(dict1["dog"])

dict1.get("dog") #procura a chave  e retorna o valor
dict1.get("cachorro") #procura a chave e não da erro se não existir
# dict1["cachorro"] #retorna erro se não existir essa chave

# É mutável (alterável)
dict2 = {
          "dog": "cachoro",
          "cat": "gato",
          "bird": "ave" 
}

print(dict2)

dict2["dog"]="cachorro"
print(dict2)