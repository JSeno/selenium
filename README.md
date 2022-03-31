#### Em construção...  🚧

# Automatização Selenium

## Download dos WEBDRIVERS

É uma ferramenta que serve para interagir com os browsers ao estar fazendo os testes automatizados.

- Chrome:  https://sites.google.com/chromium.org/driver/
- Firefox: https://github.com/mozilla/geckodriver/releases
- Edge:    https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/

## Datacake automatização de testes de assinatura.

### Versão 1.0 - 30/03/2022
### Instalação da biblioteca selenium no Python.

pip install selenium

### Importando o módulo webdriver do selenium no Python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#### Comandos uteis

 - O site que haverá a navegação
driver.get("https://www.seusite.com.br")

- Tempo de espera troque o 'tempo' pelos segundos de espera
driver.implicitly_wait(tempo)

- Comandos para janela
driver.maximize_window()
driver.minimize_window()

- Comando de busca dentro do navegador
sua_variavel = driver.find_element_by_id("Sua ID")
sua_variavel = driver.find_element_by_class("Sua Classe")
sua_variavel = driver.find_element_by_xpath("Sua Xpath")


- Comando para enviar dados no navegador
sua_variavel.send_keys("Teste de Assinatura")
sua_variavel.click()