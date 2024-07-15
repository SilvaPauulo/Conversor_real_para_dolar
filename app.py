import requests
url = 'https://economia.awesomeapi.com.br/json/last/USD-BRL'
response = requests.get(url)
print(url)

def entrada_em_real():
  valor_real = float(input('Digite o valor em real: '))
  return valor_real

def valor_dolar():
  #Valor total da cotação do dolar no dia atual:
  valor_dolar = float(dados['USDBRL']['bid'])
  return valor_dolar

def hora_da_conversao():
  data_e_hora_da_cotaçao = str(dados['USDBRL']['create_date'])
  return data_e_hora_da_cotaçao

def conversao_real_para_dolar():
  # Entrada em real
  real = entrada_em_real()
  # Valor do dolar
  dolar = valor_dolar()
  # Conversão
  conversao_real_para_dolar = dolar * real
  print(f'O valor do dolar: {dolar:,.2f}')
  print(f'O valor convertido de dolar para o real é R$:{conversao_real_para_dolar:,.2f}')
  print(f'Data da conversão: {hora_da_conversao()}')

def main():
  conversao_real_para_dolar()
main()