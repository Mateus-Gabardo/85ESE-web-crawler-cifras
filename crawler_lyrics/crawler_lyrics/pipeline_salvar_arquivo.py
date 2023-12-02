class SalvarArquivoPipeline(object):

    def open_spider(self, spider):
        self.file = open('lyrics.txt', 'w', encoding='utf-8')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        selected_attributes = {'title': item['title'], 'lyric': self.removeTag(item['lyric'])}
        line = f'"{selected_attributes["title"]}";"{selected_attributes["lyric"]}"\n'
        self.file.write(line)
        return item

    def removeTag(self, item):
        if item['lyric']:
            item['lyric'] = item['lyric'].replace('\n', '')
        return item
