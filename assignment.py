import requests
d={}

print ("retrieving data, please wait")
page = requests.get("https://fritzaquatics.com/products/fritz-rpm-reef-pro-mix")
#ian's a banana
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

print ()
print ("please enter length")
L=input()
print()
print ("please enter width")
W=input()
print ()
print ("please enter height")
H=input()
print ()

litres=round((int(L)*int(W)*int(H)/276)*4.454)
print (str(litres) + " Litres")
ideal_C = 425
ideal_M = 1350
ideal_Al = 8.5
print ()

print ("Ammonia")
A=int(input())
if A>0:
    print ("-Perform a water change-")
if A==0: print ("-All Well-")

print ()

print ("NitrItes")
nI=int(input())    
if nI>0:  
    print ("-Perform a water change-")
if nI==0: print ("-All Well-")

print ()

print ("NitrAtes")
nA=int(input())
if nA>20:  
    print ("-Perform a water change-")
if nA in range (0,21):
    print ("-All Well-")

print ()

print ("Phosphate")
P=float(input())
if P>0.03:  
   print ("-Perform a water change-")
if P>0 and P<0.029: print ("-All Well-")

print ()

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

print ()

print ("Calcium")
C=int(input())
if C>d["Calcium"][1]:
    print ("-Perform a water change-")
elif C<d["Calcium"][0]:
    diff_C = ideal_C - C
    print ("-Dose Calcium- (needs {})".format(diff_C))
    print ("Dose " + str(round(0.0074*litres*diff_C)) + " ml's")
else:
    print ("-All Well-")

print ()

print ("Magnesium")
M=int(input())
if M>d["Magnesium"][1]:  
   print ("-Perform a water change-")
elif C<d["Magnesium"][0]:
    diff_M = ideal_M - M
    print ("-Dose Magnesium- (needs {})".format(diff_M))
    print ("Dose " + str(round(0.017*litres*diff_M)) + " ml's")
else:
    print ("-All Well-")

print ()