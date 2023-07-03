# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import psycopg2

class PostgresPipeline:
    def __init__(self):
        hostname = "postgresql-db"
        username = "postgres"
        password = "password"
        database = "postgres"

        self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
        self.cur = self.connection.cursor()

        self.cur.execute("CREATE TABLE IF NOT EXISTS sreality_properties (id SERIAL PRIMARY KEY, title VARCHAR(255) NOT NULL, image_urls TEXT[])")

    def process_item(self, item, spider):
        self.cur.execute(f"INSERT INTO sreality_properties (title, image_urls) VALUES ('{item['title']}', ARRAY{item['img_urls']})")
        self.connection.commit()
        return item
    
    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()