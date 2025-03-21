from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep

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
driver.get('https://cursoautomacao.netlify.app/')

# Situação 1 - Fechar alerta
# descer a página até elementos estarem visíveis
sleep(2)
driver.execute_script('window.scrollTo(0,250)')
sleep(2)
# digitar meu nome
campo_nome = driver.find_element(By.ID, "nome")
sleep(1)
campo_nome.send_keys('jhonatan')
sleep(1)
botao_alerta = driver.find_element(By.ID, "buttonalerta")
sleep(2)
# clicar em alerta
botao_alerta.click()
sleep(2)
# clicar em ok para fechar alerta
alerta1 = driver.switch_to.alert
sleep(2)
alerta1.accept()
sleep(5)


# Situação 2 - Confirmar ou cancelar alerta
# encontrar o campo confirmar
sleep(2)
botao_confirmar = driver.find_element(By.ID, "buttonconfirmar")
# clicar no campo de confirmar
botao_confirmar.click()
sleep(2)
# Clicar em ok ou cancelar
alerta2 = driver.switch_to.alert
sleep(2)
# confirmar
alerta2.accept()
# cancelar
# alerta2.dismiss()

# Situação 3 - Inserir dados em  alerta e depois confirmar ou cancelar esses dados, além de fechar a alerta posterior
# encontrar o campo fazer pergunta
sleep(1)
botao_pergunta = driver.find_element(By.ID, "botaoPrompt")
sleep(1)
botao_pergunta.click()
# digitar algo dentro da alerta
alerta3 = driver.switch_to.alert
sleep(1)
alerta3.send_keys('jhonatan')
sleep(2)
# clicar em confirmar (ou cancelar)
alerta3.accept()
sleep(2)
# fechar a janela posterior
alerta3.dismiss()
input('')
driver.close()
