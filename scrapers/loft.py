from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webelement import WebElement
import time

class LoftScraper:
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
    self.logger_forall.log('STARTING LOFT')
    try:
      self.driver.get("https://www.loft.co.jp/news/")
      array_result = self.__process()
    except LinkCannotProcessException as e:
      self.logger_forall.log(f"FAILED Caught an exception: {e}")
      self.logger_exc.log(f"An exception occurred in LOFT: {e}")
      return { "is_success": False, "data": None }
    else:
      self.logger_forall.log('SUCCESS ENDING LOFT')
      self.logger_nonexc.log(f'No exception occurred in LOFT)')
      return { "is_success": True, "data": array_result }
      
  def close(self):
    self.driver.quit()

  def __process(self):
    try:
      link_tag = self.__find_element(self.driver, By.XPATH, '//*[@id="content-box"]/div/ul/li[1]/a', None, 10, 5, "a tag")
    except TimeoutException as e:
      raise LinkCannotProcessException(f"Cannot find element error: {e.msg}")

    new_link = link_tag.get_attribute('href')
    self.driver.get(new_link)

    try:
      time.sleep(5)
      h1_tag = self.__find_element(self.driver, By.XPATH, '//*[@id="wapper-innercontents"]/div/div[1]/div[1]/div', None, 10, 5, "h2 tag")
    except TimeoutException as e:
      raise LinkCannotProcessException(f"Cannot find element error: {e.msg}")

    try:
      image_tag = self.__find_element(self.driver, By.XPATH, '//*[@id="wapper-innercontents"]/div/div[1]/figure/img', None, 10, 5, "image tag")
    except TimeoutException as e:
      raise LinkCannotProcessException(f"Cannot find element error: {e.msg}")

    try:
      text_tag = self.__find_element(self.driver, By.XPATH, '//*[@id="content-box"]/div', None, 10, 5, "text tag")
    except TimeoutException as e:
      raise LinkCannotProcessException(f"Cannot find element error: {e.msg}")

    h1_text = h1_tag.text
    texts = self.__extract_text(text_tag).strip()
    image_link = image_tag.get_attribute('src')

    images = []
    images.append(image_link)
    
    return { "description": texts, "site_url": new_link, "images": images, "title": h1_text }

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
    """Extracts the text from an element excluding <a> and <button> tags."""
    text = element.get_attribute("textContent").strip()
    inner_tags = element.find_elements(By.XPATH, ".//a | .//button")
    for tag in inner_tags:
      text = text.replace(tag.get_attribute("textContent").strip(), "")
    return text


class LinkCannotProcessException(Exception):
  pass

# if __name__ == '__main__':
#   info_logger = Logger('info')
#   failed_logger = Logger('failed')
#   success_logger = Logger('success')

#   scraper = LoftScraper(failed_logger, success_logger, info_logger, False, False)
#   print(scraper.start())
#   scraper.close()