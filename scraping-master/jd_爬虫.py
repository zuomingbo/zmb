import requests
from lxml import etree
import MySQLdb
import time


conn = MySQLdb.connect(host='localhost', user='root',
                       passwd='mrj123456', db='scraping', charset='utf8')
cur = conn.cursor()


def top(n):
    head = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
            'Referer': 'https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&wq=s%27ho&pvid=079534dc90f34f70867214cf53fb5702'
            }
    url = 'https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&cid2=653&cid3=655&page=' + \
        str(2*n+1)+'&click=0'
    res = requests.get(url, headers=head)
    res.encoding = 'utf-8'
    tree = etree.HTML(res.text)
    all_item = tree.xpath('//li[contains(@class,"gl-item")]')

    for item in all_item:
        item_page = 'Page ' + str(n)
        item_name = item.xpath(
            'div/div[@class="p-name p-name-type-2"]/a/em/text()')
        item_price = item.xpath(
            'div/div[@class="p-price"]/strong/i/text()')
        if len(item_price) == 0:
            item_price = item.xpath(
                'div/div[@class="p-price"]/strong/@data-price')
        cur.execute("INSERT INTO creep_jdphone (item_page,item_name,item_price) VALUES (%s,%s,%s)",
                    (item_page, str(' '.join(item_name)), str(' '.join(item_price))))


def last(n):
    head = {
        'authority': 'search.jd.com',
        'method': 'GET',
        'path': '/s_new.php?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&cid2=653&cid3=655&page=2&s=28&scrolling=y&log_id=1555486674.48819&tpl=3_M&show_items=100004544998,100000177756,100002425279,8735304,100003332220,100001467225,7652013,100001364160,44221160776,100003936976,100000650837,7651927,5089235,7652089,7437786,100000349372,100003475378,100000773875,100002493099,5089225,7437708,100000287145,100004363706,7299782,5089273,100000822981,7081550,100003884564,7437784,3133811',
        'scheme': 'https',
        'cookie': 'xtest=451.cf6b6759; shshshfp=0f0d6a30ca3a154ff0dc3410cf0b6137; shshshfpa=71786a34-e8a2-6eb9-aa74-5e36a6c67e81-1555481306; areaId=15; ipLoc-djd=15-1233-42324-0; __jdc=122270672; __jdv=122270672|direct|-|none|-|1555481307588; __jdu=15554813075871930371411; shshshfpb=i3S767V3knJNVejZRi%2FwD3Q%3D%3D; 3AB9D23F7A4B3C9B=VF2QPS6TVX6VJCH6DE2GFZLJO57KXUYVBULOZ67V5A42BTI2K244PYYQUIH2YG3ALTDT4BOD2PTLKTOBWODWQWLI34; __jda=122270672.15554813075871930371411.1555481308.1555481308.1555484694.2; rkv=V0300; qrsc=3; shshshsID=66b9b3e9b41aee087d5c0f681a3714c0_18_1555486644938; __jdb=122270672.18.15554813075871930371411|2.1555484694',
        'referer': 'https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&cid2=653&cid3=655&page=1&s=3&click=0',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest'
    }

    a = time.time()
    b = '%.5f' % a
    url = 'https://search.jd.com/s_new.php?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&cid2=653&cid3=655&page=' + \
        str(2*n)+'&s='+str(48*n-20)+'&scrolling=y&log_id='+str(b)
    res = requests.get(url, headers=head)
    res.encoding = 'utf-8'
    tree = etree.HTML(res.text)
    all_item = tree.xpath('//li[contains(@class,"gl-item")]')

    for item in all_item:
        item_page = 'Page ' + str(n)
        item_name = item.xpath(
            'div/div[@class="p-name p-name-type-2"]/a/em/text()')
        item_price = item.xpath(
            'div/div[@class="p-price"]/strong/i/text()')
        if len(item_price) == 0:
            item_price = item.xpath(
                'div/div[@class="p-price"]/strong/@data-price')
        cur.execute("INSERT INTO creep_jdphone (item_page,item_name,item_price) VALUES (%s,%s,%s)",
                    (item_page, str(' '.join(item_name)), str(' '.join(item_price))))


for i in range(1, 11):
    top(i)
    last(i)
    cur.execute("INSERT INTO creep_jdphone (item_page,item_name,item_price) VALUES (%s,%s,%s)",
                ('--------', '---------------------------------------------------------------------------------------------', '---------'))

cur.close()
conn.commit()
conn.close()
