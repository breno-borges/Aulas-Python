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

linhas = [item.split(';') for item in texto]
#Aqui separo o cabecalho
cabecalho = str(linhaDados[0]).split(";")