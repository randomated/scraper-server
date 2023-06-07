import os

def convert_to_camelcase(string):
  words = string.split('_')
  capitalized_words = [word.capitalize() for word in words]
  return ''.join(capitalized_words)

def generate_text_code(title, link, h1_tag, link_tag, image_tag, text_tag):
  scraper_title = convert_to_camelcase(title)
  text = f"""from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webelement import WebElement
import time
# from logger import Logger

class {scraper_title}Scraper:
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
    self.logger_forall.log('STARTING {scraper_title}')
    try:
      self.driver.get("{link}")
      array_result = self.__process()
    except LinkCannotProcessException as e:
      self.logger_forall.log(f\"FAILED Caught an exception: {{e}}")
      self.logger_exc.log(f"An exception occurred in {scraper_title}: {{e}}")
      return {{ "is_success": False, "data": None }}
    else:
      self.logger_forall.log('SUCCESS ENDING {scraper_title}')
      self.logger_nonexc.log(f'No exception occurred in {scraper_title})')
      return {{ "is_success": True, "data": array_result }}
      
  def close(self):
    self.driver.quit()

  def __process(self):
    time.sleep(10)
    try:
      link_tag = self.__find_element(self.driver, By.XPATH, '{link_tag}', None, 10, 5, "a tag")
    except TimeoutException as e:
      raise LinkCannotProcessException(f"Cannot find element error: {{e.msg}}")

    try:
      image_tag = self.__find_element(self.driver, By.XPATH, '{image_tag}', None, 10, 5, "image tag")
    except TimeoutException as e:
      raise LinkCannotProcessException(f"Cannot find element error: {{e.msg}}")

    try:
      text_tag = self.__find_element(self.driver, By.XPATH, '{text_tag}', None, 10, 5, "text tag")
    except TimeoutException as e:
      raise LinkCannotProcessException(f"Cannot find element error: {{e.msg}}")

    new_link = link_tag.get_attribute('href')
    image_link = image_tag.get_attribute('src')
    texts = self.__extract_text(text_tag).strip()

    images = []
    images.append(image_link)
    
    return {{ "description": texts, "site_url": new_link, "images": images, "title": "{h1_tag}" }}

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
        self.logger_forall.log(f"Timed out waiting for element ({{i + 1}}/{{max_tries}}). (line {{code_line}})")
    raise TimeoutException(f"Element not found after {{max_tries}} tries. (line {{code_line}})")

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

#   scraper = {scraper_title}Scraper(failed_logger, success_logger, info_logger, False, False)
#   print(scraper.start())
#   scraper.close()
"""

  return text

if __name__ == '__main__':
  current_directory = os.path.dirname(os.path.realpath(__file__))

  lists = [
    ["goldsgym", "https://shop.adidas.jp/", "ニュース", "link", "image", "text"],
    ["shop_adidas", "https://shop.adidas.jp/", "//*[@id=\"__next\"]/div/div[1]/div[3]/main/div/div[4]/ul/li[1]/div/a/div[2]/h2", "//*[@id=\"__next\"]/div/div[1]/div[3]/main/div/div[4]/ul/li[1]/div/a", "//*[@id=\"__next\"]/div/div[1]/div[3]/main/div/div[4]/ul/li[1]/div/a/div[1]/img", "//*[@id=\"__next\"]/div/div[1]/div[3]/main/div/div[4]/ul/li[1]/div/a/div[3]/h3"],
    ["easyoga", "https://www.easyoga.jp/", "//*[@id=\"contents\"]/div/div[2]/div[1]/div/div/a[1]/div/p[3]", "//*[@id=\"contents\"]/div/div[2]/div[1]/div/div/a[1]", "//*[@id=\"contents\"]/div/div[2]/div[1]/div/div/a[1]/div/div[1]/img", "//*[@id=\"contents\"]/div/div[2]/div[1]/div/div/a[1]/div/p[4]"],
    ["store_descente_arena", "https://store.descente.co.jp/arena/", "FEATURE", "//*[@id=\"top_feature\"]/div/div[2]/div[1]/a", "//*[@id=\"top_feature\"]/div/div[2]/div[1]/a/div/div[1]/img", "//*[@id=\"top_feature\"]/div/div[2]/div[1]/a/div/div[2]/h3"],
    ["store_descente_descente", "https://store.descente.co.jp/descente/", "FEATURE", "//*[@id=\"main_area\"]/div[1]/div/div[2]/div[1]/a", "//*[@id=\"main_area\"]/div[1]/div/div[2]/div[1]/a/div[1]/div/img", "//*[@id=\"main_area\"]/div[1]/div/div[2]/div[1]/a/div[2]/p"],
    ["mugendai_yoshimoto", "https://mugendai.yoshimoto.co.jp/", "TOPICS", "/html/body/main/div[4]/div/ul/li[1]/a", "/html/body/main/div[4]/div/ul/li[1]/a/div/div", "/html/body/main/div[4]/div/ul/li[1]/a/span[2]"],
    ["village_v", "https://www.village-v.co.jp/", "イベント情報", "/html/body/main/div[4]/div[2]/section/div[2]/div/div/div[1]/div[1]/p/a", "/html/body/main/div[4]/div[2]/section/div[2]/div/div/div[1]/div[1]/p/a", "/html/body/main/div[4]/div[2]/section/div[2]/div/div/div[1]/div[2]/p[1]/a"],
    ["store_descente_descente_golf", "https://store.descente.co.jp/descentegolf/ext/news/", "/html/body/div[2]/dvi/div[2]/div/main/article/section[1]/div/ul/li[1]/a/div/h3", "/html/body/div[2]/dvi/div[2]/div/main/article/section[1]/div/ul/li[1]/a", "/html/body/div[2]/dvi/div[2]/div/main/article/section[1]/div/ul/li[1]/a/figure/picture/img", "/html/body/div[2]/dvi/div[2]/div/main/article/section[1]/div/ul/li[1]/a/div/p"]
  ] 

  scrapers_list = { "scrape_list": [] }

  for sublist in lists:
    title = sublist[0]
    link = sublist[1]
    h1_tag = sublist[2]
    link_tag = sublist[3]
    image_tag = sublist[4]
    text_tag = sublist[5]

    scraper_title = convert_to_camelcase(title)
    print(f"from code_generated.{title} import {scraper_title}Scraper")
    print(f"\"{title}\": {scraper_title}Scraper")
    
    scrapers_list["scrape_list"].append({"stores": [{"store_name": "SAMPLE", "wls_id": 563},], "type": title})

    with open(os.path.join(current_directory, "code_generated", f"{title}.py"), "w") as file:
      file.write(generate_text_code(title, link, h1_tag, link_tag, image_tag, text_tag))

  print(scrapers_list)



























