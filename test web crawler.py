import requests
from bs4 import BeautifulSoup
import json

# r = requests.get("https://www.ptt.cc/bbs/MobileComm/index.html") #將此頁面的HTML GET下來
# soup = BeautifulSoup(r.text,"html.parser") #將網頁資料以html.parser
# sel = soup.select("div.title a") #取HTML標中的 <div class="title"></div> 中的<a>標籤存入sel
# for s in sel:
#     print(s["href"], s.text)


#test = open("spider/pet/test.txt","w",encoding='UTF-8')
p = requests.Session()
url = requests.get("https://www.dcard.tw/f/pet")
soup = BeautifulSoup(url.text, "html.parser")
sel = soup.select("div.PostList_entry_1rq5Lf a.PostEntry_root_V6g0rd")
a=[]
for s in sel:
    a.append(s["href"])
    #print(s["href"], s.text)

url = "https://www.dcard.tw"+ a[2]



j=0
q=0
for i in a[2:]:
    url = "https://www.dcard.tw"+i
    j+=1
    print ("第",j,"頁的URL為:"+url)
    #file.write("temperature is {} wet is {}%\n".format(temperature, humidity))
    #test.write("第 {} 頁的URL為: {} \n".format(j,url))
    url=requests.get(url)
    soup = BeautifulSoup(url.text,"html.parser")
    sel_jpg = soup.select("div.Post_content_NKEl9d div div div img.GalleryImage_image_3lGzO5")
    for c in sel_jpg:
        q += 1
        print("第", q, "張:", c["src"])
        # test.write("%\n""第 {} 張: {} \n".format(q,c["src"]))
        pic = requests.get(c["src"])
        img2 = pic.content
        pic_out = open("spider/pet/" + str(q) + ".png", 'wb')
        pic_out.write(img2)
        pic_out.close()



print("爬蟲結束")