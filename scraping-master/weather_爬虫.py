import requests
from lxml import etree
import MySQLdb


conn = MySQLdb.connect(host='localhost', user='root',
                       passwd='mrj123456', db='scraping',charset='utf8')
cur = conn.cursor()


url = 'http://www.weather.com.cn/weather/101210701.shtml'
res = requests.get(url)
tree = etree.HTML(res.text.encode('iso-8859-1'))

for i in range(1, 8):
    day = tree.xpath(
        '//ul[@class="t clearfix"]/li[contains(@class,"skyid")]['+str(i)+']/h1/text()')
    weather = tree.xpath(
        '//ul[@class="t clearfix"]/li[contains(@class,"skyid")]['+str(i)+']/p[@class="wea"]/text()')
    temp = tree.xpath(
        '//ul[@class="t clearfix"]/li[contains(@class,"skyid")]['+str(i)+']/p[@class="tem"]/i/text()')


    cur.execute("INSERT INTO creep_weather (day,weather,temp) VALUES (%s,%s,%s)", (day, weather, temp))
    
cur.close()
conn.commit()
conn.close()

