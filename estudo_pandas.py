import pandas as pd

#escreva um codigo onde um dicionario receba produtos com seus preço. imprima os produtos que custem mais de 50

produtos = []

while True:
  try:
    quant = int(input("Digite a quantidade de produtos que deseja adicionar: "))
    break
  except ValueError:
    print("Digite um número inteiro válido.")

for i in range(quant):
  while True:
    try:
      nome = str(input(f"Digite o nome do {i+1}ºproduto: "))
      break
    except ValueError:
      print("Digite um número válido.")
  while True:
    try:
      preco = float(input(f"Digite o preço do {i+1}ºproduto: "))
      break
    except ValueError:
      print("Digite um número válido.")

  while True:
    try:
      produto = {'nome': nome, 'preco': preco}
      produtos.append(produto)
      break
    except ValueError:
      print("Digite um produto válido.")

df_produtos = pd.DataFrame(produtos)
df_produtos = df_produtos[df_produtos['preco'] > 50]
print(df_produtos)
