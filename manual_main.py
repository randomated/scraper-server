from database.saver import Saver
from scrapers.logger import Logger
from scrapers.komeda import KomedaScraper
from scrapers.bio_c_bon import BioCBonScraper
from scrapers.crisp import CrispScraper
from scrapers.masterwal import MasterwalScraper
from scrapers.in_sea import InSeaScraper
from scrapers.loft import LoftScraper
from scrapers.the_melon import TheMelonScraper
from scrapers.flying_tiger import FlyingTigerScraper
from scrapers.hay_japan import HayJapanScraper
from scrapers.shiro_shiro import ShiroShiroScraper
from scrapers.pokka import PokkaCreateScraper
from scrapers.natural_lawson import NaturalLawsonScraper
from scrapers.store_united_arrows import StoreUnitedArrowsScraper
from scrapers.maccosmetics import MaccosmeticsScraper
from scrapers.uniqlo import UniqloScraper
from scrapers.threecosmetics import ThreecosmeticsScraper
from scrapers.dulton import DultonScraper
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
from scrapers.goldsgym import GoldsgymScraper
from scrapers.shop_adidas import ShopAdidasScraper
from scrapers.easyoga import EasyogaScraper
from scrapers.store_descente_arena import StoreDescenteArenaScraper
from scrapers.store_descente_descente import StoreDescenteDescenteScraper
from scrapers.mugendai_yoshimoto import MugendaiYoshimotoScraper
from scrapers.village_v import VillageVScraper
from scrapers.store_descente_descente_golf import StoreDescenteDescenteGolfScraper
from scrapers.southerntower import SoutherntowerScraper
from scrapers.solomons import SolomonsScraper
from scrapers.tokyu_hotels_cerulean_h_restaurant_sakuragaoka import TokyuHotelsCeruleanHRestaurantSakuragaokaScraper
from scrapers.ilfiume import IlfiumeScraper
from scrapers.thaigarden import ThaigardenScraper
from scrapers.tokyu_hotels_cerulean_h_restaurant_caramelo import TokyuHotelsCeruleanHRestaurantCarameloScraper
from scrapers.towafood import TowafoodScraper
from scrapers.doutor import DoutorScraper
from scrapers.phiten import PhitenScraper
from scrapers.ebisu_fukuwarai import EbisuFukuwaraiScraper
from scrapers.reset_gym import ResetGymScraper
from scrapers.spanish_lounge import SpanishLoungeScraper
from scrapers.gaia_ochanomizu import GaiaScraper
from scrapers.starbucks import StarbucksScraper
from scrapers.goldwin import GoldwinScraper
from scrapers.mysweets import MySweetsScraper
from scrapers.tullys import TullyScraper
from scrapers.dipunto import DiPuntoScraper
from scrapers.pronto import ProntoScraper
from scrapers.shibuya_scramble_two import ShibuyaScrambleScraper
from scrapers.donki import DonkiScraper
from scrapers.momastore import MomastoreScraper
import os

current_directory = os.path.dirname(os.path.realpath(__file__))

info_logger = Logger('info', current_directory)
failed_logger = Logger('failed', current_directory)
success_logger = Logger('success', current_directory)
summary_logger = Logger('summary', current_directory)

saver = Saver(current_directory)

scrape_list = { 
  "scrape_list": [
    {
      "type": "akomeya",
      "stores": [
        {
          "store_name": "AKOMEYA TOKYO 東急プラザ渋谷",
          "wls_id": "218"
        }
      ]
    }
  ]
}

# Mapping between JSON types and classes
class_mapping = {
  "komeda": KomedaScraper,
  "bio-c-bon": BioCBonScraper,
  "crisp": CrispScraper,
  "masterwal": MasterwalScraper,
  "in-sea": InSeaScraper,
  "loft": LoftScraper,
  "the_melon": TheMelonScraper,
  "flying_tiger": FlyingTigerScraper,
  "hay_tokyo": HayJapanScraper,
  "shiro": ShiroShiroScraper,
  "pokkacreate": PokkaCreateScraper,
  "natural_lawson": NaturalLawsonScraper,
  "store_united_arrows": StoreUnitedArrowsScraper,
  "maccosmetics": MaccosmeticsScraper,
  "uniqlo": UniqloScraper,
  "threecosmetics": ThreecosmeticsScraper,
  "dulton": DultonScraper,
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
  "goldsgym": GoldsgymScraper,
  "shop_adidas": ShopAdidasScraper,
  "easyoga": EasyogaScraper,
  "store_descente_arena": StoreDescenteArenaScraper,
  "store_descente_descente": StoreDescenteDescenteScraper,
  "mugendai_yoshimoto": MugendaiYoshimotoScraper,
  "village_v": VillageVScraper,
  "store_descente_descente_golf": StoreDescenteDescenteGolfScraper,
  "southerntower": SoutherntowerScraper,
  "solomons": SolomonsScraper,
  "tokyu_hotels_cerulean_h_restaurant_sakuragaoka": TokyuHotelsCeruleanHRestaurantSakuragaokaScraper,
  "ilfiume": IlfiumeScraper,
  "thaigarden": ThaigardenScraper,
  "tokyu_hotels_cerulean_h_restaurant_caramelo": TokyuHotelsCeruleanHRestaurantCarameloScraper,
  "towafood": TowafoodScraper,
  "doutor": DoutorScraper,
  "phiten": PhitenScraper,
  "ebisu_fukuwarai": EbisuFukuwaraiScraper,
  "reset_gym": ResetGymScraper,
  "spanish_lounge": SpanishLoungeScraper,
  "gaia_ochanomizu": GaiaScraper,
  "starbucks": StarbucksScraper,
  "goldwin": GoldwinScraper,
  "mysweets": MySweetsScraper,
  "tullys": TullyScraper,
  "dipunto": DiPuntoScraper,
  'pronto': ProntoScraper,
  "shibuya_scramble": ShibuyaScrambleScraper,
  'donki': DonkiScraper,
  'momastore': MomastoreScraper,
}

will_hide = True
is_chrome = True


def create_record(title, description, site_url, images, store_name, wls_id):
  inserted_id = saver.add_scraped_data(title.split("\n")[1], description, site_url, images)
  saver.add_store(inserted_id, store_name, wls_id)

for item in scrape_list["scrape_list"]:
  cls = class_mapping[item['type']]
  scraper = cls(failed_logger, success_logger, info_logger, will_hide, is_chrome)
  result = scraper.start()
  scraper.close()
  
  if result['is_success'] is True:
    summary_logger.log(f"{item['type']} SUCCESS")

    data = result['data']

    if item['type'] == 'mysweets':
      for res in data:
        contains_data_image = any("data:image" in image_link for image_link in res['images'])
        if not contains_data_image:
          if "渋谷店" in res['title']:
            create_record(res['title'], res['description'], res['site_url'], res['images'], "MY SWEETS 渋谷店", 712)
          if "東急プラザ蒲田店" in res['title']:
            create_record(res['title'], res['description'], res['site_url'], res['images'], "MY SWEETS 東急プラザ蒲田店", 713)
          if "エトモ武蔵小山店" in res['title']:
            create_record(res['title'], res['description'], res['site_url'], res['images'], "MY SWEETS エトモ武蔵小山店", 714)
          if "エトモ長津田店" in res['title']:
            create_record(res['title'], res['description'], res['site_url'], res['images'], "MY SWEETS エトモ長津田店", 715)
          if "エトモ大井町店" in res['title']:
            create_record(res['title'], res['description'], res['site_url'], res['images'], "MY SWEETS エトモ大井町店", 716)
          if "エトモ市が尾店" in res['title']:
            create_record(res['title'], res['description'], res['site_url'], res['images'], "MY SWEETS エトモ市ヶ尾店", 717)
          if "エトモ中央林間店" in res['title']:
            create_record(res['title'], res['description'], res['site_url'], res['images'], "MY SWEETS エトモ中央林間店", 718)
          if "二子玉川店" in res['title']:
            create_record(res['title'], res['description'], res['site_url'], res['images'], "MY SWEETS 二子玉川店", 719)
    elif item['type'] == 'shibuya_scramble':
      for res in data:
        contains_data_image = any("data:image" in image_link for image_link in res['images'])
        inserted_id = saver.add_scraped_data(res['title'], res['description'], res['site_url'], res['images'], res['start_date'], res['end_date'])
        for store in item["stores"]:
          saver.add_store(inserted_id, store['store_name'], store['wls_id'])
    else:
      contains_data_image = any("data:image" in image_link for image_link in data['images'])

      if not contains_data_image:
        inserted_id = saver.add_scraped_data(data['title'], data['description'], data['site_url'], data['images'])

        for store in item["stores"]:
          saver.add_store(inserted_id, store['store_name'], store['wls_id'])

  else:
    summary_logger.log(f"{item['type']} FAILED")

saver.close_db()

