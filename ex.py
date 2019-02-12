import requests
import string
d={}
print ("retrieving data, please wait")
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
    d[name]=values

print ("please enter length")
L=input()
print ("please enter width")
W=input()
print ("please enter height")
H=input()

litres=round((int(L)*int(W)*int(H)/276)*4.454)
print (str(litres) + " Litres")
ideal_C = 425
ideal_M = 1350
ideal_Al = 8.5

print ("Alkalinity")
Al=float(input())
if Al>d["Alkalinity"][1]:
    print ("-Perform a water change-")
elif Al<d["Alkalinity"][0]:
    diff_Al = ideal_Al - Al
    print ("-Dose Alkalinity- (needs {})".format(diff_Al))
    print ("Dose " + str(round(0.38*litres*diff_Al)) + "ml's")
else:
    print ("-All Well-")



