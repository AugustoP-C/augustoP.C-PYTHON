# s = "jj gg hh"
# s_list = s.split(" ")
# print(s_list)
# ss = s_list[0] + s_list[1]
# print(type(s))
# print(type(s_list))
# print(type(ss))
import re

# t = []
# t[0] = "oiiiiiii\n"
# t[1] = "doisssss\n"
# q = str(t)
# tt = re.sub(r'[\n]', '', q)
# print(tt)

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
nav = webdriver.Chrome()
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
print(propt)