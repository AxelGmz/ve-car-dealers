from time import sleep
import lxml.html as html
import requests
from targets import list_of_accounts
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


HOME_URL='https://www.instagram.com/'

XPATH_POST_LINK='//a[@class="qi72231t nu7423ey n3hqoq4p r86q59rh b3qcqh3k fq87ekyn bdao358l fsf7x5fv rse6dlih s5oniofx m8h3af8h l7ghb35v kjdc1dyq kmwttqpk srn514ro oxkhqvkx rl78xhln nch0832m cr00lzj9 rn8ck1ys s3jn8y49 icdlwmnq _a6hd" and starts-with(@href, "/p/")]/@href'
XPATH_DESCRIPTION='//span[@class="_aacl _aaco _aacu _aacx _aad7 _aade"]/text()'


def fullcarro_scrapper():
  try:
    for account in list_of_accounts:
      DRIVER_PATH = '.\edgedriver_win64\msedgedriver'
      driver = webdriver.Edge(executable_path=DRIVER_PATH)
      result = driver.get(f'{HOME_URL}{account}')
      try:
          element = WebDriverWait(driver, 10).until(
              EC.presence_of_element_located((By.CLASS_NAME, "_aagw"))
          )
          # cars = driver.find_elements(By.XPATH,'//div[@class="_aagw"]')
          cars = driver.find_elements(By.XPATH,'//img[contains(@alt,"Precio")]')
          print('/////////////////')
          for car in cars:
            print(car.get_attribute("alt"))
            print('/////////////////')
      finally:
          driver.quit()
      
  except Exception as err:
    print(f'Ocurrio un error {err}')



if __name__ == "__main__":
  fullcarro_scrapper()