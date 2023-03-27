import time
from selenium import webdriver
from selenium.webdriver import ActionChains

r = (input("Vamos comecar.\nVc esta pronto? (S/N)\n"))
if r == 'S' or r == 's':
    print("vamos comecar")
else:
    print("Volte depois então")
    exit()
print("Primeira questao.\nO que essa cabra diz")