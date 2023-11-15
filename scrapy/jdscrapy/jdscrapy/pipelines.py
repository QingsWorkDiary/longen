# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import json


class JdscrapyPipeline:

    def __init__(self):
        self.file = open('jdxxxx.json', 'w', encoding='utf-8')
        self.file.write('[')

    def process_item(self, item, spider):
        # 将数据写入到文件中json文件
        # 将item转换成字典
        item = dict(item)
        # 将字典转换成json字符串
        json_str = json.dumps(item, ensure_ascii=False)
        # 将json字符串写入到文件中
        self.file.write(json_str + ',\n')
        return item

    def close_spider(self, spider):
        self.file.write(']')
        self.file.close()
        print('爬虫结束')
        print('保存文件成功')
        print('文件路径：jdxxxx.json')
        print('请在本地查看文件')
