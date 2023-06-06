import json
text = """
ハンズ渋谷スクランブルスクエア店	https://hands.net/	206
ハンズ渋谷店	https://hands.net/	205
ハンズ新宿店	https://hands.net/	204
WithGreen恵比寿店	https://withgreen.club/	390
WithGreen渋谷ヒカリエShinQs東横のれん街店	https://withgreen.club/	389
GU渋谷店	https://www.gu-global.com/jp/ja/feature/list/pc/	181
nergy ATRE EBISU	https://www.nergy.jp/	165
nergy SHIBUYA SCRAMBLE SQUARE	https://www.nergy.jp/	164
FIGHTING ROAD東京店	https://www.fightingroad.co.jp/	196
MIZUNO TOKYO	https://jpn.mizuno.com/campaign?did=dtctop_campaignlist	197
2foods 渋⾕ロフト店	https://2foods.jp/	419
ガーデンラウンジ「坐忘」	https://www.tokyuhotels.co.jp/cerulean-h/restaurant/zabou/index.html	484
ザ・レギャン・トーキョー	https://www.legian.jp/	486
Dining TORRENT	https://www.tokyuhotels.co.jp/stream-e/bar_dining/index.html	491
LUSH 原宿店	https://weare.lush.com/jp/	283
LUSH 渋谷駅前店	https://weare.lush.com/jp/	282
ヨガスタジオ YOGIWAY	https://www.yogiway.jp/	258
BRUNO 渋谷ヒカリエ ShinQs	https://bruno-onlineshop.com/	401
Shibuya-san	https://shibuya-san.co.jp/	646
渋谷区立松濤美術館	https://shoto-museum.jp/	650
8/(ヒカリエ)	http://www.hikarie8.com/home.shtml	656
Seria代官山アドレス・ディセ店	https://www.seria-group.com/	223
AKOMEYA TOKYO 東急プラザ渋谷	https://www.akomeya.jp/shop/pc/0feature/	218
Sushi Gonpachi Shibuya	https://gonpachi.jp/news/	437
Gonpachi Shibuya	https://gonpachi.jp/news/	436
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