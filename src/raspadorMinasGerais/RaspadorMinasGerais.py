# tetes: positivo tecnologia cnpj: 81.243.735/0001-48 / https://www.transparencia.mg.gov.br/compras-e-patrimonio/compras-e-contratos/comprasecontratos-resultado-pesquisa-avancada/2019/01-01-2019/31-12-2019/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/19096/0/0/0/0/0/0/1/0/0/0/0/0/0/0/1/0/1/0/0/0

#imports
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from datetime import timedelta
from datetime import datetime
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
nav = webdriver.Chrome()#NAVegador web

def portalT(cnpj): #fução para pegar o nome da empresa usando o cnpj
    # pegar somente os doi primeiros nomes ao entra no portal da tranparencia
    nav.get("https://portaldatransparencia.gov.br/busca/pessoa-juridica/" + str(cnpj))
    dropdown_cnpjN = WebDriverWait(nav, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/main/div[2]/section[1]/div[2]/div[1]'))) #/html/body/main/div[2]/section[1]/div[2]/div[1]/span
    cnpjN = dropdown_cnpjN.find_element(By.TAG_NAME, 'span')
    n_list = cnpjN.text.split(" ")
    nEmpresarial = n_list[0] + " " + n_list[1]
    return nEmpresarial

cnpj = "81243735000148"
nEmpresarial = portalT(cnpj)
print(nEmpresarial)
nav.get("https://www.transparencia.mg.gov.br/compras-e-patrimonio/compras-e-contratos/comprasecontratos-resultado-pesquisa-avancada")
nav.find_element(By.XPATH, '//*[@id="jform_TEXTO_CONTRATADO"]').send_keys(nEmpresarial)
time.sleep(1)
nav.find_element(By.XPATH, '//*[@id="pesquisarcontratado"]').click()
time.sleep(1)

tabela_div = nav.find_element(By.XPATH, '//*[@id="dialog"]')
print(tabela_div)
tbody = tabela_div.find_element(By.TAG_NAME, 'tbody')
print(tbody)
tr = tbody.find_elements(By.TAG_NAME, 'tr')
print(tr[0])
td = tr[0].find_element(By.TAG_NAME, 'td')
print(td)
a = td.find_element(By.TAG_NAME, 'a')
print(a)
propt = a.get_attribute("rel")

# propt = nav.find_element(By.XPATH, '//*[@id="dialog"]/table/tbody/tr[1]/td/a').get_attribute("rel")
# nav.find_element(By.XPATH, '/html/body/div[4]/div[1]/button').click()
# time.sleep(1)
# nav.find_element(By.XPATH, '//*[@id="btn_pesquisar"]').click()
# dropdown_propt = str(nav.current_url).split("/")
# propt = str(dropdown_propt[27])
print(propt)

# #Entrado no saite da traparencia Minas Gerais e pegando todos os anos ate 2018
# nav.get("https://www.transparencia.mg.gov.br/compras-e-patrimonio/compras-e-contratos/comprasecontratos-resultado-pesquisa-avancada")
# anos = nav.find_element(By.XPATH, '//*[@id="jform_ano"]')
# dropdown_list_anos = str(anos.text).split('2017')
# list_ano = str(dropdown_list_anos[0]).strip().split("\n")
# list_anos = []
# for ano in list_ano:
#     list_anos.append(ano.strip())
# print(list_anos)
#
# link = []
# for ano in list_anos:
#     nav.get("https://www.transparencia.mg.gov.br/compras-e-patrimonio/compras-e-contratos/comprasecontratos-resultado-pesquisa-avancada/" + ano +"/01-01-" + ano + "/31-12-" + ano + "/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/0/" + propt + "/0/0/0/0/0/0/1/0/0/0/0/0/0/0/1/0/1/0/0/0")
#     time.sleep(1)
#     tdody = nav.find_element(By.XPATH, '//*[@id="tabela-paginada"]/tbody') # //*[@id="tabela-paginada"]/tbody/tr/td
#     tr = tdody.find_elements(By.TAG_NAME, 'tr')
#     for tag in tr:
#         if tag.text != "Nenhum registro encontrado":
#             dropdown_links_contrato = tag.find_elements(By.CLASS_NAME, 'sorting_1')
#             for a in dropdown_links_contrato:
#                 links_contrato = a.find_elements(By.TAG_NAME, 'a')
#             for links in links_contrato:
#                 link.append(links.get_attribute('href'))
#             print("No ano de " + ano + " existe contrato")
#         else:
#             print("Contrato nao encontrado, " + tag.text)
#         print("-------------------------")
#
# for lk in link:
#     nav.get(lk)
#     dropdown_nCont = nav.find_element(By.XPATH, '//*[@id="detalhe-documento"]/div/table[4]/tbody/tr[10]')
#     nCont = str(dropdown_nCont.text).split(" ")
#     print(len(nCont))
#     print("-------------------------")
#     if len(nCont) > 3:
#         # Origen - saite // Destinio - tabela
#         # (N° Contrato) - (numero)
#         nContrato = nCont[3]
#         print("N° do contarto: " + nContrato)
#
#         # (CNPJ usado na busca) - (cnpj_contratada)
#         cnpj #variavel usada no metodo de portalT
#         print("cnpj: " + cnpj)
#
#         # (Data de Homologação) – (data_inicio_vigencia)
#         dropdown_dHomologaçãoN = nav.find_element(By.XPATH, '//*[@id="detalhe-documento"]/div/table[4]/tbody/tr[6]/td[1]')
#         dHomologação = dropdown_dHomologaçãoN.text.split(":")
#         dHomologaçãoN = dHomologação[1].strip()
#         print("data inicial: " + dHomologaçãoN)
#
#         # (Data de Homologação + 1 ano) – (data_termino_vigencia)
#         dropdown_dHomologacaoF = datetime.strptime(str(dHomologação[1].strip()), '%d/%m/%Y').date()
#         dHomologacaoF = dropdown_dHomologacaoF + timedelta(days=365)
#         print("data final: " + str(dHomologacaoF))
#
#         # (Valor total Homologado) – (valor_inicial)
#         dropdown_valorCompra = nav.find_element(By.XPATH, '//*[@id="detalhe-documento"]/div/table[2]/tbody/tr[5]/td[2]')
#         valorCompr = dropdown_valorCompra.text.split(":")
#         valorCompra = valorCompr[1].strip()
#         print("valor: " + valorCompra)
#
#         # (Unidade Orçamentaria) – (Órgão)
#         dropdown_unidade = nav.find_element(By.XPATH, '//*[@id="detalhe-documento"]/div/table[4]/tbody/tr[4]/td[1]')
#         unidad = dropdown_unidade.text.split(":")
#         unidade = unidad[1].strip()
#         print("orgão: " + unidade)
#
#         # (Fornecedor) – (Nome Fornecedor)
#         dropdown_fornecedor = nav.find_element(By.XPATH, '//*[@id="detalhe-documento"]/div/table[4]/tbody/tr[5]/td[1]')
#         fornecedo = dropdown_fornecedor.text.split("-")
#         fornecedor = fornecedo[1].strip()
#         print("fornecedor: " + fornecedor)
#

