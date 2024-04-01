def dados_usuario(idade = 0):
     print(f'idade: {idade}')    
dados_usuario(10)

def dados_usuario(idade = 50):
     print(f'idade: {idade}')     
dados_usuario()

def dados_usuario(nome, idade, salario, desconto):
     print(f'{nome}')
     print(f'{idade}')
     print(f'{salario}')
     print(f'{desconto}')
dados_usuario(salario=3000, desconto=1000, idade=30, nome='Manoel')