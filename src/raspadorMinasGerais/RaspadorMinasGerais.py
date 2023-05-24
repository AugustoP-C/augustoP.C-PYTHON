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
    dropdown_cnpjN = WebDriverWait(nav, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/main/div[2]/section[1]/div[2]/div[1]'))) #/html/body/main/div[2]/section[1]/div[2]/div[1]/span
    cnpjN = dropdown_cnpjN.find_element(By.TAG_NAME, 'span')
    n_list = cnpjN.text.split(" ")
    nEmpresarial = n_list[0] + " " + n_list[1]
    return nEmpresarial
nEmpresarial = portalT("81243735000148")
print(nEmpresarial)
nav.get("https://www.transparencia.mg.gov.br/compras-e-patrimonio/compras-e-contratos/comprasecontratos-resultado-pesquisa-avancada")
nav.find_element(By.XPATH, '//*[@id="jform_TEXTO_CONTRATADO"]').send_keys(nEmpresarial)
time.sleep(1)
nav.find_element(By.XPATH, '//*[@id="pesquisarcontratado"]').click()
time.sleep(1)
nav.find_element(By.XPATH, '//*[@id="dialog"]/table/tbody/tr[1]/td/a').click()
nav.find_element(By.XPATH, '/html/body/div[4]/div[1]/button').click()
time.sleep(1)
nav.find_element(By.XPATH, '//*[@id="btn_pesquisar"]').click()
dropdown_propt = str(nav.current_url).split("/")
propt = str(dropdown_propt[27])


#Entrado no saite da traparencia Minas Gerais e pegando todos os anos ate 2018
nav.get("https://www.transparencia.mg.gov.br/compras-e-patrimonio/compras-e-contratos/comprasecontratos-resultado-pesquisa-avancada")
anos = nav.find_element(By.XPATH, '//*[@id="jform_ano"]')
dropdown_list_anos = str(anos.text).split('2017')
list_ano = str(dropdown_list_anos[0]).strip().split("\n")
list_anos = []
for ano in list_ano:
    list_anos.append(ano.strip())
print(list_anos)

for ano in list_anos:
    nav.get("https://www.transparencia.mg.gov.br/compras-e-patrimonio/compras-e-contratos/comprasecontratos-resultado-pesquisa-avancada/" + ano +"/01-01-" + ano + "/31-12-" + ano + "/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/" + propt + "/0/0/0/0/0/0/1/0/0/0/0/0/0/0/1/0/1/0/0/0")
    time.sleep(10)
    tdody = nav.find_element(By.XPATH, '//*[@id="tabela-paginada"]/tbody') # //*[@id="tabela-paginada"]/tbody/tr/td
    tr = tdody.find_elements(By.TAG_NAME, 'tr')
    for tag in tr:
        if tag.text != "Nenhum registro encontrado":
            print("no ano de " + ano + " existe contrato: " + tag.text)
            # # (Número) - (numero)
            # numero = nav.find_element(By.XPATH, '//*[@id="mainDiv"]/div[2]/div[2]/div/div/div[3]/div[2]')
            # print("numero: " + numero.text)
            # # (Fornecedor CPF/CNPJ) - (cnpj_contratada)
            # fornecedor = nav.find_element(By.XPATH, '//*[@id="mainDiv"]/div[2]/div[2]/div/div/div[10]/div[2]')
            # print("fornecedor: " + fornecedor.text)
            # # (Data Inicial) – (data_inicio_vigencia)
            # dInicial = nav.find_element(By.XPATH, '//*[@id="mainDiv"]/div[2]/div[2]/div/div/div[7]/div[2]')
            # print("data inicial: " + dInicial.text)
            # # (Data Final) – (data_termino_vigencia)
            # dFinal = nav.find_element(By.XPATH, '//*[@id="mainDiv"]/div[2]/div[2]/div/div/div[8]/div[2]')
            # print("data final: " + dFinal.text)
            # # (Valor inicial) – (valor_inicial)
            # vInicial = nav.find_element(By.XPATH, '//*[@id="mainDiv"]/div[2]/div[2]/div/div/div[11]/div[2]')
            # print("valor inicial" + vInicial.text)
            # # (Secretaria) – (Órgão)
            # secretaria = nav.find_element(By.XPATH, '//*[@id="mainDiv"]/div[2]/div[2]/div/div/div[1]/div[2]')
            # print("secretaria : " + secretaria.text)
            # # (Fornecedor) – (Nome Fornecedor)
            # nFornecedor = nav.find_element(By.XPATH, '//*[@id="mainDiv"]/div[2]/div[2]/div/div/div[9]/div[2]/a')
            # print("fornecedor: " + nFornecedor.text)
        else:
            print("Contrato nao encontrado, " + tag.text)
        print("-------------------------")