##First Version of the webscraper

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/global/au-en/p/pl?d=graphics+card'

# Opening the website then closing the website
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# parse the page you downloaded as html
page_soup = soup(page_html, "html.parser")

#After inspecting an element on the page, you parse in the element
# you want and assigning it a varible. in this cause i called it 
# cell
itemcell =  page_soup.findAll("div",{"class":"item-cell"}) 
item = itemcell[0]

filename = "products.csv"
f = open(filename, "w")

headers = "brand, itemname, shipping\n"
f.write(headers)

#drill into the element and scrape what you need from the website
for item in itemcell:
    brand = item.div.div.a.img["title"]
    
    titlebox = item.findAll("a", {"class":"item-title"})
    itemname = titlebox[0].text

    shipping = item.findAll ("li",{"class":"price-ship"})
    shippingrate = shipping[0].text

    print("Brand: " + brand)
    print("Item_Name: " + itemname)
    print("Shpping_Rate: " + shippingrate)

    f.write(brand + "," + itemname.replace(",","|") + "," + shippingrate + "\n")

f.close()

##update