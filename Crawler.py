import requests
from bs4 import BeautifulSoup
from urllib import request



def spider():
    url= 'http://www.bseindia.com/'
    #url=input("enter the url: ")
    source= requests.get(url)
    plain_text=source.text
    #print(plain_text)
    soup=BeautifulSoup(plain_text,"html5lib")
    Fw = open('Crawler_Result.txt', 'w')

    for link in soup.findAll('a',href=True):
        #href= url + link.get('href')
        href = link.get('href')
        print(href)
        title=link.text

        response = request.urlopen(href)
        response1=response.getcode()
        if (response1 == 200):

            Fw.write(href + " is working\n")
        else:
            Fw.write(href +  " is not working\n")



    Fw.close()



spider()

