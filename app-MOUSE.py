from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

def iniciar_driver():
    chrome_options = Options()
    # Fonte de opções de switches https://peter.sh/experiments/chromium-command-line-switches/

    arguments = ['--lang=pt-BR', '--window-size=800,600',
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

driver = iniciar_driver()
driver.get('https://cursoautomacao.netlify.app/exemplo_chains')

# ActionChains(sequencia de passos)
botao = driver.find_element(By.ID, 'botao-direito')
chain = ActionChains(driver)
chain.context_click(botao).pause(3).send_keys(Keys.DOWN).pause(3).send_keys(
    Keys.DOWN).pause(3).send_keys(Keys.DOWN).pause(3).click().perform()

driver.get('https://cursoautomacao.netlify.com/')
window_10_radio_button = driver.find_element(By.ID, 'WindowsRadioButton')
chain2 = ActionChains(driver)
chain2.click(window_10_radio_button).pause(3).send_keys(
    Keys.DOWN).pause(3).send_keys(Keys.UP).click().perform()
input('')
driver.close()