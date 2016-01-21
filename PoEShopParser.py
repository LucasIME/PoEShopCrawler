import urllib2
from BeautifulSoup import BeautifulSoup

class PoEShopParser():
    def __init__(self, targetURL):
        self.targetURL = targetURL

    def getItemAndPricesList(self):
        responseList  = []
        html = urllib2.urlopen(self.targetURL)
        wholePageSoup = BeautifulSoup(html)
        for itemSection in wholePageSoup.findAll('div', {'class': lambda x : x and 'shopItemBase' in x.split()}):
            itemSoup = BeautifulSoup(str(itemSection))
            name = itemSoup.find('a', {'class':'name'})
            priceHtml = itemSoup.find('div', {'class':'price'})
            priceSoup =  BeautifulSoup(str(priceHtml))
            price = priceSoup.div.find(text=True, recursive=False)
            responseList.append( (name.string, price) )
        return responseList