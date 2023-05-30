from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

nav = webdriver.Chrome()

nav.get("https://fast.com/pt/")
WebDriverWait(nav, 30).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="show-more-details-link"]'))).click()
time.sleep(40)
dowload = nav.find_element(By.XPATH, '//*[@id="speed-value"]')
upload = nav.find_element(By.XPATH, '//*[@id="upload-value"]')
lCarregada = nav.find_element(By.XPATH, '//*[@id="bufferbloat-value"]')
lNCarregada = nav.find_element(By.XPATH, '//*[@id="latency-value"]')
print("A velocidade de Dowload e de: " + dowload.text)
print("A velocidade de Upload e de: " + upload.text)
print("A velocidade de Latencia Cerregada e de: " + lCarregada.text)
print("A velocidade de Latencia não Cerregada e de: " + lNCarregada.text)