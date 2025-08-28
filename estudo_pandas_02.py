#crie uma lista de dicionarios onde cada dicionario representa um produto com nome e preço. Imprima o total da compra

import pandas as pd

produtos = []

while True:
  try:
    quant = int(input('Quantos produtos deseja inserir? '))
    break
  except ValueError:
    print('Erro! Insira um número válido.')

for i in range(quant):
  while True:
    try:
      nome = str(input(f'Insira o nome do {i+1}º produto: ')).capitalize()
      break
    except ValueError:
      print('Erro! Insira um nome válido.')

  while True:
    try:
      preco = float(input(f'Insira o preço do {nome[0:1]}: '))
      break
    except ValueError:
      print('Erro! Insira um preço válido.')
  while True:
    try:
      quantidade = int(input(f'Insira a quantidade do {nome[0:1]}: '))
      break
    except ValueError:
      print('Erro! Insira uma quantidade válida.')
  while True:
    try:
      produto = {'nome': nome, 'preco': preco, 'quantidade': quantidade}
      produtos.append(produto)
      break
    except ValueError:
      print('Erro! Insira um produto válido.')
print()
df = pd.DataFrame(produtos)
print(df)

total = 0

for i in range(len(produtos)):
  total += produtos[i]['preco'] * produtos[i]['quantidade']

print(f'O total da compra é: {total}')
