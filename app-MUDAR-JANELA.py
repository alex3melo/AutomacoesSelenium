from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep

def iniciar_driver():
    chrome_options = Options()
    # Fonte de opções de switches https://peter.sh/experiments/chromium-command-line-switches/

    arguments = ['--lang=pt-BR', '--window-size=1000,900',
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
sleep(1)

janela_inicial = driver.current_window_handle
print(janela_inicial)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(1)

botao_janela = driver.find_element(By.XPATH, '//button[@onclick="abrirJanelaDesafio()"]')
driver.execute_script('arguments[0].click()', botao_janela)
sleep(1)

janelas = driver.window_handles
print(janelas)
for janela in janelas:
    if janela not in janela_inicial:
        #mudar janela 
        print(janela)
        driver.switch_to.window(janela)
        sleep(1)
        campo_texto = driver.find_element(By.XPATH, '//textarea[@id="opiniao_sobre_curso"]')
        #campo_texto.click()
        campo_texto.send_keys('desafio')
        sleep(1)
        botao_pesquisar = driver.find_element(By.XPATH, '//button[@id="fazer_pesquisa"]')
        botao_pesquisar.click
        sleep(3)
        driver.close()

driver.switch_to.window(janela_inicial)

campo_texto_final = driver.find_element(By.XPATH, '//textarea[@id="campo_desafio7"]')
campo_texto_final.click()
campo_texto_final.send_keys('Finalizado!')

input('')
driver.close()