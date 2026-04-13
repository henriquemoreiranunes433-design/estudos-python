from pathlib import Path
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Chrome Options
# https://peter.sh/experiments/chromium-command-line-switches/


CAMINHO_ATUAL = Path(__file__).parent

# 2. Se o seu chromedriver estiver em uma pasta 'drivers' 
# que está no MESMO NÍVEL do seu script:
CHROME_DRIVER_PATH = CAMINHO_ATUAL / 'drivers' / 'chromedriver.exe'


def make_chrome_browser(*options: str) -> webdriver.Chrome:
    # 1. Configura as Opções (Options)
    chrome_options = webdriver.ChromeOptions()

    if options:
        for option in options:
            chrome_options.add_argument(option)

    # Adicionando proteções contra detecção de robô
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")

    # 2. Configura o Serviço (Service) - Definindo a variável aqui!
    chrome_service = Service(
        executable_path=str(CHROME_DRIVER_PATH),
    )

    # 3. Cria o Navegador (Browser) - Usando as variáveis acima
    browser = webdriver.Chrome(
        service=chrome_service, # Agora ela está definida logo acima
        options=chrome_options
    )

    # 4. Comando extra para limpar o rastro do WebDriver via JavaScript
    browser.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    return browser


if __name__ == '__main__':
    TIME_TO_WAIT = 10
    # Example
    # options = '--headless', '--disable-gpu',
    options = ()
    browser = make_chrome_browser(*options)

    # Como antes
    browser.get('https://www.google.com.br')

    #espere para encotrar o imput
    search_imput = WebDriverWait(browser, TIME_TO_WAIT).until(
        EC.presence_of_element_located(
                (By.NAME, 'q')
        )      
    )
    search_imput.send_keys('youtube')
    search_imput.send_keys(Keys.ENTER)

    results = browser.find_element(By.ID, 'search')
    links = results.find_elements(By.TAG_NAME, 'a')
    links[0].click()
    youtube_search = WebDriverWait(browser, TIME_TO_WAIT).until(
    EC.presence_of_element_located(
        (By.NAME, 'search_query')
    )
)
# 2. Digitar o que você quer procurar
    youtube_search.send_keys('racionais')

    # 3. Dar Enter
    youtube_search.send_keys(Keys.ENTER)

    titulo_video = "A vida É Desafio - Nada Como Um Dia Após O Outro Dia (Chora Agora)"

    video = WebDriverWait(browser,30).until(
        EC.element_to_be_clickable((By.XPATH, f"//a[@id='video-title' and contains(@title, '{titulo_video}')]"))
    )
    video.click()

        

        

        # Dorme por 10 segundos
    sleep(TIME_TO_WAIT)