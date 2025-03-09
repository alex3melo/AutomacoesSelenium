from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

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

titulo = driver.find_element(By.XPATH, '//*[text()="ZONA DE TESTES"]')
titulo2 = driver.find_element(By.XPATH, '//h1[text()="ZONA DE TESTES"]')
texto = driver.find_element(By.XPATH, '//div[@id="select-class-example"]//fieldset/h4')


if titulo:
    print(f'Titulo {titulo.text} Encontrato')

input('')
driver.close()
'''
# Como montar um XPATH
# De forma geral você vai montar um xpath da seguinte forma
//tag[@atributo="valor"]

# Ultra genérico(engloba todas tags da página)
//* 

# Ultra genérico + tag
//*[tag]

# apenas contem um parte do texto
//*[contains(text(),"Exemplo")] 
//*[contains(text(),"Exemplo") or contains( text(), "Dropdown" )]
//*[contains(text(),'Dropdown') and  contains(text(),'Bootstrap') ]

# Inicia com um texto
//*[starts-with(text(),"Exemplo")]
//*[starts-with(@class,"btn")]

# Buscando apenas por um texto spefícico
//*[text()="Exemplo Checkbox"] # Genérico, porém especificando o texto
//h4[text()="Exemplo Checkbox"] # Com tag e especificando o texto

# Buscando por um elemento específico usando tag e propriedade
//button[@id="dropdownMenuButton"] # tag com propriedade e valor
//section[@class="jumbotron"] # tag com propriedade e valor
//div[@class="form-check"] #tag com propriedade e valor

# Como encontrar filhos de cada elemento
# Encontra único filho
//div/fieldset
//div/fieldset/h4
# Encontrar filho, quando há multiplos filhos
# Find child when multiple elements
//thead/tr//th[2]
'''