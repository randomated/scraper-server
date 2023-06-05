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
from database.saver import Saver
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
    },
    {
      "stores": [
        {"store_name": "Flying Tiger Copenhagen表参道ストア", "wls_id": 221},
      ],  
      "type": "flying_tiger"
    },
    {
      "stores": [
        {"store_name": "HAY TOKYO", "wls_id": 219},
      ],  
      "type": "hay_tokyo"
    },
    {
      "stores": [
        {"store_name": "SHIRO 渋谷ヒカリエ ShinQs店", "wls_id": 278},
        {"store_name": "SHIRO ＋Q（プラスク）ビューティー渋谷スクランブルスクエア店", "wls_id": 277},
        {"store_name": "SHIRO BEAUTY 表参道本店", "wls_id": 276},
        {"store_name": "SHIRO 表参道本店", "wls_id": 275},
      ],  
      "type": "shiro"
    },
    {
      "stores": [
        {
          "store_name": "カフェ・ド・クリエ グラン 恵比寿ガーデンプレイス店",
          "wls_id": "607"
        },
        {
          "store_name": "カフェ・ド・クリエ グラン　渋谷桜丘スクエア店",
          "wls_id": "606"
        },
        {
          "store_name": "カフェ・ド・クリエ 代々木東口店",
          "wls_id": "605"
        },
        {
          "store_name": "カフェ・ド・クリエ 南新宿店",
          "wls_id": "604"
        },
        {
          "store_name": "カフェ・ド・クリエ 渋谷3丁目店",
          "wls_id": "603"
        }
      ],
      "type": "pokkacreate"
    },
    {
      "type": "natural_lawson",
      "stores": [
        {
          "store_name": "ナチュラルローソン　渋谷神泉町",
          "wls_id": "360"
        },
        {
          "store_name": "ナチュラルローソン　恵比寿南三丁目",
          "wls_id": "359"
        },
        {
          "store_name": "ナチュラルローソン　渋谷道玄坂一丁目",
          "wls_id": "358"
        },
        {
          "store_name": "ナチュラルローソン　渋谷代官山",
          "wls_id": "357"
        },
        {
          "store_name": "ナチュラルローソン　代々木駅西",
          "wls_id": "356"
        },
        {
          "store_name": "ナチュラルローソン　渋谷一丁目",
          "wls_id": "355"
        },
        {
          "store_name": "ナチュラルローソン　神宮外苑西",
          "wls_id": "354"
        },
        {
          "store_name": "ナチュラルローソン　広尾五丁目",
          "wls_id": "353"
        },
        {
          "store_name": "ナチュラルローソン　代々木八幡",
          "wls_id": "352"
        }
      ]
    },
    {
      "type": "maccosmetics",
      "stores": [
        {
          "store_name": "M∙A∙C Cosmetics Japanラフォーレ原宿",
          "wls_id": "340"
        },
        {
          "store_name": "M∙A∙C Cosmetics Japan 渋谷ヒカリエ シンクス",
          "wls_id": "339"
        },
        {
          "store_name": "M∙A∙C Cosmetics Japan 渋谷スクランブルスクエア",
          "wls_id": "338"
        },
        {
          "store_name": "M∙A∙C Cosmetics Japan 西武渋谷",
          "wls_id": "337"
        }
      ]
    }
  ]
}

# {
#   "type": "store_united_arrows",
#   "stores": [
#     {
#       "store_name": "ユナイテッドアローズ アトレ恵比寿 ウィメンズストア",
#       "wls_id": "190"
#     },
#     {
#       "store_name": "ユナイテッドアローズ 渋谷スクランブルスクエア店",
#       "wls_id": "189"
#     },
#     {
#       "store_name": "オデット エ オディール 渋谷シンクス店",
#       "wls_id": "188"
#     },
#     {
#       "store_name": "ユナイテッドアローズ 渋谷シンクス ウィメンズストア",
#       "wls_id": "187"
#     },
#     {
#       "store_name": "ロク 渋谷キャットストリート店 （ROKU SHIBUYA CAT STREET）",
#       "wls_id": "186"
#     },
#     {
#       "store_name": "UNITED ARROWS ディストリクト",
#       "wls_id": "185"
#     },
#     {
#       "store_name": "ユナイテッドアローズ＆サンズ （UNITED ARROWS & SONS）",
#       "wls_id": "184"
#     },
#     {
#       "store_name": "ユナイテッドアローズ 原宿本店",
#       "wls_id": "183"
#     }
#   ]
# }


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
  "maccosmetics": MaccosmeticsScraper
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
    inserted_id = saver.add_scraped_data(data['title'], data['description'], data['site_url'], data['images'])

    for store in item["stores"]:
      saver.add_store(inserted_id, store['store_name'], store['wls_id'])
  else:
    summary_logger.log(f"{item['type']} FAILED")

saver.close_db()


