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
    },
    {
      "type": "goldsgym",
      "stores": [
        {
          "store_name": "GOLD'S GYM代々木公園PREMIUM",
          "wls_id": "643"
        },
        {
          "store_name": "GOLD'S GYM代々木上原東京",
          "wls_id": "642"
        }
      ]
    },
    {
      "type": "shop_adidas",
      "stores": [
        {
          "store_name": "アディダス オリジナルス ガールズ ショップ 渋谷109",
          "wls_id": "171"
        },
        {
          "store_name": "アディダス オリジナルス フラッグシップ ストア 原宿",
          "wls_id": "170"
        },
        {
          "store_name": "アディダス ブランドセンター原宿",
          "wls_id": "169"
        },
        {
          "store_name": "アディダス ブランドセンター RAYARD MIYASHITA PARK",
          "wls_id": "168"
        },
        {
          "store_name": "アディダス ブランドセンター 渋谷",
          "wls_id": "167"
        }
      ]
    },
    {
      "type": "easyoga",
      "stores": [
        {
          "store_name": "イージーヨガストア代官山",
          "wls_id": "166"
        }
      ]
    },
    {
      "type": "store_descente_arena",
      "stores": [
        {
          "store_name": "アリーナショップ 東京",
          "wls_id": "192"
        }
      ]
    },
    {
      "type": "store_descente_descente",
      "stores": [
        {
          "store_name": "DESCENTE TOKYO",
          "wls_id": "194"
        }
      ]
    },
    {
      "type": "mugendai_yoshimoto",
      "stores": [
        {
          "store_name": "よしもと∞ホール",
          "wls_id": "644"
        },
        {
          "store_name": "吉本∞ホール",
          "wls_id": "685"
        },
        {
          "store_name": "サンプルストア",
          "wls_id": "684"
        }
      ]
    },
    {
      "type": "village_v",
      "stores": [
        {
          "store_name": "ヴィレッジヴァンガード渋谷本店",
          "wls_id": "203"
        }
      ]
    },
    {
      "type": "store_descente_descente_golf",
      "stores": [
        {
          "store_name": "DESCENT GOLF 新宿タカシマヤ",
          "wls_id": "195"
        }
      ]
    },
    {
      "type": "tokyu_hotels_cerulean_h_restaurant_sakuragaoka",
      "stores": [
        {
          "store_name": "日本料理「Japanese Cuisine 桜丘」",
          "wls_id": "492"
        }
      ]
    },
    {
      "type": "tokyu_hotels_cerulean_h_restaurant_caramelo",
      "stores": [
        {
          "store_name": "ガーデンキッチン「かるめら」",
          "wls_id": "422"
        }
      ]
    },
    {
      "type": "thaigarden",
      "stores": [
        {
          "store_name": "Thai Garden 渋谷",
          "wls_id": "443"
        }
      ]
    },
    {
      "type": "ilfiume",
      "stores": [
        {
          "store_name": "イタリアンダイニング Il Fiume（イルフューメ）渋谷",
          "wls_id": "489"
        }
      ]
    },
    {
      "type": "solomons",
      "stores": [
        {
          "store_name": "原宿Solomons（ソロモンズ）",
          "wls_id": "498"
        }
      ]
    },
    {
      "type": "southerntower",
      "stores": [
        {
          "store_name": "ラウンジ サウスコート ｜Lounge South Court",
          "wls_id": "499"
        }
      ]
    },
    {
      "stores": [
        {
          "store_name": "エクセルシオール カフェ 渋谷宮益坂店",
          "wls_id": "597"
        }
      ],
      'type': 'doutor'
    },
    {
      "stores": [
        {
          "store_name": "ファイテンショップ 渋谷東口店",
          "wls_id": "199"
        }
      ],
      'type': 'phiten'
    },
    {
      "stores": [
        {
          "store_name": "福笑（ふくわらい）",
          "wls_id": "366"
        }
      ],
      'type': 'ebisu_fukuwarai'
    },
    {
      "stores": [
        {
          "store_name": "プロテインバーRESET",
          "wls_id": "478"
        }
      ],
      'type': 'reset_gym'
    },
    {
      "stores": [
        {
          "store_name": "spanish lounge parador パラドール",
          "wls_id": "495"
        }
      ],
      'type': 'spanish_lounge'
    },
    {
      "stores": [
        {
          "store_name": "GAIA 代々木上原店",
          "wls_id": "384"
        }
      ],
      'type': 'gaia_ochanomizu'
    },
    {
      "stores": [
        {
          "store_name": "JOURNAL STANDARD FURNITURE 渋谷店",
          "wls_id": "395"
        }
      ],
      'type': 'baycrews'
    },
    {
      "stores": [
        {
          "store_name": "スターバックス京王笹塚店",
          "wls_id": "545"
        },
        {
          "store_name": "スターバックスアコルデ代々木上原店",
          "wls_id": "544"
        },
        {
          "store_name": "スターバックス代々木店",
          "wls_id": "543"
        },
        {
          "store_name": "スターバックス新宿南口店",
          "wls_id": "542"
        },
        {
          "store_name": "スターバックス新宿サザンテラス店",
          "wls_id": "541"
        },
        {
          "store_name": "スターバックス新宿マインズタワー店",
          "wls_id": "540"
        },
        {
          "store_name": "スターバックス北参道店",
          "wls_id": "539"
        },
        {
          "store_name": "スターバックスリンクスクエア新宿店",
          "wls_id": "538"
        },
        {
          "store_name": "スターバックス渋谷ヒカリエ ShinQs店",
          "wls_id": "537"
        },
        {
          "store_name": "スターバックス渋谷パルコ店",
          "wls_id": "536"
        },
        {
          "store_name": "スターバックスTSUTAYA BOOKSTORE 渋谷スクランブルスクエア店",
          "wls_id": "535"
        },
        {
          "store_name": "スターバックス恵比寿ガーデンプレイスタワー１F店",
          "wls_id": "534"
        },
        {
          "store_name": "スターバックス渋谷文化村通り店",
          "wls_id": "533"
        },
        {
          "store_name": "スターバックス渋谷フクラス店",
          "wls_id": "532"
        },
        {
          "store_name": "スターバックス渋谷マークシティ店",
          "wls_id": "531"
        },
        {
          "store_name": "スターバックスSHIBUYA TSUTAYA店",
          "wls_id": "530"
        },
        {
          "store_name": "スターバックス渋谷ファイヤー通り店",
          "wls_id": "529"
        },
        {
          "store_name": "スターバックス渋谷モディ店",
          "wls_id": "528"
        },
        {
          "store_name": "スターバックス渋谷公園通り店",
          "wls_id": "527"
        },
        {
          "store_name": "スターバックスプリンチ 代官山T-SITE",
          "wls_id": "526"
        },
        {
          "store_name": "スターバックス代官山 蔦屋書店",
          "wls_id": "525"
        },
        {
          "store_name": "スターバックスアトレ恵比寿店(2F)",
          "wls_id": "524"
        },
        {
          "store_name": "スターバックスアトレ恵比寿店(5F)",
          "wls_id": "523"
        },
        {
          "store_name": "スターバックス恵比寿ユニオンビル店",
          "wls_id": "522"
        },
        {
          "store_name": "スターバックス恵比寿ガーデンプレイス センタープラザB1店",
          "wls_id": "521"
        },
        {
          "store_name": "スターバックス恵比寿ファーストスクエア店",
          "wls_id": "520"
        },
        {
          "store_name": "スターバックス広尾店",
          "wls_id": "519"
        },
        {
          "store_name": "スターバックス渋谷クロスタワー店",
          "wls_id": "518"
        },
        {
          "store_name": "スターバックス渋谷３丁目店",
          "wls_id": "517"
        },
        {
          "store_name": "スターバックス渋谷cocoti店",
          "wls_id": "516"
        },
        {
          "store_name": "スターバックス渋谷ストリーム店",
          "wls_id": "515"
        },
        {
          "store_name": "スターバックス渋谷2丁目店",
          "wls_id": "514"
        },
        {
          "store_name": "スターバックス神宮前6丁目店",
          "wls_id": "513"
        },
        {
          "store_name": "スターバックス明治神宮前メトロピア店",
          "wls_id": "512"
        },
        {
          "store_name": "スターバックスMIYASHITA PARK店",
          "wls_id": "511"
        },
        {
          "store_name": "スターバックスWITH HARAJUKU店",
          "wls_id": "510"
        },
        {
          "store_name": "スターバックス表参道ヒルズ店",
          "wls_id": "509"
        },
        {
          "store_name": "スターバックス東急プラザ 表参道原宿店",
          "wls_id": "508"
        },
        {
          "store_name": "スターバックス表参道 神宮前4丁目店",
          "wls_id": "507"
        }
      ],
      'type': 'starbucks'
    },
    {
      'type': 'goldwin',
      'stores': [
        {
          "store_name": "THE NORTHFACE CAMP/PLAY EARTH KIDS/NEUTRALWORKS.恵比",
          "wls_id": "159"
        },
        {
          "store_name": "THE NORTH FACE/DANSKIN beautiful things ヒカリエShinQs",
          "wls_id": "160"
        }
      ]
    },
    {
      'type': 'mysweets',
      'stores': [
        {
          "store_name": "サンプルストア",
          "wls_id": "688"
        }
      ]
    }
  ]
}


# {
#   "type": "seria_group",
#   "stores": [
#     {
#       "store_name": "Seria代官山アドレス・ディセ店",
#       "wls_id": "223"
#     }
#   ]
# },
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
# },
# {
#   "type": "nergy",
#   "stores": [
#     {
#       "store_name": "nergy ATRE EBISU",
#       "wls_id": "165"
#     },
#     {
#       "store_name": "nergy SHIBUYA SCRAMBLE SQUARE",
#       "wls_id": "164"
#     }
#   ]
# },
# {
#   "stores": [
#     {
#       "store_name": "椿屋カフェ フレンテ笹塚店",
#       "wls_id": "620"
#     },
#     {
#       "store_name": "椿屋カフェ 渋谷店",
#       "wls_id": "619"
#     }
#   ],
#   'type': 'towafood'
# },



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
  "mysweets": MySweetsScraper
}

will_hide = True
is_chrome = True

for item in scrape_list["scrape_list"]:
  cls = class_mapping[item['type']]
  scraper = cls(failed_logger, success_logger, info_logger, will_hide, is_chrome)
  result = scraper.start()
  scraper.close()
  
  if result['is_success'] is True:
    summary_logger.log(f"{item['type']} SUCCESS")

    data = result['data']

    if item['type'] != 'mysweets':
      contains_data_image = any("data:image" in image_link for image_link in data['images'])

      if not contains_data_image:
        inserted_id = saver.add_scraped_data(data['title'], data['description'], data['site_url'], data['images'])

        for store in item["stores"]:
          saver.add_store(inserted_id, store['store_name'], store['wls_id'])
    else:
      for res in data:
        contains_data_image = any("data:image" in image_link for image_link in res['images'])
        if not contains_data_image:
          inserted_id = saver.add_scraped_data(res['title'], res['description'], res['site_url'], res['images'])

          for store in item["stores"]:
            saver.add_store(inserted_id, store['store_name'], store['wls_id'])
  else:
    summary_logger.log(f"{item['type']} FAILED")

saver.close_db()


