import time
from datetime import datetime
from selenium import webdriver
from selenium.common import TimeoutException, StaleElementReferenceException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests

import os
import time
import traceback

# from classes.Contrato import Contrato
# from repository.pedido_fonte_dados_repository import criar_pedido_fonte_dados, alterar_status
# from repository.erro_fonte_dados_repository import criar_erro_fonte_dados
#
# id_fonte_dados =
#
# log_dir = '/tmp/transp_ce_log'
# log_file = '/tmp/transp_ce_log/log.txt'
#
# if not os.path.exists(log_dir):
#     os.makedirs(log_dir)
#
def logger (logfile, info):
    f = open(logfile, 'a+')
    currentdate = time.strftime('%Y-%m-%d|%H:%M:%S')
    f.write(currentdate + ',' + info + '\n')
    f.write(traceback.format_exc() + '\n')
    f.close()
#
# def de_para_contratos(dict_contratos_list):
#     contratos_list = []
#
#     for contrato_dict in dict_contratos_list:
#         contrato = Contrato(
#             numero=contrato_dict['numero_contrato'],
#             cnpj_contratada=contrato_dict['cnpj'],
#             data_inicio_vigencia=contrato_dict['data_inicio_vigencia'],
#             data_termino_vigencia=contrato_dict['data_fim_vigencia'],
#             valor_inicial=float(contrato_dict['valor_global']),
#             orgao=contrato_dict['orgao'],
#             nome_fornecedor=contrato_dict['fornecedor'],
#             esfera='Estadual',
#             poder='Executivo',
#             uf_orgao='CE',
#             fonte='Transparencia Ceara'
#         )
#         if contrato.data_inicio_vigencia and type(contrato.data_inicio_vigencia) == str:
#             contrato.data_inicio_vigencia = datetime.strptime(contrato.data_inicio_vigencia, '%d/%m/%Y')
#         if contrato.data_termino_vigencia and type(contrato.data_termino_vigencia) == str:
#             contrato.data_termino_vigencia = datetime.strptime(contrato.data_termino_vigencia, '%d/%m/%Y')
#         contratos_list.append(contrato)
#     return contratos_list
#
# def realizar_raspagem(cnpj: str, id_pedido: int):
#     if not os.path.exists(log_dir):
#         os.makedirs(log_dir)
#
#     status = {
#         'Contratos': 'Pendente'
#     }
#     id_pedido_fonte_dados = criar_pedido_fonte_dados(status, id_fonte_dados, id_pedido)
#     dict_contratos_list = []


cnpj = 34635368000148
url = f'https://cearatransparente.ce.gov.br/portal-da-transparencia/contratos/contratos?cod_concedente=+&cod_gestora=+&data_assinatura=&data_vigencia=&decricao_modalidade=+&descricao_situacaxdatalist-search_datalist=&locale=pt-BR&page=1000000&search={cnpj}&search_datalist=&search_sacc=&sort_column=integration_contracts_contracts.descricao_nome_credor&sort_direction=asc&tipo_objeto=+&__=__'
#       https://cearatransparente.ce.gov.br/portal-da-transparencia/contratos/contratos?cod_concedente=+&cod_gestora=+&data_assinatura=&data_vigencia=&decricao_modalidade=+&descricao_situacaxdatalist-search_datalist=&locale=pt-BR&page={i}&search={cnpj}&search_datalist=&search_sacc=&sort_column=integration_contracts_contracts.descricao_nome_credor&sort_direction=asc&tipo_objeto=+&__=__'
#       https://cearatransparente.ce.gov.br/portal-da-transparencia/contratos/contratos?cod_concedente=+&cod_gestora=+&data_assinatura=&data_vigencia=&decricao_modalidade=+&descricao_situacao=+&locale=pt-BR&page={i}&search={cnpj}&search_datalist=&search_sacc=&sort_column=integration_contracts_contracts.data_assinatura&sort_direction=asc&tipo_objeto=+&__=__
url2 = f'https://cearatransparente.ce.gov.br/portal-da-transparencia/contratos/contratos?cod_concedente=+&cod_gestora=+&data_assinatura=&data_vigencia=&decricao_modalidade=+&descricao_situacaxdatalist-search_datalist=&locale=pt-BR&page=1000000&search=28123417000160&search_datalist=&search_sacc=&sort_column=integration_contracts_contracts.descricao_nome_credor&sort_direction=asc&tipo_objeto=+&__=__'

    #Inicializa o Chrome Linux

    # chrome_options = Options()
    # chrome_options.add_argument("--headless")
    # chrome_options.add_argument("--no-sandbox")
    # chrome_options.add_argument("--disable-dev-shm-usage")
    # chrome_prefs = {}
    # chrome_options.experimental_options["prefs"] = chrome_prefs
    # chrome_prefs["profile.default_content_settings"] = {"images": 2}
    # try:
    # status['Contratos'] = 'Carregando'
    # alterar_status(status, id_pedido_fonte_dados)
    # logger(log_file, f'Inicio da raspagem')
driver = webdriver.Chrome()
# wait = WebDriverWait(driver, 10)

#Entrado no saite e esperando ele carregar
# driver.get(url)
# time.sleep(5)

# iframe = driver.find_element(By.XPATH, '/html/body/footer/div[2]/div/div[3]/div/div/span/iframe')
# driver.switch_to.frame(iframe)
#
# driver.find_element(By.XPATH, '/html/body/div[6]/div[2]/div/a').click() #/html/body/div[6]/div[2]/div/a
# time.sleep(2)
# driver.find_element(By.LINK_TEXT, "Última").click()
# time.sleep(10)
# dropdown_numero_paginas = driver.find_element(By.XPATH, '/html/body/div[5]/div[6]/div/div/div[2]/div/div[2]/div/div[2]/div[5]/div/nav')
# numero_paginas = dropdown_numero_paginas.find_element(By.CLASS_NAME, 'page current')
# print(numero_paginas.text)
driver.get(url)
time.sleep(5)
dropdown_total_pages = driver.find_element(By.XPATH, '/html/body/div[5]/div[6]/div/div/div[2]/div/div[2]/div/div[2]/div[5]/div/nav').text
total_pages = dropdown_total_pages.split("\n")
print(total_pages)
pages = total_pages[len(total_pages) - 1]
print(type(pages))
for i in range(int(pages)):
    driver.get("https://cearatransparente.ce.gov.br/portal-da-transparencia/contratos/contratos?cod_concedente=+&cod_gestora=+&data_assinatura=&data_vigencia=&decricao_modalidade=+&descricao_situacaxdatalist-search_datalist=&locale=pt-BR&page=" + str(i + 1) + "&search=" + str(cnpj) + "&search_datalist=&search_sacc=&sort_column=integration_contracts_contracts.descricao_nome_credor&sort_direction=asc&tipo_objeto=+&__=__")
    contrato_dict = {
        'numero': driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div/div[1]/div[1]/h2').text,
        'cnpj': driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div/div[1]/div[2]/div[2]/div[3]/div/p[1]').text,
        'data_inicio_vigencia': driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div/div[1]/div[2]/div[4]/div[2]/div/p[1]').text,
        'data_termino_vigencia': driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div/div[1]/div[2]/div[4]/div[3]/div/p[1]').text,
        'valor_inicial': driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div/div[1]/div[2]/div[5]/div[5]/div/p[1]').text,
        'orgao': driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div/div[1]/div[2]/div[3]/div[1]/div/p[1]').text,
        'nome_fornecedor': driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div/div[1]/div[2]/div[2]/div[2]/div/p[1]').text
    }

            # dict_contratos_list.append(contrato_dict)
            #
            # contratos_list = de_para_contratos(dict_contratos_list)
            # logger(log_file, f'Guardou os dados de contratos encontrados')
            #
            # if len(contratos_list) == 0:
            #     status['Contratos'] = 'Sem Dados'
            #     logger(log_file, f'Raspagem realizada: sem dados')
            #
            # else:
            #     status['Contratos'] = 'Concluído'
            #     logger(log_file, f'Raspagem realizada: concluída')

driver.quit()

    #     except Exception as e:
    #     status['Contratos'] = 'Erro'
    #     logger(log_file, f'Erro na raspagem')
    #     erro = str(e).split("\n")
    #     if 'timeout' in erro[0]:
    #         criar_erro_fonte_dados(id_pedido, id_fonte_dados, 'Contratos', 'Timeout', erro[0])
    #     else:
    #         criar_erro_fonte_dados(id_pedido, id_fonte_dados, 'Contratos', 'Erro na raspagem', erro[0])
    #     contratos_list = []
    # alterar_status(status, id_pedido_fonte_dados)
    #
    # return {
    #     'status': status,
    #     'contratos': contratos_list,
    # }
    #