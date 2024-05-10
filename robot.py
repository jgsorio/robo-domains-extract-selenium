from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


print('Robot Initializing...')

driver = webdriver.Chrome()
driver.get('https://registro.br')


with open('./dominios.txt', 'r') as f:
    for line in f.readlines():
        pesquisa = driver.find_element(by='id', value='is-avail-field')
        pesquisa.clear() # Limpando a pesquisa
        pesquisa.send_keys(line)
        pesquisa.send_keys(Keys.RETURN)
        
        time.sleep(2)
        elements = driver.find_elements(by='tag name', value='strong')
        with open('./resultados.txt', 'a', encoding='utf-8') as f:
            
            f.write('Dominio ' + elements[1].text + ' Disponibilidade ' + elements[2].text + '\n')
            time.sleep(2)# dormindo


driver.close()