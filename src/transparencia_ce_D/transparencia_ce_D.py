import time
from datetime import datetime
from selenium import webdriver
from selenium.common import TimeoutException, StaleElementReferenceException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests

import os
import time
import traceback

log_dir = '/tmp/sobral_contratos_log'
log_file = '/tmp/sobral_contratos_log/log.txt'

if not os.path.exists(log_dir):
    os.makedirs(log_dir)
def logger (logfile, info):
    f = open(logfile, 'a+')
    currentdate = time.strftime('%Y-%m-%d|%H:%M:%S')
    f.write(currentdate + ',' + info + '\n')
    f.write(traceback.format_exc() + '\n')
    f.close()

cnpj = 22
# obtetdo o numero total de paginas
url = f'https://cearatransparente.ce.gov.br/portal-da-transparencia/contratos/contratos?cod_concedente=+&cod_gestora=+&data_assinatura=&data_vigencia=&decricao_modalidade=+&descricao_situacaxdatalist-search_datalist=&locale=pt-BR&page=1000000&search={cnpj}&search_datalist=&search_sacc=&sort_column=integration_contracts_contracts.descricao_nome_credor&sort_direction=asc&tipo_objeto=+&__=__'

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_prefs = {}
chrome_options.experimental_options["prefs"] = chrome_prefs
chrome_prefs["profile.default_content_settings"] = {"images": 2}


logger(log_file, f'Inicio da raspagem')
driver = webdriver.Chrome()

#Entrado no saite e esperando ele carregar, e pegando o total de paginas
driver.get(url)
time.sleep(15)
dropdown_total_pages = driver.find_element(By.XPATH, '/html/body/div[5]/div[6]/div/div/div[2]/div/div[2]/div/div[2]/div[5]/div').text
total_pages = dropdown_total_pages.split("\n")
pages = total_pages[len(total_pages) - 1]
logger(log_file, f'Total de paginas obtido')

links = []
for page in range(int(pages)):
    driver.get("https://cearatransparente.ce.gov.br/portal-da-transparencia/contratos/contratos?cod_concedente=+&cod_gestora=+&data_assinatura=&data_vigencia=&decricao_modalidade=+&descricao_situacaxdatalist-search_datalist=&locale=pt-BR&page=" + str(page + 1) + "&search=" + str(cnpj) + "&search_datalist=&search_sacc=&sort_column=integration_contracts_contracts.descricao_nome_credor&sort_direction=asc&tipo_objeto=+&__=__")
    time.sleep(35.)
    dropdown_contratos = driver.find_element(By.XPATH, '/html/body/div[5]/div[6]/div/div/div[2]/div/div[2]/div/div[2]/div[3]/table/tbody')
    contratos = dropdown_contratos.find_elements(By.TAG_NAME, 'tr')
    for dropdown_dados in contratos:
        dropdown_a = dropdown_dados.find_element(By.TAG_NAME, 'td')
        a = dropdown_a.find_element(By.TAG_NAME, 'a')
        link = a.get_attribute('href')
        links.append(link)
        logger(log_file, f'Links obtidos')
for dados in links:
    driver.get(dados)
    time.sleep(1)
    dropdown_numero = driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div/div[1]/div[1]/h2').text
    dropdown_cnpj = driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div/div[1]/div[2]/div[2]/div[3]/div/p[2]').text
    data_inicio_vigencia = driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div/div[1]/div[2]/div[4]/div[2]/div/p[2]').text
    data_termino_vigencia = driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div/div[1]/div[2]/div[4]/div[3]/div/p[2]').text
    dropdown_valor_inicial = driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div/div[1]/div[2]/div[5]/div[5]/div/p[2]').text
    orgao = driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div/div[1]/div[2]/div[3]/div[1]/div/p[2]').text
    nome_fornecedor = driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div/div[1]/div[2]/div[2]/div[2]/div/p[2]').text

    numero = dropdown_numero.split(" ")
    cnpj2 = dropdown_cnpj.replace('.', '').replace('/', '').replace('-', '')
    valor_inicial = dropdown_valor_inicial.replace('R$ ', '').replace('.', '').replace(',', '.')

    print(numero)

    contrato_dict = {
        'numero': numero[2],
        'cnpj': cnpj2,
        'data_inicio_vigencia': data_inicio_vigencia,
        'data_fim_vigencia': data_termino_vigencia,
        'valor_global': valor_inicial,
        'orgao': orgao,
        'fornecedor': nome_fornecedor
                    }
    logger(log_file, f'Raspagem completa')
