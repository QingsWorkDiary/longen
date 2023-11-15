import datetime
import time

import scrapy
from ..items import JdItem


class Jd1Spider(scrapy.Spider):
    name = 'jd1'
    # https://list.jd.com/list.html?cat=1318,12099,9756
    start_urls = [
        'https://list.jd.com/list.html?cat=1318,12099,9756'
        ,
        'https://list.jd.com/list.html?cat=1318%2C12099%2C9756&isList=1&page=3&s=57&click=0&log_id=1699882370108.1505'
        ,
        'https://list.jd.com/list.html?cat=1318%2C12099%2C9756&isList=1&page=5&s=117&click=0&log_id=1699882577090.4788'
        ,
        'https://list.jd.com/list.html?cat=1318%2C12099%2C9756&isList=1&page=7&s=177&click=0&log_id=1699882602865.5403'
    ]

    def __init__(self):
        self.headers = {
            "authority": "list.jd.com",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "accept-language": "zh-CN,zh;q=0.9",
            "cache-control": "no-cache",
            "pragma": "no-cache",
            "sec-ch-ua": "\"Google Chrome\";v=\"119\", \"Chromium\";v=\"119\", \"Not?A_Brand\";v=\"24\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "none",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
        }
        self.cookies = {
            "__jdu": "1389728386",
            "areaId": "15",
            "shshshfpa": "7faa6132-9432-dd9f-94f6-48f7a986da30-1697177625",
            "shshshfpx": "7faa6132-9432-dd9f-94f6-48f7a986da30-1697177625",
            "_pst": "jd_662db017b1c2a",
            "unick": "jd_662db017b1c2a",
            "pin": "jd_662db017b1c2a",
            "_tp": "Gx1VSaE1gJtrydlVgEvX77S1jtxkCjbBwjB8uwktxwo%3D",
            "user-key": "6fe68553-6b09-4a63-95fd-0edcaa426d90",
            "unpl": "JF8EAJpnNSttWEMGARNQHxAVH1pRWwgKHEcFZjdRAV9dG1AGEwEcFEB7XlVdXxRLFx9uYBRUW1NLUw4aBisSEXteU11bD00VB2xXXAQDGhUQR09SWEBJJV1QV1QMQhIDaGAFZG1bS2QFGjIbEBlDW1dXXwFMJwJfYDVkbVBNVwETBysTIEptFgoBDEoRBG5kSFRfUUNSBhIAEhUgSm1X",
            "__jdv": "76161171|haosou-search|t_262767352_haosousearch|cpc|15885841661_0_19c59c534e644d3fa78aed34a529267a|1699262166611",
            "ipLoc-djd": "15-1250-1251-44548",
            "joyya": "1699509206.1699509284.19.02m59oh",
            "__jda": "122270672.1389728386.1699261912.1699509179.1699880080.6",
            "jsavif": "1",
            "avif": "1",
            "mba_muid": "1389728386",
            "TrackID": "1Gtw12BEFaB2CfHvNdRGcs5rt9cDpWtu_JLA0zWAEQB9YqnH8u55U8ZHM12WIKweVdRqiMfzLtYy_BLhhDUp3aOn6yyepBchHo-QduDVBD5s",
            "thor": "358CB62CC5D0084873A7996A1EDF175887312EDF1EDA706DA6C360245A8FE5D773E901F7CB552DECC02D19507A444276C7A451CF96FCDBE6E80276C627AAC3E12807BFC2D87EA8031010AD1A527B2E689507B0D85523830F36A5CAFDD9F2E273969311701E3920B3DBDB7C6DFAA5D5191915DDC19815ECC60A9DFC0500B8735D296D0B420EBD4B9F66731B7A46A1F6C62B2E990F49CE32B12CB6D2F7666B8AAB",
            "flash": "2_dTShdL4ILyt7PW_w5aZBlE1nw3Qv1OClc6IvUGRPxqpIgRNm05FwLiRtqsDjamMoXyUkQpJZKjDKlbNrOdaVZQ196Ob6c2ccgMrG-bQAV35*",
            "pinId": "oukm6lTRtzBj9FWB-moGNbV9-x-f3wj7",
            "xapieid": "jdd03TOYU2YFJAUBBR4AKXYLN6LJDCGE34Z2GSSZR6IPV2ANKL2RML4MIEB3A534ASMSKLLC4F456JRDR5P6ECTP2RSATLEAAAAMLZDKPGVYAAAAADKLH63HU45VBGAX",
            "__jdc": "122270672",
            "__jdb": "122270672.14.1389728386|6.1699880080",
            "shshshsID": "e49df6bb23394116a50e702c6043381a_6_1699881853744",
            "3AB9D23F7A4B3CSS": "jdd03TOYU2YFJAUBBR4AKXYLN6LJDCGE34Z2GSSZR6IPV2ANKL2RML4MIEB3A534ASMSKLLC4F456JRDR5P6ECTP2RSATLEAAAAMLZDNKCXYAAAAACMOX25ERVACRDAX",
            "_gia_d": "1",
            "shshshfpb": "AAi6i2siLEqphMpQy3Z-U9kj3qYbaMBaXF3YlfwAAAAA",
            "3AB9D23F7A4B3C9B": "TOYU2YFJAUBBR4AKXYLN6LJDCGE34Z2GSSZR6IPV2ANKL2RML4MIEB3A534ASMSKLLC4F456JRDR5P6ECTP2RSATLE"
        }
        self.page = 1
        self.current_page = 1

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse, cookies=self.cookies, headers=self.headers)

    def parse(self, response, **kwargs):
        divs = response.xpath('//*[@id="J_goodsList"]/ul/li/div')
        for div in divs:
            item = JdItem()
            # （标题（title） 价格(price) 颜色(color) 尺码(size) 网站货号(sku) 详情(details) 大图的URL (img_urls)
            title = div.xpath('./div[4]/a/em/text()').get()
            price = div.xpath('./div[3]/strong/i/text()').get()
            img_urls = div.xpath('./div[1]/a/img/@data-lazy-img').get()
            spu = div.xpath('./div[8]/@id').get().replace("J_pro_", '')
            detail_url = f'https://item.jd.com/{spu}.html'
            item['title'] = title
            item['price'] = price
            item['img_urls'] = img_urls
            item['spu'] = spu
            yield scrapy.Request(url=detail_url, callback=self.parse_detail, cookies=self.cookies, headers=self.headers,
                                 meta={'item': item})
            # https://list.jd.com/list.html?cat=1318%2C12099%2C9756&isList=1&page=1&s=1&click=0&log_id=1699365198620.5102 第一页
            # https://list.jd.com/list.html?cat=1318%2C12099%2C9756&isList=1&page=3&s=58&click=0&log_id=1699365212132.2477 第二页
            # https://list.jd.com/list.html?cat=1318%2C12099%2C9756&isList=1&page=5&s=117&click=0&log_id=1699365238677.7320 第三页
            # https://list.jd.com/list.html?cat=1318%2C12099%2C9756&isList=1&page=7&s=177&click=0&log_id=1699365270926.1981 第四页

    def parse_detail(self, response, **kwargs):
        print("开始解析详情页")
        item = response.meta['item']
        # 颜色(color) 尺码(size)
        sizes = response.xpath('//*[@id="choose-attr-2"]/div[2]/div/@data-value').extract()
        # print(size)
        colors = response.xpath('//*[@id="choose-attr-1"]/div[2]/div/@data-value').extract()
        # print(colors)
        skus = response.xpath('//*[@id="choose-attr-1"]/div[2]/div/@data-sku').extract()
        item['color'] = colors
        item['size'] = sizes
        item['sku'] = skus
        yield item
