#caso do hemocentro, identificar se um possivel doador de sangue está apto para realizar o procediemento

#caso haja algum impedimento, a informação virá para essa lista e será informada no final da avaliação

impedimentos = []

#extração de dados no usuario inicial

while True:
  try:
    sexo = str(input('Olá! Para começarmos a avaliação para saber se você está apto para a doação em nosso hemocentro, informe seu sexo (M/F): ')).upper()
    doacao = str(input('Você já realizou alguma doação em algum hemocentro? (S/N): ')).upper()
    idade = int(input('Informe sua idade: '))
    peso= float(input('Informe seu peso: '))
    sint14 = str(input('Como estamos em periodo de Covid-19, é necessario informar algumas informações relacionadas a isso.\nVocê teve febre ou sintomas gripais nos últimos 14 dias? (S/N): ')).upper()
    viagem = str(input('Você realizou alguma viagem para o exterior nos últimos 30 dias? (S/N): ')).upper()
    contato = str(input('Você teve contato com algum caso suspeito ou confirmado nos últimos 30 dias? (S/N): ')).upper
    break
  except ValueError:
   print('Digite uma opção válida')

#extração de dados conforme o sexo
#homem
while sexo == 'M':
  while True:
    try:
      if doacao == 'S':
        qtdoacoes = int(input('Quantas doações você já realizou este ano? '))
        itdoacoes = int(input('Há quantos meses foi sua ultima doação? '))
      else:
       pass
      break
    except ValueError:
      print('Alguma das informações informadas não é valida. Por favor, informe as informações de forma correta, se lembrando de responder com "S" ou "N"')
  break

#mulher:
while sexo == 'F':
  while True:
    try:
      gra_amamentacao = str(input('Você está grávida ou amamentando um bebê menor de 12 meses? (S/N): ')).upper()
      if gra_amamentacao == 'S':
        gra_amamentacao = True
      else:
        gra_amamentacao = False
      if doacao == 'S':
        qtdoacoes = int(input('Quantas doações você já realizou este ano? '))
        itdoacoes = int(input('Há quantos meses foi sua ultima doação? '))
      else:
        pass
      break
    except ValueError:
      print('Alguma das informações informadas não é valida. Por favor, informe as informações de forma correta, se lembrando de responder com "S" ou "N"')
  break

#validação dos dados geral

if idade < 16:
  impedimentos.append('Você não tem idade suficiente para doar sangue')
elif idade < 18 and idade > 16:
  autorizacao_menor = str(input('Você tem autorização do seu responsavel para doar sangue? (S/N): ')).upper()
  if autorizacao_menor == 'N':
    impedimentos.append('Você não tem autorização para doar sangue')
  else:
    pass
elif idade > 18:
  pass
elif idade > 60 and idade < 69:
  autorizacao_maior = str(input('Você tem autorização do seu médico para doar sangue? (S/N): ')).upper()
  if autorizacao_maior == 'N':
    impedimentos.append('Você não tem autorização para doar sangue')
  else:
    pass
else:
  impedimentos.append('Você não tem idade para doar sangue')

if peso >= 50:
  pass
else:
  impedimentos.append('Você não tem peso suficiente para doar sangue')

if sint14 == 'S':
  impedimentos.append('Você teve febre ou sintomas gripais nos últimos 14 dias')
  pass
else:
  pass

if viagem == 'S':
  impedimentos.append('Você realizou alguma viagem para o exterior nos últimos 30 dias')
  pass
else:
  pass

if contato == 'S':
  impedimentos.append('Você teve contato com algum caso suspeito ou confirmado nos últimos 30 dias')
  pass
else:
  pass

#validação de dados para homem

if sexo == 'M':
  if doacao == 'S':
    if qtdoacoes == 4:
      impedimentos.append('Você já realizou 4 doações este ano')
      pass
    else:
      pass
    if itdoacoes < 2:
      impedimentos.append('Você realizou uma doação há menos de 2 meses, que é o intervalo minimo.')
      pass
    else:
      pass
  else:
    pass

#validação de dados para mulher

if sexo == 'F':
  if doacao == 'S':
    if qtdoacoes == 3:
      impedimentos.append('Você já realizou 3 doações este ano')
      pass
    else:
      pass
    if itdoacoes < 3:
      impedimentos.append('Você realizou uma doação há menos de 3 meses, que é o intervalo minimo.')
      pass
    else:
      pass
  else:
    pass
  if gra_amamentacao == True:
    impedimentos.append('Você está grávida ou amamentando um bebê menor de 12 meses')
    pass
  else:
    pass

#retorno do resultado para o usuario

if len(impedimentos) == 0:
  print('Parabéns! Você está apto para a doação em nosso hemocentro! Siga os próximos passos para a realização da doação!')
else:
  print('Foram encontrados os seguintes impedimentos:')
  for impedimento in impedimentos:
    print(f'- {impedimento}')




#não é por nada não, sor... mas esse aqui eu fiz com muito esmero kkkkkkkkkkkk
