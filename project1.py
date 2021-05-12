from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.index.go.kr/unify/idx-info.do?idxCd=4262")

soup = BeautifulSoup(html,"lxml")

div = soup.find_all('div',{'class':'content right'})

table = div[0].find_all('table',{'id':'t_Table_426201'})

tbody = table[0].find_all('tbody')

tr = tbody[0].find_all('tr')

list = []
count = 0
cyc = 0
for i in tr:
    list2 = []
    td = tr[cyc].find_all('td')
    cyc += 1
    if count == 1:
        break

    for n in td:
        m = n.get_text()
        print(m)
        m = m.replace('\n',' ')
        list2.append(m)

    print('')
    list.append(list2)
    count += 1