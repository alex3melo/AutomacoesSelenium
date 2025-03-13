# selenium 4
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
import random

campo_texto = None

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
driver.get('https://cursoautomacao.netlify.app/desafios')
driver.maximize_window()
sleep(2)

driver.execute_script("window.scrollTo(0, 1000)")
sleep(2)

#campo_texto = driver.find_element(By.XPATH, '//textarea[@id="campoparagrafo"]')
campo_texto = driver.find_element(By.ID, 'campoparagrafo')
"""
if campo_texto is not None:
    print("Campo encontrado")
"""
def digitar_naturalmente(texto, elemento):
    for letra in texto:
        elemento.send_keys(letra)
        sleep(random.randint(1, 5)/30)

texto = 'Aqui recomendo que você sempre tenha essa história pronta para contar de uma forma que saliente o seu interesse por a área. Isso porque caso você realmente esteja interessado na vaga, desta maneira você irá mostrar a quem estiver te analisando que você tem uma grande probabilidade de ser um profissional mais engajado com as tarefas da empresa. Capriche nessa história.Muitos aqui iram dizer coisas como: porque vocês são uma ótima empresa, porque todos falam bem de você. Mas alerto: seja autêntico na sua resposta  as empresas querem aqui saber se você pesquisou sobre a empresa e como o seu skillset (seu conhecimento) pode agregar para a empresa, então use essa oportunidade para falar como a EMPRESA vai ganhar contratando você. Não diga coisas como: sempre foi meu sonho trabalhar aqui! As empresas não ganham nada com seu sonho de querer trabalhar lá (triste, mas é a realidade), então mostre o que você tem de melhor para ajudar a empresa crescer. No meu caso a resposta que dei foi a seguinte: “Amo aprender e ensinar e estou constantemente me atualizando, além de gostar muito de ensinar e aprender com os outros integrantes da equipe, percebi que vocês em uma cultura internacional e isso me chamou muita atenção, seria ótimo poder trabalhar com vocês!'
digitar_naturalmente(texto,campo_texto)

input('')
driver.close()