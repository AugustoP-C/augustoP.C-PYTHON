# cnpj para testes: 07385282000131 https://portaldatransparencia.gov.br/pessoa-juridica/busca/lista?termo=07385282000131&pagina=1&tamanhoPagina=10&

from selenium import webdriver
import time
import pandas as pd
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

nav = webdriver.Chrome()

def portalT(cnpj):
    # pegar somente os doi primeiros nomes ao entra no portal da tranparencia
    nav.get("https://portaldatransparencia.gov.br/pessoa-juridica/busca/lista?termo=" + str(cnpj) +"&pagina=1&tamanhoPagina=10&")
    nav.find_element(By.XPATH, '//*[@id="resultados"]/li/h3/a').click()
    time.sleep(2)
    dropdown_cnpjN = nav.find_element(By.XPATH, '/html/body/main/div[2]/section[1]/div[2]/div[1]')
    cnpjN = dropdown_cnpjN.find_element(By.TAG_NAME, 'span')
    n_list = cnpjN.text.split(" ")
    nEmpresarial = n_list[0] + "+" + n_list[1]
    return nEmpresarial

nav.get("http://transparencia.sobral.ce.gov.br/contrato/ano_exercicio:")
nav.find_element(By.XPATH, '//*[@id="cookieConsentContainer"]/div[2]/a').click()
nav.find_element(By.CSS_SELECTOR, ".input-field:nth-child(1) > .select-wrapper").click()
time.sleep(3)
dropdown_anos = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/main/div/div[2]/div/div/div[1]/form/div[1]/div[1]/div/ul')))
anos = dropdown_anos.find_elements(By.TAG_NAME, 'li')
ano_list = []
for ano in anos:
    ano_list.append(ano.text)
del ano_list[0]
# print(ano_list)
# print(portalT("07385282000131"))
portalTV = portalT("07385282000131")
print(portalTV)
nav.get("http://transparencia.sobral.ce.gov.br/contrato/ano_exercicio:" + str(ano) + "/fornecedor:" + portalTV)

for ano in ano_list:
    nav.get("http://transparencia.sobral.ce.gov.br/contrato/ano_exercicio:" + str(ano) + "/fornecedor:" + portalTV)
    tabela = nav.find_element(By.XPATH, '//*[@id="mainDiv"]/div[3]/div/div/div/div[2]/div[2]')
    links_contatros = tabela.find_elements(By.TAG_NAME, 'a')
    # for link in links_contatros:
    #
    # if link.get_attribute('href'):
    #     if 'contrato/detail' in link.get_attribute('href'):
    #         time.sleep(2)
    #         nav.get(link.get_attribute('href'))
    #         contrato = nav.find_element(By.XPATH, '//*[@id="mainDiv"]/div[2]/div[2]/div/div')
    #         print(contrato.text)
    #     else:
    #         print("Contrato nao encontrado")
    # Origem(identificação do campo na página de raspagem)
    # Destino(identificação da coluna na tabela onde será gravado o dado)
    # (Número) - (numero)
    # (Fornecedor CPF/CNPJ) - (cnpj_contratada)
    # (Data Inicial) – (data_inicio_vigencia)
    # (Data Final) – (data_termino_vigencia)
    # (Valor inicial) – (valor_inicial)
    # (Secretaria) – (Órgão)
    # (Fornecedor) – (Nome Fornecedor)
    # (Colocar na tabela manualmente “Estadual" – (Esfera)
    # (Colocar na tabela manualmente “Executivo” – (Poder)
    # (Colocar na tabela manualmente “Sobral” – (UF Órgão)
    # (Colocar na tabela manualmente “Sobral (CE)) contratos” – (Fonte)
    time.sleep(5)

