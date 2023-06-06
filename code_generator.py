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
    ["hands", "https://hands.net/", "トピックス", "//*[@id=\"modArticleThumbnailList\"]/ul[1]/li[1]/a", "//*[@id=\"modArticleThumbnailList\"]/ul[1]/li[1]/a/div[1]/img", "//*[@id=\"modArticleThumbnailList\"]/ul[1]/li[1]/a/div[2]/p"],
    ["withgreen", "https://withgreen.club/", "NEWS & TOPICS", "//*[@id=\"newsSlider\"]/div[1]/article[1]/a", "//*[@id=\"newsSlider\"]/div[1]/article[1]/figure/img", "//*[@id=\"newsSlider\"]/div[1]/article[1]/h3"],
    ["gu_global", "https://www.gu-global.com/jp/ja/feature/list/pc/", "特集一覧", "//*[@id=\"root\"]/div[7]/div/div/a[1]", "//*[@id=\"root\"]/div[7]/div/div/a[1]/div/div[1]/div/img", "//*[@id=\"root\"]/div[7]/div/div/a[1]/div/div[2]/p[2]"],
    ["nergy", "https://www.nergy.jp/", "NEWS", "//*[@id=\"list\"]/div[2]/div/article[1]/figure/div/a", "//*[@id=\"list\"]/div[2]/div/article[1]/figure/div/a/img", "//*[@id=\"list\"]/div[2]/div/article[1]/figure/figcaption/div[1]"],
    ["fighting_road", "https://www.fightingroad.co.jp/", "CAMPAIGN", "/html/body/div[1]/main/section[2]/div/ul/li[1]/a", "/html/body/div[1]/main/section[2]/div/ul/li[1]/a/div/img", "/html/body/div[1]/main/section[2]/div/ul/li[1]/a/p"],
    ["mizuno", "https://jpn.mizuno.com/campaign?did=dtctop_campaignlist", "イベント・キャンペーン一覧", "//*[@id=\"block-mizuno-theme-content\"]/article/div/div[2]/div/div/div[1]/ul/li[1]/a", "//*[@id=\"block-mizuno-theme-content\"]/article/div/div[2]/div/div/div[1]/ul/li[1]/a/picture/img", "//*[@id=\"block-mizuno-theme-content\"]/article/div/div[2]/div/div/div[1]/ul/li[1]/a/p"],
    ["two_foods", "https://2foods.jp/", "お知らせ", "//*[@id=\"contents\"]/div/section[8]/div[1]/div[1]/a", "//*[@id=\"contents\"]/div/section[8]/div[1]/div[1]/a/div/div[1]/div/img", "//*[@id=\"contents\"]/div/section[8]/div[1]/div[1]/a/div/div[2]/h2"],
    ["tokyu_hotels_cerulean_h", "https://www.tokyuhotels.co.jp/cerulean-h/restaurant/zabou/index.html", "おすすめレストランプラン", "//*[@id=\"main-content\"]/section/div[9]/div/div/div/div/div[2]/div/div/div/div/div[1]/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/a", "//*[@id=\"main-content\"]/section/div[9]/div/div/div/div/div[2]/div/div/div/div/div[1]/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/a/img", "//*[@id=\"main-content\"]/section/div[9]/div/div/div/div/div[2]/div/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/h6/a"],
    ["legian", "https://www.legian.jp/", "INFORMATION", "//*[@id=\"ajaxreload\"]/a[1]", "//*[@id=\"ajaxreload\"]/a[1]/dl/dt/picture/img", "//*[@id=\"ajaxreload\"]/a[1]/dl/dd/p"],
    ["tokyu_hotels_stream_e", "https://www.tokyuhotels.co.jp/stream-e/bar_dining/index.html", "おすすめレストランプラン", "//*[@id=\"main-content\"]/section/div[5]/div/div/div/div/div[2]/div/div/div/div/div[1]/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/a", "//*[@id=\"main-content\"]/section/div[5]/div/div/div/div/div[2]/div/div/div/div/div[1]/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/a/img", "//*[@id=\"main-content\"]/section/div[5]/div/div/div/div/div[2]/div/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/h6/a"],
    ["weare_lush", "https://weare.lush.com/jp/", "Must read", "/html/body/main/div[3]/div/div/div/div/div[6]/a", "/html/body/main/div[3]/div/div/div/div/div[6]/a/img", "/html/body/main/div[3]/div/div/div/div/div[6]/a/div/h4"],
    ["yogiway", "https://www.yogiway.jp/", "news", ".//div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/article/div/div[2]/a", ".//div[1]/div/div/div/div[2]/div/div/div[1]/div/div[1]/div/div/img", ".//div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/article/div/div[2]/a/div/div/p"],
    ["baycrews", "https://baycrews.jp/store/detail/0975", "ACME Furniture, JOURNAL STANDARD FURNITUREのブログ", "/html/body/main/article/div/aside[2]/ul/li[1]/a", "/html/body/main/article/div/aside[2]/ul/li[1]/a/div[1]/img", "/html/body/main/article/div/aside[2]/ul/li[1]/a/div[2]/div[1]"],
    ["bruno_online_shop", "https://bruno-onlineshop.com/", "Feature", "//*[@id=\"main\"]/div[3]/section[1]/ul/li[1]/a", "//*[@id=\"main\"]/div[3]/section[1]/ul/li[1]/a/img", "//*[@id=\"main\"]/div[3]/section[1]/ul/li[1]/a/p[2]"],
    ["shibuya_san", "https://shibuya-san.co.jp/", "Tourist Information", "//*[@id=\"exhibitions\"]/div[2]/div/a[1]", "//*[@id=\"exhibitions\"]/div[2]/div/a[1]/dl/dd/img", "//*[@id=\"exhibitions\"]/div[2]/div/a[1]/dl/dt/p[1]"],
    ["shoto_museum", "https://shoto-museum.jp/", "EXHIBITIONS 展覧会", "/html/body/div[1]/main/article/div[1]/div/div[1]/a", "/html/body/div[1]/main/article/div[1]/div/div[1]/a/div[1]/img", "/html/body/div[1]/main/article/div[1]/div/div[1]/a/div[2]/h4"],
    ["hikarie", "http://www.hikarie8.com/home.shtml", "NEWS", "//*[@id=\"contents\"]/section/article[2]/div/div[1]/h2/a", "//*[@id=\"contents\"]/section/article[2]/figure/a/img", "//*[@id=\"contents\"]/section/article[2]/div/div[1]/h2/a"],
    ["seria_group", "https://www.seria-group.com/", "おすすめ商品", "//*[@id=\"slider2\"]/li[4]/a", "//*[@id=\"slider2\"]/li[4]/a/span/span[1]/img", "//*[@id=\"slider2\"]/li[4]/a/span/span[2]"],
    ["akomeya", "https://www.akomeya.jp/shop/pc/0feature/", "季節の特集", "/html/body/div[1]/div[3]/div/main/div[1]/div[2]/dl[1]/dt/a", "/html/body/div[1]/div[3]/div/main/div[1]/div[2]/dl[1]/dt/a/figure/img", "/html/body/div[1]/div[3]/div/main/div[1]/div[2]/dl[1]/dd[2]/a"],
    ["gonpachi", "https://gonpachi.jp/news/", "NEWS", ".//div[1]/article[1]/div[1]/a", ".//div[1]/article[1]/div[1]/a/img", ".//div[1]/article[1]/h2/a"]
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



























