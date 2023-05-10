from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless") # não abre o navegador

driver = webdriver.Chrome(options=chrome_options) # abre o navegador
driver.get("https://www.google.com.br") # acessa o site
print("Abriu o ", driver.title) # imprime o título da página
driver.quit() # fecha o navegador