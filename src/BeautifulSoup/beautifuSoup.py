import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
i = 1
cnpj = 34635368000148
url = f'https://cearatransparente.ce.gov.br/portal-da-transparencia/contratos/contratos?cod_concedente=+&cod_gestora=+&commit=Buscar&data_assinatura=&data_vigencia=&decricao_modalidade=+&descricao_situacao=+&flexdatalist-search_datalist=&locale=pt-BR&page={i}&search={cnpj}&search_datalist=&search_sacc=&sort_column=integration_contracts_contracts.data_assinatura&sort_direction=asc&tipo_objeto=+&utf8=%E2%9C%93&__=__'
driver = webdriver.Chrome()

requisicao = requests.get(url)
soup = BeautifulSoup(requisicao.text, 'html.parser')
# soup = BeautifulSoup(driver.page_source, 'html.parser')
time.sleep(5)
total_pages = soup.find_all('a')
# print(soup)
for i in total_pages:
    print(i)
    print(" ")
# print(len(total_pages))

# https://cearatransparente.ce.gov.br/portal-da-transparencia/contratos/contratos?cod_concedente=+&cod_gestora=+&data_assinatura=&data_vigencia=&decricao_modalidade=+&descricao_situacaxdatalist-search_datalist=&locale=pt-BR&page=1000000&search=34635368000148&search_datalist=&search_sacc=&sort_column=integration_contracts_contracts.descricao_nome_credor&sort_direction=asc&tipo_objeto=+&__=__

# a[href*= "/portal-da-transparencia/contratos/contratos?cod_concedente=+&cod_gestora=+&data_assinatura=&data_vigencia=&decricao_modalidade=+&descricao_situacao=+&locale=pt-BR&page=10&search=34635368000148&search_datalist=&search_sacc=&sort_column=&sort_direction=&tipo_objeto=+"]

# <a data-remote="true" href="/portal-da-transparencia/contratos/contratos?cod_concedente=+&amp;" \
# "cod_gestora=+&amp;data_assinatura=&amp;data_vigencia=&amp;decricao_modalidade=+&amp;descricao_situacao=+&" \
# "amp;locale=pt-BR&amp;page=10&amp;search=34635368000148&amp;search_datalist=&amp;search_sacc=&amp;" \
# "sort_column=integration_contracts_contracts.descricao_nome_credor&amp;sort_direction=asc&amp;tipo_objeto=+"
# >Última</a>

#
# requisicao = requests.get(url)
# site = BeautifulSoup(requisicao.Response(), 'html.parser')
# # print(site.prettify())
#
# print(site.find('span class="last"'))