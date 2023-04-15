import requests
from bs4 import BeautifulSoup

def ret_ssilka(url, limit=1):
    eminem=[]
    page=requests.get(url)
    soup=BeautifulSoup(page.content, "html.parser")
    header_post=soup.find_all("a", class_="tm-title__link", limit=limit)
    for i in header_post:
        i=str(i)
        nmb = i.find('href="')+6
        nmb2 = i.find('"><span>')
        eminem.append(i[nmb:nmb2])
    retr="https://habr.com"+str(eminem[-1])
    return retr




def spisok(url, limit=5):
    eminem=[]
    page=requests.get(url)
    soup=BeautifulSoup(page.content, "html.parser")
    header_post=soup.find_all("a", class_="tm-title__link", limit=limit)
    chislo=-10
    for i in header_post:
        spisochek={}
        i=str(i)
        nmb=i.find("<span>")+6
        eminem.append(i[nmb:-11])
        stroka = "\n \n"
        for i in eminem:
            chislo += 1
            stroka +=str(chislo) + ": "+ i + " \n "
            spisochek[chislo]=i
    return stroka

def tekst(url, limit=910):
    retr=""
    page=requests.get(url)
    soup=BeautifulSoup(page.content, "html.parser")
    texts = soup.find_all("p")
    for text in texts:
        retr+=str(text.get_text())
    retr=retr[:limit]
    retr+=f"... Статья была взята с сайта Хабр, оригинал -> \n{url}"
    return retr
