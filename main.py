from config import *
from PoEMailSender import PoeMailSender
from PoEShopParser import PoEShopParser

def main():
    shopParser = PoEShopParser(shopOffersURL)
    itemPriceList = shopParser.getItemAndPricesList()
    mailSender = PoeMailSender(sourceEmail)
    for name,price in itemPriceList:
        print name, price
        bodyText  =  "The item %s is in discount! It now costs %s Coins!\n" % (name, price)
    mailSender.connect()
    mailSender.sendMail("meireles31@msn.com", "PoE Discounts!", bodyText)
    mailSender.disconnect()

if __name__ == "__main__":
    main()