
import psycopg2
from itemadapter import ItemAdapter


class PostgresPipeline:
    def open_spider(self, spider):
        hostname = 'localhost'
        username = 'admin'
        password = '1234'
        database = 'postgres'
        self.connection = psycopg2.connect(
            host=hostname, user=username, password=password, 
            dbname=database)
        
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