import datetime
from itemadapter import ItemAdapter
import psycopg2


class CrawlerLyricsPipeline:
    def __init__(self, database):
        self.database = database

    @classmethod
    def from_crawler(cls, crawler):
        settings = crawler.settings
        print(settings)
        database = {
            'host': settings.get('DATABASE')['host'],
            'user': settings.get('DATABASE')['user'],
            'password': settings.get('DATABASE')['password'],
            'database': settings.get('DATABASE')['database'],
            'port': settings.get('DATABASE')['port'],
        }
        return cls(database)
    
    def open_spider(self, spider):
        self.connection = psycopg2.connect(**self.database)
        self.cur = self.connection.cursor()
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS catholic_lyrics(
                id serial PRIMARY KEY,
                title VARCHAR(250), 
                author VARCHAR (250), 
                lyric TEXT, 
                cifra TEXT, 
                link_ref VARCHAR(250)
            );
            """)
    def close_spider(self, spider):
        finish_time = datetime.now()
        elapsed_time = finish_time - self.start_time
        spider.log(f"Spider ran for: {elapsed_time}")
        self.cur.close()
        self.connection.close()
    
    def process_item(self, item, spider):
        try:
            self.cur.execute(
                "insert into catholic_lyrics(title, author, lyric, cifra, link_ref) values(%s,%s,%s,%s,%s)", 
                (item['title'], item['author'], item['lyric'], item['cifra'], item['link_ref']))
            self.connection.commit()
        except:
            self.connection.rollback()
            raise
        return item
