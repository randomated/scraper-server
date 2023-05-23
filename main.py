from scrapers.logger import Logger
from scrapers.komeda import KomedaScraper
from scrapers.bio_c_bon import BioCBonScraper
from scrapers.crisp import CrispScraper
from scrapers.masterwal import MasterwalScraper
from scrapers.in_sea import InSeaScraper
from scrapers.loft import LoftScraper
from scrapers.the_melon import TheMelonScraper
from database.saver import Saver

info_logger = Logger('info')
failed_logger = Logger('failed')
success_logger = Logger('success')
summary_logger = Logger('summary')

saver = Saver()

scrape_list = { 
  "scrape_list": [
    { 
      "stores": [
        {"store_name": "コメダ珈琲店 渋谷道玄坂上店", "wls_id": 563},
        {"store_name": "コメダ珈琲店 渋谷宮益坂上店", "wls_id": 562},
      ], 
      "type": "komeda"
    },
    { 
      "stores": [
        {"store_name": "ビオセボン恵比寿店", "wls_id": 383},
        {"store_name": "ビオセボン富ヶ谷店", "wls_id": 382},
        {"store_name": "ビオセボン外苑西通り店", "wls_id": 381},
      ], 
      "type": "bio-c-bon"
    },
    { 
      "stores": [
        {"store_name": "CRISP SALAD WORKS恵比寿店", "wls_id": 394},
        {"store_name": "CRISP SALAD WORKS代官山店", "wls_id": 393},
        {"store_name": "CRISP SALAD WORKS新宿南口店", "wls_id": 392},
        {"store_name": "CRISP SALAD WORKS渋谷スクランブルスクエア店", "wls_id": 391},
      ], 
      "type": "crisp"
    },
    {
      "stores": [
        {"store_name": "#Re by MASTERWAL 渋谷スクランブルスクエア", "wls_id": 410}
      ],
      "type": "masterwal"
    },
    {
      "stores": [
        {"store_name": "Magma spastudio INSEA 恵比寿店", "wls_id": 263}
      ],  
      "type": "in-sea"
    },
    {
      "stores": [
        {"store_name": "コスメロフト東急プラザ表参道原宿店", "wls_id": 208},
        {"store_name": "渋谷ロフト", "wls_id": 207}
      ],  
      "type": "loft"
    },
    {
      "stores": [
        {"store_name": "マインドフルネスサロン MELON 渋谷", "wls_id": 256},
      ],  
      "type": "the_melon"
    }
  ]
}

will_hide = True

# result = [texts, new_link, image_link, h1_text]
for item in scrape_list["scrape_list"]:
  if item['type'] == "komeda":
    scraper = KomedaScraper(failed_logger, success_logger, info_logger, will_hide, False)
    result = scraper.start()
    scraper.close()
    if result['is_success'] is True:
      summary_logger.log('KOMEDA SUCCESS')

      data = result['data']
      inserted_id = saver.add_scraped_data(data['title'], data['description'], data['site_url'], data['images'])

      for store in item["stores"]:
        saver.add_store(inserted_id, store['store_name'], store['wls_id'])
    else:
      summary_logger.log('KOMEDA FAILED')

  elif item['type'] == "bio-c-bon":
    scraper = BioCBonScraper(failed_logger, success_logger, info_logger, will_hide, False)
    result = scraper.start()
    scraper.close()
    if result['is_success'] is True:
      summary_logger.log('BIO-C-BON SUCCESS')

      data = result['data']
      inserted_id = saver.add_scraped_data(data['title'], data['description'], data['site_url'], data['images'])

      for store in item["stores"]:
        saver.add_store(inserted_id, store['store_name'], store['wls_id'])
    else:
      summary_logger.log('BIO-C-BON FAILED')

  elif item['type'] == "crisp":
    scraper = CrispScraper(failed_logger, success_logger, info_logger, will_hide, False)
    result = scraper.start()
    scraper.close()
    if result['is_success'] is True:
      summary_logger.log('CRISP SUCCESS')

      data = result['data']
      inserted_id = saver.add_scraped_data(data['title'], data['description'], data['site_url'], data['images'])

      for store in item["stores"]:
        saver.add_store(inserted_id, store['store_name'], store['wls_id'])
    else:
      summary_logger.log('CRISP FAILED')

  elif item['type'] == "masterwal":
    scraper = MasterwalScraper(failed_logger, success_logger, info_logger, will_hide, False)
    result = scraper.start()
    scraper.close()
    if result['is_success'] is True:
      summary_logger.log('MASTERWAL SUCCESS')

      data = result['data']
      inserted_id = saver.add_scraped_data(data['title'], data['description'], data['site_url'], data['images'])

      for store in item["stores"]:
        saver.add_store(inserted_id, store['store_name'], store['wls_id'])
    else:
      summary_logger.log('MASTERWAL FAILED')

  elif item['type'] == "in-sea":
    scraper = InSeaScraper(failed_logger, success_logger, info_logger, will_hide, False)
    result = scraper.start()
    scraper.close()
    if result['is_success'] is True:
      summary_logger.log('IN-SEA SUCCESS')

      data = result['data']
      inserted_id = saver.add_scraped_data(data['title'], data['description'], data['site_url'], data['images'])

      for store in item["stores"]:
        saver.add_store(inserted_id, store['store_name'], store['wls_id'])
    else:
      summary_logger.log('IN-SEA FAILED')

  elif item['type'] == "loft":
    scraper = LoftScraper(failed_logger, success_logger, info_logger, will_hide, False)
    result = scraper.start()
    scraper.close()
    if result['is_success'] is True:
      summary_logger.log('LOFT SUCCESS')

      data = result['data']
      inserted_id = saver.add_scraped_data(data['title'], data['description'], data['site_url'], data['images'])

      for store in item["stores"]:
        saver.add_store(inserted_id, store['store_name'], store['wls_id'])
    else:
      summary_logger.log('LOFT FAILED')

  elif item['type'] == "the_melon":
    scraper = TheMelonScraper(failed_logger, success_logger, info_logger, will_hide, False)
    result = scraper.start()
    scraper.close()
    if result['is_success'] is True:
      summary_logger.log('THE-MELON SUCCESS')

      data = result['data']
      inserted_id = saver.add_scraped_data(data['title'], data['description'], data['site_url'], data['images'])

      for store in item["stores"]:
        saver.add_store(inserted_id, store['store_name'], store['wls_id'])
    else:
      summary_logger.log('THE-MELON FAILED')

      
saver.close_db()