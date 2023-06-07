import json
text = """
GOLD'S GYM代々木公園PREMIUM	https://www.goldsgym.jp/	643
GOLD'S GYM代々木上原東京	https://www.goldsgym.jp/	642
アディダス オリジナルス ガールズ ショップ 渋谷109	https://shop.adidas.jp/	171
アディダス オリジナルス フラッグシップ ストア 原宿	https://shop.adidas.jp/	170
アディダス ブランドセンター原宿	https://shop.adidas.jp/	169
アディダス ブランドセンター RAYARD MIYASHITA PARK	https://shop.adidas.jp/	168
アディダス ブランドセンター 渋谷	https://shop.adidas.jp/	167
イージーヨガストア代官山	https://www.easyoga.jp/	166
アリーナショップ 東京	https://store.descente.co.jp/arena/	192
DESCENTE TOKYO	https://store.descente.co.jp/descente/	194
よしもと∞ホール	https://mugendai.yoshimoto.co.jp/	644
ヴィレッジヴァンガード渋谷本店	https://www.village-v.co.jp/	203
DESCENT GOLF 新宿タカシマヤ	https://store.descente.co.jp/descentegolf/ext/news/	195
"""

scrape_list = { "scrape_list": [] }

lines = text.strip().split('\n')
for line in lines:
    data = line.split('\t')

    index = next((index for index, item in enumerate(scrape_list["scrape_list"]) if item["type"] == data[1]), -1)

    if index != -1:
    	scrape_list["scrape_list"][index]["stores"].append({ "store_name": data[0], "wls_id": data[2] })
    else:
    	scrape_list["scrape_list"].append({ "type": data[1], "stores": [ { "store_name": data[0], "wls_id": data[2] } ] })

print(json.dumps(scrape_list, indent=2, ensure_ascii=False))