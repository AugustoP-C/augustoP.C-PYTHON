from selenium import webdriver
from selenium.webdriver import ActionChains
import time

nav = webdriver.Chrome()
nav.get("https://www.youtube.com/watch?v=4cRRIB1SrHc&ab_channel=MissPazzissima")
nav.find_element("xpath", '//*[@id="movie_player"]/div[27]/div[2]/div[1]/button').click()
ActionChains(nav).send_keys("f").perform()
time.sleep(20)