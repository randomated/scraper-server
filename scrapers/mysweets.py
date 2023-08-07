from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webelement import WebElement
import time
# from logger import Logger

class MySweetsScraper:
  def __init__(self, logger_exc, logger_nonexc, logger_forall, is_headless=True, is_chrome=True):
    # create a logger for exceptions
    self.logger_exc = logger_exc
    self.logger_nonexc = logger_nonexc
    self.logger_forall = logger_forall

    if is_chrome:
      options = ChromeOptions()
      options.add_argument('--incognito')
      
      if is_headless:
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
      
      self.driver = webdriver.Chrome(options=options)
    else:
      options = FirefoxOptions()
      options.add_argument('-private')
            
      if is_headless:
          options.add_argument('-headless')
          options.add_argument('-no-sandbox')
          options.add_argument('-disable-dev-shm-usage')

      self.driver = webdriver.Firefox(options=options)

  def start(self):
    self.logger_forall.log('STARTING MySweets')
    try:
      self.driver.get("https://mysweets.jp/")
      array_result = self.__process()
    except LinkCannotProcessException as e:
      self.logger_forall.log(f"FAILED Caught an exception: {e}")
      self.logger_exc.log(f"An exception occurred in MySweets: {e}")
      return { "is_success": False, "data": None }
    else:
      self.logger_forall.log('SUCCESS ENDING MySweets')
      self.logger_nonexc.log(f'No exception occurred in MySweets)')
      return { "is_success": True, "data": array_result }
      
  def close(self):
    self.driver.quit()

  def __process(self):
    time.sleep(10)
    array_result = []
    try:
      div_tag = self.__find_element(self.driver, By.XPATH, './/*[@id="top"]/main/section/div/div', None, 10, 5, "div tag")
      article_elements = div_tag.find_elements(By.XPATH, ".//article")
      for article_element in article_elements:
        images = []

        article_id = article_element.get_attribute('id')

        shop_name1 = article_element.find_element(By.XPATH, './/div[2]/p[1]')
        shop_name2 = article_element.find_element(By.XPATH, './/div[2]/h4')

        image_tag = article_element.find_element(By.XPATH, './/div[1]/img')
        image_link = image_tag.get_attribute('src')
        images.append(image_link)

        text_tag1 = article_element.find_element(By.XPATH, './/div[2]/p[2]')
        text_tag2 = article_element.find_element(By.XPATH, './/div[2]/div[2]')

        link_tag = article_element.find_element(By.XPATH, './/div[2]/div[3]/a[2]')
        new_link = link_tag.get_attribute('href')

        array_result.append({ "title": f"{shop_name1.text}\n{shop_name2.text}", "images": images, "description": f"{text_tag1.text}\n{text_tag2.text}\n\n今後出店のお店は詳細ページからご確認ください", "site_url": "https://mysweets.jp/#{article_id}" })

    except TimeoutException as e:
      raise LinkCannotProcessException(f"Cannot find element error: {e.msg}")
    else:
      return array_result

  def __find_element(self, driver, locator_type, locator, parent_element=None, timeout=10, max_tries=5, code_line=""):
    for i in range(max_tries):
      try:
        if parent_element is None:
          element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((locator_type, locator))
          )
          return element
        else:
          element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((locator_type, locator)), parent_element
          )
          return element
      except TimeoutException:
        self.logger_forall.log(f"Timed out waiting for element ({i + 1}/{max_tries}). (line {code_line})")
    raise TimeoutException(f"Element not found after {max_tries} tries. (line {code_line})")

  def __extract_text(self, element: WebElement) -> str:
    text = element.get_attribute("textContent").strip()
    inner_tags = element.find_elements(By.XPATH, ".//a | .//button")
    for tag in inner_tags:
      text = text.replace(tag.get_attribute("textContent").strip(), "")
    return text


class LinkCannotProcessException(Exception):
  pass

# if __name__ == '__main__':
#   current_directory = "/Users/argiebacomo/Desktop/python_stuffs/scraper-server"
#   info_logger = Logger('info', current_directory)
#   failed_logger = Logger('failed', current_directory)
#   success_logger = Logger('success', current_directory)

#   scraper = MySweetsScraper(failed_logger, success_logger, info_logger, False, False)

#   print(scraper.start())
#   scraper.close()
