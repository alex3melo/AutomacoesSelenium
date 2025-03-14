# selenium 4
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from time import sleep
import random

import pyautogui

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

def moverNaTela(elemento):

    pyautogui.moveTo(x=elemento.location["x"],y=elemento.location["y"])
    sleep(1)
    pyautogui.click()
    pyautogui.moveTo(x=elemento.location["x"]+30,y=elemento.location["y"]+155, duration=1)
    pyautogui.click()
    pyautogui.moveTo(x=elemento.location["x"]+32,y=elemento.location["y"]+160, duration=1)

    pyautogui.moveTo(x=elemento.location["x"]+32,y=elemento.location["y"]+350, duration=1)

    pyautogui.moveTo(x=elemento.location["x"]+330,y=elemento.location["y"]+350, duration=1)

    pyautogui.moveTo(x=elemento.location["x"]+330,y=elemento.location["y"]+500, duration=1)
    sleep(1)
    pyautogui.click()


driver = iniciar_driver()
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

if link_tiss is not None:
    print('link encontrado')
    print(f'loca: {link_tiss.location}')

"""action = ActionChains(driver)
action.move_to_element_with_offset(link_tiss,2,2)
action.perform()
action.double_click(link_tiss)
action.perform()"""

moverNaTela(link_tiss)

input('')
driver.close()