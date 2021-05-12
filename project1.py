import matplotlib.pyplot as plt
import matplotlib
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
    if count == 2:
        break

    for n in td:
        m = n.get_text()
        print(m)
        m = m.replace('\n',' ')
        list2.append(m)

    print('')
    list.append(list2)
    count += 1

list_t1 = list[0]
list_j = list[1]

list_t = []
for i in list_t1:
    i = i.replace(',','')
    i = int(i)
    list_t.append(i)

list_j = [float(i) for i in list_j]

list_y = []
for y in range(2009,2020):
    list_y.append(y)

print(list_y)
print(list_t)
print(list_j)

matplotlib.rcParams['axes.unicode_minus']=False
plt.rc('font', family='Malgun Gothic')
plt.plot(list_y,list_t,color='purple')
plt.plot(list_y,list_j,color='lightblue')
plt.title('전체 형법범죄')
plt.xticks(list_y)
plt.xlabel('연도')
plt.ylabel('인구 십만 명당 건수')
plt.show()