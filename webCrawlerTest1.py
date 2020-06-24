import requests
from bs4 import BeautifulSoup

urlPost="https://www.ptt.cc/ask/over18?from=%2Fbbs%2FGossiping%2Findex.html"
urlGet="https://www.ptt.cc/bbs/Gossiping/index.html"

r = requests.Session()
payload ={
    "from":"/bbs/Gossiping/index.html",
    "yes":"yes"
}

rPost = r.post(urlPost,payload)

for i in range(2):
    rGet = r.get(urlGet)
    soup = BeautifulSoup(rGet.text,"html.parser")
    selector = soup.select("div.title a") #標題
    u = soup.select("div.btn-group.btn-group-paging a") #a標籤
    print ("本頁的URL為"+url)
    url = "https://www.ptt.cc"+ u[1]["href"] #上一頁的網址

    for s in selector: #印出網址跟標題
        print(s["href"],s.text)
