import requests
from lxml import etree
import MySQLdb

conn = MySQLdb.connect(host='localhost', user='root',
                       passwd='mrj123456', db='scraping',charset='utf8')

cur = conn.cursor()

for i in range(0, 10):
    url = 'https://movie.douban.com/top250?start='+str(i*25)+'&filter='
    res = requests.get(url)

    tree = etree.HTML(res.text)
    top250 = tree.xpath('//span[@class="title"][1]/text()')
    cur.execute("INSERT INTO creep_movie (url,content) VALUES (%s,%s)", (url, str(top250)))

cur.close()
conn.commit()
conn.close()
