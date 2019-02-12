import requests
import string
d={}

page = requests.get("https://fritzaquatics.com/products/fritz-rpm-reef-pro-mix")

from bs4 import BeautifulSoup
soup=BeautifulSoup (page.content,"html.parser")
soup.find_all("p")

for item in soup.find_all("p")[3:6]:
    #print (type(soup.find_all("p")))
    lst=item.get_text().split()
    lst2=lst[1].split("-")
    name = lst[0][:-1]
    begin = float(lst2[0])
    end = float(lst2[1])
    values=(begin,end)
    #print (parameter)
    #print (begin)
    #print (end)
    d[name]=values
    
print (d)
    
    #D={parameter:begin,parameter:end}
    #print (D)





# import requests
# page = requests.get ("http://dataquestio.github.io/web-scraping-pages/simple.html")
# print (page)