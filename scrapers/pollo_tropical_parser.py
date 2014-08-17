from bs4 import BeautifulSoup
import urllib2
import json
import codecs

def check_null(n,img):
    try:
        return img[n]
    except IndexError:
        return ""

f = urllib2.urlopen('http://pollotropical.com/menus/')
doc = BeautifulSoup(f.read())
urls = doc.find_all("a",class_="menu-category-link")
output=[]
scrape_url=[]
for url in urls:
    scrape_url.append(url['href'])
scrape_url.remove('/menu-group/tropichops/')
scrape_url.remove('/menu-group/family-meals/')
scrape_url.remove('/menu-group/kids-meals/')
scrape_url.remove('/menu-group/side-dishes/')



for url in scrape_url:
    print 'Running: ' + url
    f = urllib2.urlopen('http://pollotropical.com'+url)
    doc = BeautifulSoup(f.read())
    texts = doc.find_all("div", class_="entry-content")

    for text in texts:
        temp = dict([('name',text.find("h2", class_="entry-title").string),
            ('description',text.find("p").string),
            ('image',text.find("img")['src']),
            ('category',doc.find("h1",class_="post-title").string),
            ('restaurant','Pollo Tropical')
            ])
        output.append(temp)

#code for scraping side dishes

f = urllib2.urlopen('http://pollotropical.com/menu-group/side-dishes/')
print 'Running: '+'http://pollotropical.com/menu-group/side-dishes/'
doc = BeautifulSoup(f.read())
texts=doc.find_all("div", class_="entry-content")
img_list=doc.find_all("li", class_="three-q-right-image")
imgs=[]
for item in img_list:
    imgs.append(item.find("img")['src'])

for x in range(len(texts)):
    temp = dict([('name',texts[x].find("h2", class_="entry-title").string),
            ('description',texts[x].find("p").string),
            ('image',check_null(x,imgs)),
            ('category',doc.find("h1",class_="post-title").string),
            ('restaurant','Pollo Tropical')
            ])
    output.append(temp)

#code for scraping signature sauces

f = urllib2.urlopen('http://pollotropical.com/menu-group/signature-sauces/')
print 'Running: '+'http://pollotropical.com/menu-group/signature-sauces/'
doc = BeautifulSoup(f.read())
texts=doc.find_all("div", class_="entry-content")
img_list=doc.find_all("li", class_="three-q-right-image")
imgs=[]
for item in img_list:
    imgs.append(item.find("img")['src'])
for x in range(len(texts)):
    temp = dict([('name',texts[x].find("h2", class_="entry-title").string),
            ('description',texts[x].find("p").string),
            ('image',check_null(x,imgs)),
            ('category',doc.find("h1",class_="post-title").string),
            ('restaurant','Pollo Tropical')
            ])
    output.append(temp)


#code for scraping family meals

f = urllib2.urlopen('http://pollotropical.com/menu-group/family-meals/')
print 'Running: '+'http://pollotropical.com/menu-group/family-meals/'
doc = BeautifulSoup(f.read())
divs=doc.find_all("div", class_="right-content-area")
for div in divs:
    heads=div.find_all("h4")
for x in range(len(heads)):
    temp = dict([('name',heads[x].string),
            ('description',""),
            ('image',""),
            ('category',doc.find("h1",class_="post-title").string),
            ('restaurant','Pollo Tropical')
            ])
    output.append(temp)


f = urllib2.urlopen('http://pollotropical.com/menu-group/kids-meals/')
print 'Running'+'http://pollotropical.com/menu-group/kids-meals/'
doc = BeautifulSoup(f.read())
texts=doc.find_all("div", class_="entry-content")

for text in texts:
    temp = dict([('name',text.find("h2",class_="entry-title").string),
            ('description',''),
            ('image',''),
            ('category',doc.find("h1",class_="post-title").string),
            ('restaurant','Pollo Tropical')
            ])
    output.append(temp)

#writing output to file
f=codecs.open('pollotropical.json', encoding='utf-8', mode='w')

json.dump(output, f, sort_keys=True, indent=4, separators=(',', ':'))
f.close()
#print json.dumps(output, sort_keys=True, indent=4, separators=(',', ':'))





