#input() Cheque / .format() Cheque / if, else e elif Cheque / loop for Cheque +- / loop while Cheque
#Bibliotecas / fuçoes

from selenium import webdriver
import time
import pandas as pd
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

nav = webdriver.Chrome()
nav.get("https://fast.com/pt/")
wait = WebDriverWait(nav, 60)
wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="show-more-details-link"]'))).click()
time.sleep(2)
dowl = nav.find_element("xpath", '//*[@id="speed-value"]').text
time.sleep(40)
upl = nav.find_element("xpath", '//*[@id="upload-value"]').text
lateNC = nav.find_element("xpath", '//*[@id="latency-value"]').text
lateC = nav.find_element("xpath", '//*[@id="bufferbloat-value"]').text
print("A rede que vc esta conectada tem:\n{0} de Dowload\n{1} de Upload\n{2} de Latencia carregada\n{3} de Latencia não carregada".format(dowl, upl, lateC, lateNC))

# i = int(input("Ate qual numero vc quer que eu conte?\n"))
# n = int(0)
# y = bool
# while i > n:
#     if i > 10:
#         print("Eu não sei contar mais que onze")
#         y = False
#         break
#     else:
#         print("Numero {}".format(n))
#         y = True
#     n = n + 1
#     if y == False:
#         print("Preciso estudar")
#     else:
#         print("Acabou")