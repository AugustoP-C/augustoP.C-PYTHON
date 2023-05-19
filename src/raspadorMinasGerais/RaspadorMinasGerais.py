# tetes: positivo tecnologia cnpj: 81.243.735/0001-48 / https://www.transparencia.mg.gov.br/compras-e-patrimonio/compras-e-contratos/comprasecontratos-resultado-pesquisa-avancada/2019/01-01-2019/31-12-2019/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/19096/0/0/0/0/0/0/1/0/0/0/0/0/0/0/1/0/1/0/0/0

#imports
import re
from selenium import webdriver
import time
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

nav = webdriver.Chrome()#NAVegador web

def portalT(cnpj): #fução para pegar o nome da empresa usando o cnpj
    # pegar somente os doi primeiros nomes ao entra no portal da tranparencia
    nav.get("https://portaldatransparencia.gov.br/busca/pessoa-juridica/" + str(cnpj))
    dropdown_cnpjN = WebDriverWait(nav, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/main/div[2]/section[1]/div[2]/div[1]')))
    cnpjN = dropdown_cnpjN.find_element(By.TAG_NAME, 'span')
    n_list = cnpjN.text.split(" ")
    nEmpresarial = n_list[0] + "+" + n_list[1]
    return nEmpresarial
nEmpresarial = portalT("07385282000131")
print(nEmpresarial)
def nProtocolo(nEmpresarial): #fução para pegar o numero do protocolo do saite
    nav.get("https://www.transparencia.mg.gov.br/compras-e-patrimonio/compras-e-contratos/comprasecontratos-resultado-pesquisa-avancada")
    nav.find_element(By.XPATH, '//*[@id="jform_TEXTO_CONTRATADO"]').send_keys("positivo tecnologia")
    nav.find_element(By.XPATH, '//*[@id="pesquisarcontratado"]').click()
    time.sleep(1)
    nav.find_element(By.XPATH, '//*[@id="dialog"]/table/tbody/tr[1]/td/a').click()
    nav.find_element(By.XPATH, '/html/body/div[4]/div[1]/button').click()
    time.sleep(1)
    nav.find_element(By.XPATH, '//*[@id="btn_pesquisar"]').click()
    dropdown_propt = str(nav.current_url).split("/")
    propt = dropdown_propt[27]
    return propt
propt = nProtocolo(nEmpresarial)
print(propt)

#Entrado no saite da traparencia Minas Gerais e pegando todos os anos ate 2018
nav.get("https://www.transparencia.mg.gov.br/compras-e-patrimonio/compras-e-contratos/comprasecontratos-resultado-pesquisa-avancada")
anos = nav.find_element(By.XPATH, '//*[@id="jform_ano"]')
dropdown_list_anos = str(anos.text).split('2017')
list_anos = str(dropdown_list_anos[0]).split('\n')
del list_anos[6]
print(list_anos)
