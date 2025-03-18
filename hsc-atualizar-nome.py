from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep
import random

UserUNI = ''
Passw = ''

def iniciar_driver():
    chrome_options = Options()
    # Fonte de opções de switches https://peter.sh/experiments/chromium-command-line-switches/

    arguments = ['--lang=pt-BR', '--window-size=1000,1000',
                '--incognito']
    ''' Common arguments
    --start-maximized # Inicia maximizado
    --lang=pt-BR # Define o idioma de inicialização, # en-us , pt-BR
    --incognito # Usar o modo anônimo
    --window-size=800,800 # Define a resolução da janela em largura e altura
    --headless # Roda em segundo plano(com a janela fechada)
    --disable-notifications # Desabilita notificações
    --disable-gpu # Desabilita renderização com GPU
    '''
    for argument in arguments:
        chrome_options.add_argument(argument)

    caminho_padrao_para_download = 'E:\\Storage\\Desktop'

    # Lista de opções experimentais(nem todas estão documentadas) https://chromium.googlesource.com/chromium/src/+/32352ad08ee673a4d43e8593ce988b224f6482d3/chrome/common/pref_names.cc
    chrome_options.add_experimental_option("prefs", {
        'download.default_directory': caminho_padrao_para_download,
        # Atualiza diretório para diretório passado acima
        'download.directory_upgrade': True,
        # Setar se o navegar deve pedir ou não para fazer download
        'download.prompt_for_download': False,
        "profile.default_content_setting_values.notifications": 2,  # Desabilita notificações
        # Permite realizar múltiplos downlaods multiple downloads
        "profile.default_content_setting_values.automatic_downloads": 1,
    })

    driver = webdriver.Chrome(options=chrome_options)
    return driver

def digitar_naturalmente(texto, elemento):
    for letra in texto:
        elemento.send_keys(letra)
        sleep(random.randint(1, 5)/30)

driver = iniciar_driver()
action = ActionChains(driver)

driver.get('https://unimedcerrado.topsaude.com.br/PortalCredenciado/')
driver.maximize_window()
sleep(2)

usuario = driver.find_element(By.XPATH, '//input[@id="usuario"]')
digitar_naturalmente(UserUNI,usuario)

sleep(2)
senha = driver.find_element(By.XPATH, '//input[@id="senha"]')
digitar_naturalmente(Passw,senha)

sleep(1)
entrar = driver.find_element(By.XPATH, '//input[@id="login-submit"]')
entrar.click()

sleep(5)
aviso = driver.find_element(By.CLASS_NAME, 'btn.btn-primary')
aviso.click()

sleep(2)
link_tiss = driver.find_element(By.XPATH, '//a[@href="#PORCRED50"]')

action.move_to_element_with_offset(link_tiss,2,2)
action.perform()

link_tiss.send_keys(Keys.ENTER)

sleep(1)
link_digtiss = driver.find_element(By.XPATH, '//a[@href="#PORCRED50.5"]')

action.move_to_element_with_offset(link_digtiss,2,2)
action.perform()
sleep(1)
link_digtiss.send_keys(Keys.TAB)

sleep(1)
link_LoteFat = driver.find_element(By.XPATH, '//a[@data-href="/PortalCredenciado/HomePortalCredenciado/DigitacaoTiss/LoteFaturamento?tituloFuncao=Lote de Faturamento"]')
action.move_to_element_with_offset(link_LoteFat,2,2)
action.perform()

sleep(1)
action.click(link_LoteFat)
action.perform()

paciente = None
sleep(10)

# Encontrar a iframe
iframe = driver.find_element(By.XPATH, "//iframe[@src='/PortalCredenciado/HomePortalCredenciado/DigitacaoTiss/LoteFaturamento?tituloFuncao=Lote de Faturamento']")
# Mudar para dentro da iframe
driver.switch_to.frame(iframe)

#elementos = driver.find_elements(By.XPATH, '//table[@id="TabContainerRemessa_TPNovaRemessa_gridBuscaRemessa"]//tbody/tr[1]/th')

tabelahtml = driver.find_element(By.XPATH, '//table[@id="TabContainerRemessa_TPNovaRemessa_gridBuscaRemessa"]')

htmlcontent = tabelahtml.get_attribute("outerHTML")

soup = BeautifulSoup(htmlcontent, "html.parser")

tabela = soup.find(nome="tabela")
print(tabela)
df = pd.read_html(str(tabela))[0]

df.to_csv("tabela.csv", encoding="UTF-8", sep=";", index=False)

input('')
driver.close()