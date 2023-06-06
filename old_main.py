from scrapers.logger import Logger
from database.saver import Saver
from scrapers.hands import HandsScraper
from scrapers.withgreen import WithgreenScraper
from scrapers.gu_global import GuGlobalScraper
from scrapers.nergy import NergyScraper
from scrapers.fighting_road import FightingRoadScraper
from scrapers.mizuno import MizunoScraper
from scrapers.two_foods import TwoFoodsScraper
from scrapers.tokyu_hotels_cerulean_h import TokyuHotelsCeruleanHScraper
from scrapers.legian import LegianScraper
from scrapers.tokyu_hotels_stream_e import TokyuHotelsStreamEScraper
from scrapers.weare_lush import WeareLushScraper
from scrapers.yogiway import YogiwayScraper
from scrapers.baycrews import BaycrewsScraper
from scrapers.bruno_online_shop import BrunoOnlineShopScraper
from scrapers.shibuya_san import ShibuyaSanScraper
from scrapers.shoto_museum import ShotoMuseumScraper
from scrapers.hikarie import HikarieScraper
from scrapers.seria_group import SeriaGroupScraper
from scrapers.akomeya import AkomeyaScraper
from scrapers.gonpachi import GonpachiScraper
import os

current_directory = os.path.dirname(os.path.realpath(__file__))

info_logger = Logger('info', current_directory)
failed_logger = Logger('failed', current_directory)
success_logger = Logger('success', current_directory)
summary_logger = Logger('summary', current_directory)

saver = Saver(current_directory)

scrape_list = {
  'scrape_list': [{'stores': [{'store_name': 'SAMPLE', 'wls_id': 563}], 'type': 'akomeya'}, {'stores': [{'store_name': 'SAMPLE', 'wls_id': 563}], 'type': 'gonpachi'}]
}


# Mapping between JSON types and classes
class_mapping = {
  "hands": HandsScraper, 
  "withgreen": WithgreenScraper, 
  "gu_global": GuGlobalScraper, 
  "nergy": NergyScraper, 
  "fighting_road": FightingRoadScraper, 
  "mizuno": MizunoScraper, 
  "two_foods": TwoFoodsScraper, 
  "tokyu_hotels_cerulean_h": TokyuHotelsCeruleanHScraper, 
  "legian": LegianScraper, 
  "tokyu_hotels_stream_e": TokyuHotelsStreamEScraper, 
  "weare_lush": WeareLushScraper, 
  "yogiway": YogiwayScraper, 
  "baycrews": BaycrewsScraper, 
  "bruno_online_shop": BrunoOnlineShopScraper, 
  "shibuya_san": ShibuyaSanScraper, 
  "shoto_museum": ShotoMuseumScraper, 
  "hikarie": HikarieScraper, 
  "seria_group": SeriaGroupScraper, 
  "akomeya": AkomeyaScraper, 
  "gonpachi": GonpachiScraper, 
}

will_hide = True

for item in scrape_list["scrape_list"]:
  cls = class_mapping[item['type']]
  scraper = cls(failed_logger, success_logger, info_logger, will_hide, False)
  result = scraper.start()
  scraper.close()
  
  if result['is_success'] is True:
    summary_logger.log(f"{item['type']} SUCCESS")

    data = result['data']

    contains_data_image = any("data:image" in image_link for image_link in data['images'])

    if not contains_data_image:
      inserted_id = saver.add_scraped_data(data['title'], data['description'], data['site_url'], data['images'])

      for store in item["stores"]:
        saver.add_store(inserted_id, store['store_name'], store['wls_id'])
  else:
    summary_logger.log(f"{item['type']} FAILED")

saver.close_db()


