original_url = "https://yahoo-education.myguide.hk/d/oversea/expert/wong/page/"
import urllib
import BeautifulSoup
import re
Soup = BeautifulSoup.BeautifulSoup
count = 0
while count <= 1:
    count = count + 1
    weburl = original_url+str(count)+"/"
    page = urllib.urlopen(weburl).read()
    soup = Soup(page)
    list = soup.findAll(True, attrs ={"class":["question","answer"]})
    for i in list:
        s = str(i)
        start_q = s.find("question")
        end_q = s.find("span>發問者".decode("utf8"))
        start_a = s.find("answer")
        end_a = s.find("</span></div>")
        question = s[start_q:end_q]
        answer = s[start_a:end_a]
        print ("Q",count,":",question)
        print ("A", count,":",answer)
        


