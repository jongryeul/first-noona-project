import requests
from bs4 import BeautifulSoup
import re
import sqlite3

fdic = {}
list_a = []
list_b = []

for page in range(1, 5):
    url = "https://fine.fss.or.kr/main/fin_tip/dic/financedic.jsp?page="+str(page)
    print(url)

    response = requests.get(url)
    # print(response.text)

    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        ul = soup.select_one('ul.dic_result_list')
        sub = ul.select('li > dl > dt')
        con = ul.select('li > dl > dd')

        for i in sub:
            tmp = i.get_text().strip()
            tmp = re.sub('^[0-9]+. ', '', tmp)
            # print(tmp)
            list_a.append(tmp)

        for i in con:
            tmp = i.get_text().strip()
            list_b.append(tmp)
            # print(tmp)

    else:
        print(response.status_code)

for i in range(len(list_a)):
    fdic[i] = [list_a[i], list_b[i]]

    # print(len(list_a))
    # print()
    # print(fdic)


conn = sqlite3.connect("fdic1.db")
cur = conn.cursor()
conn.execute("create table fss_dic(id integer, name text, content text)")

for i in fdic:
    name = fdic[i][0]
    content = fdic[i][1]

    sql = "insert into fss_dic values (?,?,?)"
    cur.execute(sql, (i, name, content))

conn.commit()
conn.close()