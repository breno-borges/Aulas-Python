import requests as req
import random

indice = int(random.random() * 6)  # Escolhendo o índice do dataset
print(f'Seu índice é o número: {indice}')

# Montando uma lista com as URLs (Não altere essa célula, somente execute)
lista_url = list()
lista_url.append(
    'https://raw.githubusercontent.com/luiscarlosjunior/aulas-graduacao/master/data-science/analise-dados/datasets/csv/dsfaltas/faltasAlunos1.csv')
lista_url.append(
    'https://raw.githubusercontent.com/luiscarlosjunior/aulas-graduacao/master/data-science/analise-dados/datasets/csv/dsfaltas/faltasAlunos2.csv')
lista_url.append(
    'https://raw.githubusercontent.com/luiscarlosjunior/aulas-graduacao/master/data-science/analise-dados/datasets/csv/dsfaltas/faltasAlunos3.csv')
lista_url.append(
    'https://raw.githubusercontent.com/luiscarlosjunior/aulas-graduacao/master/data-science/analise-dados/datasets/csv/dsfaltas/faltasAlunos4.csv')
lista_url.append(
    'https://raw.githubusercontent.com/luiscarlosjunior/aulas-graduacao/master/data-science/analise-dados/datasets/csv/dsfaltas/faltasAlunos5.csv')
lista_url.append(
    'https://raw.githubusercontent.com/luiscarlosjunior/aulas-graduacao/master/data-science/analise-dados/datasets/csv/dsfaltas/faltasAlunos6.csv')

# URL escolhida
url_escolhida = lista_url[indice]
print(f'URL escolhida: {url_escolhida}')

url = url_escolhida

#Aqui faço o pré processamento, primeiro splitando pela quebra de linha
dadosRequisicao = req.get(url).text
linhaDados = dadosRequisicao.split("\n")

#Aqui mostro as três primeiras linhas do dataset tirando o cabeçalho
for linha in range(1, 4):
  print(linhaDados[linha])

#Aqui faço o split das informações por ;
dados = []
for indice in range(1, len(linhaDados)-1):
  dados.append( linhaDados[indice].split(";"))
print(dados)

#Aqui faço a média utilizando list mesmo
sumFev = 0
sumMar = 0
sumAbr = 0
sumMai = 0
sumJun = 0

for indice in range(0, len(dados) - 1):
  sumFev += float(dados[indice][1])
  sumMar += float(dados[indice][2])
  sumAbr += float(dados[indice][3])
  sumMai += float(dados[indice][4])
  sumJun += float(dados[indice][5])

print(f'A media de faltas em fevereiro é de {round(sumFev/len(dados),1)}')
print(f'A media de faltas em março é de {round(sumMar/len(dados),1)}')
print(f'A media de faltas em abril é de {round(sumAbr/len(dados),1)}')
print(f'A media de faltas em maio é de {round(sumMai/len(dados),1)}')
print(f'A media de faltas em junho é de {round(sumJun/len(dados),1)}')