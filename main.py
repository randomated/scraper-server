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
    },
    {
      "type": "uniqlo",
      "stores": [
        {
          "store_name": "ユニクロ 渋谷道玄坂店",
          "wls_id": "180"
        },
        {
          "store_name": "ユニクロ 新宿高島屋店",
          "wls_id": "179"
        },
        {
          "store_name": "ユニクロ 原宿店",
          "wls_id": "178"
        }
      ]
    },
    {
      "type": "threecosmetics",
      "stores": [
        {
          "store_name": "THREE 西武渋谷店",
          "wls_id": "281"
        },
        {
          "store_name": "THREE 渋谷ヒカリエ ShinQs店",
          "wls_id": "280"
        },
        {
          "store_name": "VISIONARIUM THREE SHIBUYA",
          "wls_id": "279"
        }
      ]
    },
    {
      "type": "dulton",
      "stores": [
        {
          "store_name": "ル・クルーゼ 渋谷ヒカリエ ShinQs店",
          "wls_id": "406"
        },
        {
          "store_name": "ル・クルーゼ 新宿タカシマヤ",
          "wls_id": "407"
        }
      ]
    },
    {
      "type": "hands",
      "stores": [
        {
          "store_name": "ハンズ渋谷スクランブルスクエア店",
          "wls_id": "206"
        },
        {
          "store_name": "ハンズ渋谷店",
          "wls_id": "205"
        },
        {
          "store_name": "ハンズ新宿店",
          "wls_id": "204"
        }
      ]
    },
    {
      "type": "withgreen",
      "stores": [
        {
          "store_name": "WithGreen恵比寿店",
          "wls_id": "390"
        },
        {
          "store_name": "WithGreen渋谷ヒカリエShinQs東横のれん街店",
          "wls_id": "389"
        }
      ]
    },
    {
      "type": "gu_global",
      "stores": [
        {
          "store_name": "GU渋谷店",
          "wls_id": "181"
        }
      ]
    },
    {
      "type": "nergy",
      "stores": [
        {
          "store_name": "nergy ATRE EBISU",
          "wls_id": "165"
        },
        {
          "store_name": "nergy SHIBUYA SCRAMBLE SQUARE",
          "wls_id": "164"
        }
      ]
    },
    {
      "type": "fighting_road",
      "stores": [
        {
          "store_name": "FIGHTING ROAD東京店",
          "wls_id": "196"
        }
      ]
    },
    {
      "type": "mizuno",
      "stores": [
        {
          "store_name": "MIZUNO TOKYO",
          "wls_id": "197"
        }
      ]
    },
    {
      "type": "two_foods",
      "stores": [
        {
          "store_name": "2foods 渋⾕ロフト店",
          "wls_id": "419"
        }
      ]
    },
    {
      "type": "tokyu_hotels_cerulean_h",
      "stores": [
        {
          "store_name": "ガーデンラウンジ「坐忘」",
          "wls_id": "484"
        }
      ]
    },
    {
      "type": "legian",
      "stores": [
        {
          "store_name": "ザ・レギャン・トーキョー",
          "wls_id": "486"
        }
      ]
    },
    {
      "type": "tokyu_hotels_stream_e",
      "stores": [
        {
          "store_name": "Dining TORRENT",
          "wls_id": "491"
        }
      ]
    },
    {
      "type": "weare_lush",
      "stores": [
        {
          "store_name": "LUSH 原宿店",
          "wls_id": "283"
        },
        {
          "store_name": "LUSH 渋谷駅前店",
          "wls_id": "282"
        }
      ]
    },
    {
      "type": "yogiway",
      "stores": [
        {
          "store_name": "ヨガスタジオ YOGIWAY",
          "wls_id": "258"
        }
      ]
    },
    {
      "type": "bruno_online_shop",
      "stores": [
        {
          "store_name": "BRUNO 渋谷ヒカリエ ShinQs",
          "wls_id": "401"
        }
      ]
    },
    {
      "type": "shibuya_san",
      "stores": [
        {
          "store_name": "Shibuya-san",
          "wls_id": "646"
        }
      ]
    },
    {
      "type": "shoto_museum",
      "stores": [
        {
          "store_name": "渋谷区立松濤美術館",
          "wls_id": "650"
        }
      ]
    },
    {
      "type": "hikarie",
      "stores": [
        {
          "store_name": "8/(ヒカリエ)",
          "wls_id": "656"
        }
      ]
    },
    {
      "type": "seria_group",
      "stores": [
        {
          "store_name": "Seria代官山アドレス・ディセ店",
          "wls_id": "223"
        }
      ]
    },
    {
      "type": "akomeya",
      "stores": [
        {
          "store_name": "AKOMEYA TOKYO 東急プラザ渋谷",
          "wls_id": "218"
        }
      ]
    },
    {
      "type": "gonpachi",
      "stores": [
        {
          "store_name": "Sushi Gonpachi Shibuya",
          "wls_id": "437"
        },
        {
          "store_name": "Gonpachi Shibuya",
          "wls_id": "436"
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
  "maccosmetics": MaccosmeticsScraper,
  "uniqlo": UniqloScraper,
  "threecosmetics": ThreecosmeticsScraper,
  "dulton": DultonScraper
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


