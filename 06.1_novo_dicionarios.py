# exercídio de dicionários
colors = {
  'azul': 'Blue',
  'vermelho': 'Red',
  'amarelo': 'Yellow',
  'verde': 'Green',
  'preto': 'Black',
  'branco': 'White'
}

cor = input('Digite o nome de uma cor:').lower()
traducao = colors.get(cor, 'Esta cor não consta no meu dicionário')

print(traducao)