""" Importando o módulo webdriver da biblioteca selenium """
from re import S
from selenium import webdriver

""" Importando o módulo keys da biblioteca selenium """
from selenium.webdriver.common.keys import Keys

""" Importando a Biblioteca PANDAS para caso necessário"""
import pandas as pd

"""  Criando uma instancia do navegador que usarei que no caso é o Google Chrome """
driver = webdriver.Chrome(executable_path=r"E:\Webdriver\chromedriver.exe") # Caminho do driver

""" Abrindo a página do navegador"""
driver.get("https://devisp.datacake.com.br")

""" Definindo um tempo de espera para o navegador carregar a página """
driver.implicitly_wait(5) # Tempo de espera marcado para 5 segundos.

""" Maximizando a tela """
driver.maximize_window()

""" Primeira Página do Assine"""

""" Buscando Campo CPF pelo ID"""
src_doc = driver.find_element_by_id("bfc_taxvat")

""" Digitando o CPF """
src_doc.send_keys("12345678909")

""" Buscando Campo Nome pelo ID"""
src_nome = driver.find_element_by_id("bfc_name")

""" Digitando o Nome """
src_nome.send_keys("Teste de Assinatura")

""" Buscando Campo Email pelo ID"""
src_email = driver.find_element_by_id("bfc_email")

""" Digitando o Email """
src_email.send_keys("testes@datacake.com.br")

""" Buscando Campo Telefone pelo ID"""
src_telefone = driver.find_element_by_id("mobile_celular")

""" Digitando o Telefone """
src_telefone.send_keys("(11) 99999-9999")

""""Buscando Campo CEP pelo ID"""
src_cep = driver.find_element_by_id("bfc_postalCode")

""" Digitando o CEP """
src_cep.send_keys("18680410")

""" Buscando campo número da casa pelo ID"""
src_numero = driver.find_element_by_id("bfc_numberOfAddress")

""" Digitando o número da casa """
src_numero.send_keys("410")

""" Buscando tipo de acesso pelo ID"""
src_acess = driver.find_element_by_id("bfc_typeOfAccess")

""" Digitando tipo de acesso pelo ID"""
src_acess.send_keys("Residencial")

""" Buscando tipo de cadastro pelo ID"""
src_cadastro = driver.find_element_by_id("bfc_typeOfCustomer")

""" Digitando tipo de cadastro pelo ID"""
src_cadastro.send_keys("Não sou cliente")

""" Buscando campo Disclaimer pelo ID"""
src_lgpd = driver.find_element_by_id("bfc_lgpd_disclaimer_label")

""" Digitando o Disclaimer """
src_lgpd.click()

""" Buscando campo Continuar pelo ID"""
src_continuar = driver.find_element_by_id("bfc_continuar")

""" Clicando no botão Continuar """
src_continuar.click()


""" Segunda Página do Assine"""

""" Buscando planos pela XPATH """
src_planos = driver.find_element_by_xpath('/html/body/wda-root/theme-providerfy/wda-providerfy-content-viewer[2]/plugin-provider-checkout/div/section/div[2]/div/plugin-provider-checkout-plans/div/div[1]/div[2]/div/div/plugin-provider-checkout-plan-internet/div/div/div/div[2]/div[2]/button/span')

""" Clicando no plano """
src_planos.click()

""" Adicionando tempo de espera para o navegador carregar a página """
driver.implicitly_wait(6) # Tempo de espera marcado para 8 segundos.

# Preciso descobrir o porquê do erro de não clicar no botão
""" Buscando campo Continuar Assinatura pelo ID"""
src_continuar_assinatura = driver.find_element_by_id('summary-continuar-assinatura')

""" Clicando no botão Continuar Assinatura """
src_continuar_assinatura.click()

