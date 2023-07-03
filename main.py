import crochet
crochet.setup()

from flask import Flask, render_template, request, redirect, url_for
import psycopg2

from scrapy import signals
from scrapy.crawler import CrawlerRunner, CrawlerProcess
from luxonis.spiders.sreality import SrealitySpider
from scrapy.utils.project import get_project_settings

app = Flask(__name__)
crawl_runner = CrawlerRunner()

hostname = "postgresql-db"
username = "postgres"
password = "password"
database = "postgres"

connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
cur = connection.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS sreality_properties (id SERIAL PRIMARY KEY, title VARCHAR(255) NOT NULL, image_urls TEXT[])")

@app.route('/', methods=['GET', 'POST'])
def index():

    data = list()

    if request.method == 'POST':
        if request.form.get('delete_all') == 'Delete all':
            cur.execute("TRUNCATE TABLE sreality_properties")
            connection.commit()
            cur.execute("SELECT * FROM sreality_properties")
            data = cur.fetchall()
        
        elif request.form.get('scrape') == 'Scrape':
            return redirect(url_for('scrape'))

    elif request.method == 'GET':
    
        cur.execute("SELECT * FROM sreality_properties")
        data = cur.fetchall()

    return render_template("index.html", data=data)

@app.route('/scrape')
def scrape():
    scrape_with_crochet()
    return "hi"

@crochet.run_in_reactor
def scrape_with_crochet():
    eventual = crawl_runner.crawl(SrealitySpider)
    eventual.addCallback(finished_scrape)

def finished_scrape():
    print("neki")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)