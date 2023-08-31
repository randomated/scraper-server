from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement
from datetime import datetime
import time
# from logger import Logger

class ShibuyaScrambleScraper:
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
    self.logger_forall.log('STARTING ShibuyaScramble')
    try:
      self.driver.get("https://www.shibuya-scramble-square.com/")
      array_result = self.__process()
    except LinkCannotProcessException as e:
      self.logger_forall.log(f"FAILED Caught an exception: {e}")
      self.logger_exc.log(f"An exception occurred in ShibuyaScramble: {e}")
      return { "is_success": False, "data": None }
    else:
      self.logger_forall.log('SUCCESS ENDING ShibuyaScramble')
      self.logger_nonexc.log(f'No exception occurred in ShibuyaScramble)')
      return { "is_success": True, "data": array_result }
      
  def close(self):
    self.driver.quit()

  def __process(self):
    time.sleep(5)
    self.driver.execute_script("window.scrollTo(0, 200);")

    try:
      button_tag = self.__find_element(self.driver, By.XPATH, './/*[@id="js-newsList-cats"]/div[1]/div[2]/a', None, 10, 5, "button tag")
      button_tag.click()
      self.driver.execute_script("window.scrollTo(0, 1000);")
    except TimeoutException as e:
      raise LinkCannotProcessException(f"Cannot find element error: {e.msg}")

    array_result = []
    try:
      ul_tag = self.__find_element(self.driver, By.XPATH, './/ul[@class="newsList3__list fade-stagger-parentHorizon js-newsList-list"]', None, 10, 5, "ul tag")
      ul_elements = ul_tag.find_elements(By.XPATH, ".//li")
      for ul_element in ul_elements:
        images = []

        time.sleep(5)
        modal_link = ul_element.find_element(By.XPATH, './/a')
        self.driver.execute_script("arguments[0].click();", modal_link)

        try:
          time.sleep(5)
          modal_tag = self.__find_element(self.driver, By.XPATH, './/div[@class="modaal-wrapper modaal-inline"]', None, 10, 5, "modal_tag tag")
        except TimeoutException as e:
          raise LinkCannotProcessException(f"Cannot find element error: {e.msg}")

        try:
          time.sleep(5)
          link_tag = modal_tag.find_element(By.XPATH, './/a[@class="js-news-linkUrl1"]')
          link = link_tag.get_attribute('href')
        except NoSuchElementException:
          try:
            close_modal_tag = self.__find_element(self.driver, By.XPATH, './/button[@class="modaal-close"]', None, 10, 5, "close_modal tag")
            self.driver.execute_script("arguments[0].click();", close_modal_tag)
          except TimeoutException as e:
            raise LinkCannotProcessException(f"Cannot find element error: {e.msg}")
          continue
        else:
          if link == "https://www.shibuya-scramble-square.com/#":
            try:
              close_modal_tag = self.__find_element(self.driver, By.XPATH, './/button[@class="modaal-close"]', None, 10, 5, "close_modal tag")
              self.driver.execute_script("arguments[0].click();", close_modal_tag)
            except TimeoutException as e:
              raise LinkCannotProcessException(f"Cannot find element error: {e.msg}")
            continue

        h1_tag = modal_tag.find_element(By.XPATH, './/div/div/div/div/div/div/div[2]/div[2]/h3')
        h1_text = h1_tag.text

        image_tag = modal_tag.find_element(By.XPATH, './/div/div/div/div/div/div/div[2]/div[1]/div/img')
        image_link = image_tag.get_attribute('src')
        images.append(image_link)

        text_tag = modal_tag.find_element(By.XPATH, './/div/div/div/div/div/div/div[2]/div[2]/p[3]')
        texts = self.__extract_text(text_tag).strip()[:105] + "..."

        period_tag = modal_tag.find_element(By.XPATH, ".//div/div/div/div/div/div/div[2]/div[2]/p[1]/span")
        expiry_date = period_tag.text.replace(" ", "")
        start, end = self.__convert_date_string(expiry_date)

        try:
          close_modal_tag = self.__find_element(self.driver, By.XPATH, './/button[@class="modaal-close"]', None, 10, 5, "close_modal tag")
          self.driver.execute_script("arguments[0].click();", close_modal_tag)
        except TimeoutException as e:
          raise LinkCannotProcessException(f"Cannot find element error: {e.msg}")

        array_result.append({ "title": h1_text, "images": images, "description": f"{texts}", "site_url": f"{link}", "start_date": start, "end_date": end })

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

  def __convert_date_string(self, date_string):
    month_mapping = {
      '1月': 1, '2月': 2, '3月': 3, '4月': 4, '5月': 5, '6月': 6,
      '7月': 7, '8月': 8, '9月': 9, '10月': 10, '11月': 11, '12月': 12
    }

    if "月" in date_string and "日" in date_string:
      today_year = datetime.now().year
      if "～" in date_string:
        parts = date_string.split('～')
      else:
        parts = date_string.split('〜')

      start_part = parts[0].strip()
      start_month, start_day = start_part.split('月')
      start_month_num = month_mapping[f"{start_month}月"]
      start_date = datetime(today_year, start_month_num, int(start_day.split("日")[0]))

      if len(parts) > 1:
        if "月" in parts[1].strip():
          end_part = parts[1].strip()
          end_month, end_day = end_part.split('月')
          end_month_num = month_mapping[f"{end_month}月"]
          end_date = datetime(today_year, end_month_num, int(end_day.split("日")[0]))
        else:
          if parts[1].strip() != '':
            end_part = parts[1].strip()
            end_date = datetime(today_year, start_month_num, int(end_part.split("日")[0]))
          else:
            return start_date.strftime('%B %d, %Y'), datetime(2999, 12, 31).strftime('%B %d, %Y')
        return start_date.strftime('%B %d, %Y'), end_date.strftime('%B %d, %Y')

      else:
        return start_date.strftime('%B %d, %Y'), datetime(2999, 12, 31).strftime('%B %d, %Y')
    else:
      return None, None

class LinkCannotProcessException(Exception):
  pass

# if __name__ == '__main__':
#   current_directory = "/Users/argiebacomo/Desktop/python_stuffs/scraper-server"
#   info_logger = Logger('info', current_directory)
#   failed_logger = Logger('failed', current_directory)
#   success_logger = Logger('success', current_directory)

#   scraper = ShibuyaScrambleScraper(failed_logger, success_logger, info_logger, False, False)
#   print(scraper.start())
#   scraper.close()
