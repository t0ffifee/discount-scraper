from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument('--headless=new')
options.add_argument('user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36')
driver = webdriver.Chrome(options=options)
driver.get('https://www.jumbo.com/aanbiedingen/')


driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
wait = WebDriverWait(driver, 10)
elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//h3/a')))

for el in elements:
  print(el.text)

driver.quit()
