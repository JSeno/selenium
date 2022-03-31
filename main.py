""" Importando o módulo webdriver da biblioteca selenium """
from selenium import webdriver

""" Importando o módulo keys da biblioteca selenium """
from selenium.webdriver.common.keys import Keys

"""  Criando uma instancia do navegador que usarei que no caso é o Google Chrome """
driver = webdriver.Chrome(executable_path=r"E:\Webdriver\chromedriver.exe") # Caminho do driver

""" Abrindo a página do navegador"""
driver.get("https://devisp.datacake.com.br")

""" Definindo um tempo de espera para o navegador carregar a página """
driver.implicitly_wait(5) # Tempo de espera marcado para 5 segundos.

""" Maximizando a tela """
driver.maximize_window()

