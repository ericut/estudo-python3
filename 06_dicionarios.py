# dicionários
joao = {
  'nome': 'João',
  'sobrenome': 'Pereira',
  'profissao': 'Programador',
  'filhos': ['Pedro', 'Maria']
}

print(type(joao))
print(len(joao))
print(joao['nome'])
print(joao['filhos'][0])

# mutações
# deletando um valor:
del joao['filhos']

## mudando algum valor
joao['profissao'] = 'aposentado'
print(joao)

# verificar se existe algum valor no dicionario
print('sobrenome' in joao) 

# verificar o dicionário / percorrendo todos os elementos
for x in joao:
  print(x)

# imprimindo com detalhes
for x in joao:
  print(x + ': ' + joao[x])

# utilizando método .get('chave', 'Texto retorno')
# solicitar informação dentro do dicionário
print(joao.get('nome', 'Esta informação não consta no cadastro'))
print(joao.get('idade', 'Esta informação não consta no cadastro'))


# incluindo valores
joao['filhos'] = ['Pedro', 'Maria']
joao['filhos'].append('Jorge') # incluindo valor na lista
print(joao)

# apagando toda informação do dicionário
joao.clear()
print(joao)

