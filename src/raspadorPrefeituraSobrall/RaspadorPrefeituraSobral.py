# 1 acessar a URL:http://transparencia.sobral.ce.gov.br/contrato/ano_exercicio:2023
# 2 ??? ver a origem(identificação do campo na página de raspagem) e o
# destino(identificação da coluna na tabela onde será gravado o dado)
# 3 obeter os dados: numero, cpf/cnpj do fornecedor(cnpj/cpf_contratada), data do pedido
# data inicial(data_inicio_vigencia) e data final (data_termino_vigencia), valor do pedido(valor_inicial),
# orgão fiscalizador(orgão), fornecedor(nome do fornecedor)
# 4 faser o raspador repetir esse processo com diferentes anos e diferentes telas
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
for ano in ano_list:
    nav.get("http://transparencia.sobral.ce.gov.br/contrato/ano_exercicio:" + str(ano) + "/fornecedor:" + portalTV)
    time.sleep(5)

