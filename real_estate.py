import requests
from bs4 import BeautifulSoup

r = requests.get("http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
c=r.content
soup=BeautifulSoup(c,"html.parser")


all=soup.find_all("div", {"class":"propertyRow"})
x=all[0].find("h4",{"class":"propPrice"}).text.replace(" ","").replace("\n","")
listo=[]
for item in all:
    y=item.find("h4",{"class","propPrice"}).text.replace(" ","").replace("\n","")
    print(y)
    f=item.find_all("span",{"class","propAddressCollapse"})[0].text
    print(f)
    fd=item.find_all("span",{"class","propAddressCollapse"})[1].text
    print(fd)
    try: 
        print(item.find("span",{"class","infoBed"}).find("b").text)
    except:
        print(None)
    try: 
        print(item.find("span",{"class","infoSqFt"}).find("b").text)
    except:
        print(None)
    try: 
        print(item.find("span",{"class","infoValueFullBath"}).find("b").text)
    except:
        print(None)

    try: 
        print(item.find("span",{"class","infoValueHalfBath"}).find("b").text)
    except:
        print(None)
    print(" ")
