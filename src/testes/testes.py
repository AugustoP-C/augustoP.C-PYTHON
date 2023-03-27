#input() Cheque
#.format() Cheque
#if, else e elif Cheque
#loop for Cheque +-
#loop while Cheque
#Bibliotecas
#fuçoes

from selenium import webdriver #https://fast.com/pt/
import time

i = int(input("Ate qual numero vc quer que eu conte?\n"))
n = int(0)
y = bool
while i > n :
    if i > 10:
        print("Eu não sei contar mais que onze")
        y = False
        break
    else:
        print("Numero {}".format(n))
        y = True
    n = n + 1
if y == False:
    print("Preciso estudar")
else:
    print("Acabou")