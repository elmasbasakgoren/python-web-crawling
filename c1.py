from bs4 import BeautifulSoup
import requests

def getTextFromURL(url):
   r = requests.get(url)
   soup = BeautifulSoup(r.text, "html.parser")
   unvan= soup.find_all('div',{'class':'aux-content-widget-2'}) #degistirilebilir, find fonksiyonu
   for i in unvan:
       print(i.text)


def parse(url):
    try:
        parsed_url_components = url.split('//')
        sublevel_split = parsed_url_components[1].split('/', 1)
        domain = sublevel_split[0].replace(".", "")
        return domain
    except IndexError:
        print("URL format error!")
getTextFromURL("https://www.imdb.com/title/tt0266697/plotsummary?ref_=tt_ql_stry_3#synopsis")


