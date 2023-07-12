# cnpj para testes: 07385282000131 https://portaldatransparencia.gov.br/pessoa-juridica/busca/lista?termo=07385282000131&pagina=1&tamanhoPagina=10&

#imports
from selenium import webdriver
import time
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

nav = webdriver.Chrome()#NAVegador web

def portalT(cnpj): #fução para pegar o nome da empresa usando o cnpj
    # pegar somente os doi primeiros nomes ao entra no portal da tranparencia
    nav.get("https://www.portaltransparencia.gov.br/busca/pessoa-juridica/" + str(cnpj))
    dropdown_cnpjN = WebDriverWait(nav, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/main/div[2]/section[1]/div[2]/div[1]')))
    cnpjN = dropdown_cnpjN.find_element(By.TAG_NAME, 'span')
    n_list = cnpjN.text.split(" ")
    nEmpresarial = n_list[0] + "+" + n_list[1]
    return nEmpresarial

#entrando no saite de sobral e epgando os anos dispooniveis
nav.get("http://transparencia.sobral.ce.gov.br/contrato/ano_exercicio:")
WebDriverWait(nav, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="cookieConsentContainer"]/div[2]/a'))).click()
WebDriverWait(nav, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".input-field:nth-child(1) > .select-wrapper"))).click()
time.sleep(3)
dropdown_anos = WebDriverWait(nav, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/main/div/div[2]/div/div/div[1]/form/div[1]/div[1]/div/ul')))
anos = dropdown_anos.find_elements(By.TAG_NAME, 'li')
ano_list = []
for ano in anos:
    ano_list.append(ano.text)
del ano_list[0]
print(ano_list)

#entrado no saite de sobral e pegando todos os dados
portalTV = portalT("07385282000131")
print(portalTV)
nav.get("http://transparencia.sobral.ce.gov.br/contrato/ano_exercicio:" + str(ano) + "/fornecedor:" + portalTV)
for ano in ano_list:
    nav.get("http://transparencia.sobral.ce.gov.br/contrato/ano_exercicio:" + str(ano) + "/fornecedor:" + portalTV)
    try:
        tabela_div = WebDriverWait(nav, 3).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="mainDiv"]/div[3]/div/div/div/div[2]/div[2]'))) #'//*[@id="mainDiv"]/div[3]/div/div/div/div[2]/div[2]'
        if tabela_div:
            tabela_numero = WebDriverWait(nav, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="mainDiv"]/div[3]/div/div/div/div[2]/div[2]/table/tbody/tr/td[1]')))
            link_contatros = tabela_numero.find_element(By.TAG_NAME, 'a')
            # for link in links_contatros:
            # link.get_attribute('href')
            if link_contatros:
                link = link_contatros.get_attribute('href')
                print(link)
                nav.get(link)
                print(ano)
                # (Número) - (numero)
                numero = nav.find_element(By.XPATH, '//*[@id="mainDiv"]/div[2]/div[2]/div/div/div[3]/div[2]')
                print("numero: " + numero.text)
                # (Fornecedor CPF/CNPJ) - (cnpj_contratada)
                fornecedor = nav.find_element(By.XPATH, '//*[@id="mainDiv"]/div[2]/div[2]/div/div/div[10]/div[2]')
                print("fornecedor: " + fornecedor.text)
                # (Data Inicial) – (data_inicio_vigencia)
                dInicial = nav.find_element(By.XPATH, '//*[@id="mainDiv"]/div[2]/div[2]/div/div/div[7]/div[2]')
                print("data inicial: " + dInicial.text)
                # (Data Final) – (data_termino_vigencia)
                dFinal = nav.find_element(By.XPATH, '//*[@id="mainDiv"]/div[2]/div[2]/div/div/div[8]/div[2]')
                print("data final: " + dFinal.text)
                # (Valor inicial) – (valor_inicial)
                vInicial = nav.find_element(By.XPATH, '//*[@id="mainDiv"]/div[2]/div[2]/div/div/div[11]/div[2]')
                print("valor inicial" + vInicial.text)
                # (Secretaria) – (Órgão)
                secretaria = nav.find_element(By.XPATH, '//*[@id="mainDiv"]/div[2]/div[2]/div/div/div[1]/div[2]')
                print("secretaria : " + secretaria.text)
                # (Fornecedor) – (Nome Fornecedor)
                nFornecedor = nav.find_element(By.XPATH, '//*[@id="mainDiv"]/div[2]/div[2]/div/div/div[9]/div[2]/a')
                print("fornecedor: " + nFornecedor.text)
                # (Colocar na tabela manualmente “Estadual" – (Esfera)
                
                # (Colocar na tabela manualmente “Executivo” – (Poder)

                # (Colocar na tabela manualmente “Sobral” – (UF Órgão)

                # (Colocar na tabela manualmente “Sobral (CE)) contratos” – (Fonte)

    except TimeoutException:
        print("Contrato nao encontrado")
        print(tabela_div)
        pass
