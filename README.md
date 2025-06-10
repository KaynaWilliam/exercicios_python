# exercicios_python
import pandas as pd

com_inicial = [
    'Adicionar',
    'Listar',
    'Buscar',
    'Sair'
]

produtos = [] 

while True: 
  print("\n--- Sistema de Cadastro de Produtos ---")
  while True:
      opcao = str(input('O que deseja fazer? (Adicionar, Listar, Buscar, Sair) ')).capitalize()
      if opcao not in com_inicial:
        raise ValueError
      break
    except ValueError:
      print('Erro! Insira uma opção válida.')

  if opcao == 'Adicionar':
    while True:
      try:
        quant = int(input('Quantos produtos deseja adicionar? '))
        break
      except ValueError:
        print('Erro! Insira um número válido.')
    for i in range(quant):
      while True:
        try:
          nome = str(input(f'Insira o nome do {i+1}º produto: ')).capitalize()
          preço = float(input(f'Insira o preço do {nome}: '))
          quantidade = int(input(f'Insira a quantidade do {nome}: ')) 
          break
        except ValueError:
          print('Erro! Insira um nome/preço/quantidade válido.')

      produto = {'nome': nome, 'preço': preço, 'quantidade': quantidade}
      produtos.append(produto)

    print("\nProdutos adicionados com sucesso!")


  elif opcao == 'Listar':
    if produtos:
        df_produto = pd.DataFrame(produtos)
        print("\n--- Lista de Produtos ---")
        print(df_produto)
    else:
        print("\nNenhum produto cadastrado.")


  elif opcao == 'Buscar':
    while True:
      try:
        nome_buscar = str(input('Insira o nome do produto que deseja buscar: ')).capitalize()
        break
      except ValueError:
        print('Erro! Insira um nome válido.')

    encontrado = False
    for produto in produtos:
      if produto['nome'] == nome_buscar:
        print("\n--- Produto Encontrado ---")
        df_produto = pd.DataFrame([produto])
        print(df_produto)
        encontrado = True
        break

    if not encontrado:
      print('\nProduto não encontrado')


  elif opcao == 'Sair':
    print('\nObrigado por usar o sistema. Saindo...')
    break
