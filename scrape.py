import requests;
import numpy as np
import sqlite3
from bs4 import BeautifulSoup;

r = requests.get('https://listfist.com/list-of-one-piece-arcs');

soup = BeautifulSoup(r.content, 'html.parser');

s = soup.find('tbody')

arcs = []
for line in s.find_all("td", class_='col-2 even'):
    arcs.append(line.text)

startChapters = []
for line in s.find_all("td", class_='col-3 odd'):
    startChapters.append(line.text)

startEpisodes = []
for line in s.find_all("td", class_='col-7 odd'):
    startEpisodes.append(line.text)

# combine lists
data = [list(a) for a in zip(arcs, startChapters)]
data = np.array(data)

# remove filler arcs
search = '0'
col = 1
data = data[~(data[:,col] == search),:]

# get end chapters
endChapters = []
for i in range(len(data) - 1):
    endChapters.append(int(data[i + 1][1]) - 1)
endChapters.append(0)

# combine lists into one
arcs = [i[0] for i in data]
start = [i[1] for i in data]
currentChapter = start

data = [list(a) for a in zip(arcs, start, endChapters, currentChapter)]

for arc in data:
    arc[1] = int(arc[1])

#for arc in data:
#    print(arc)

connection = sqlite3.connect('manga.db')

cursor = connection.cursor()

table = "create table arc (title varchar(255) not null, start int, end int, current int);"

cursor.execute(table)
cursor.executemany("insert into arc values (?,?,?,?)", data)
connection.commit()

cursor.execute("select * from arc")
rows = cursor.fetchall()
for row in rows:
    print(row)