from django.shortcuts import render
from django.http import HttpResponse 
#from rest_framework.views import APIView
#from rest_framework.response import Response
#from rest_framework import status
from firstapp.models import Uniinf, Program_Highlights
#from firstapp.serializers import universitiesSerializer
from requests_html import HTMLSession
from bs4 import BeautifulSoup
import sqlite3
# Create your views here.

url = 'https://www.topmba.com/emba-rankings/global/2018'

#url of the page we want to scrape 
ses  = HTMLSession()
def getdata(url): 
    res  = ses.get(url)
    # this is just to ensure that the page is loaded 
    res.html.render(sleep = 5, timeout = 20) # render the pages 
    soup = BeautifulSoup(res.html.html, 'html.parser')
    return soup # method returns the html data
soup = getdata(url)

def sortdata(soup):
    data =  []
    table = soup.find('table', {'id': "qs-rankings"})
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])
    return data #  function returns the list of the data
data = sortdata(soup)

Rank = []
Name_of_University = []
City = []
Country = []
for i in range(len(data)):
    for j in range(4):
        if j == 0:
            Rank.append(data[i][j])
        elif j == 1:
            Name_of_University.append(data[i][j])
        elif j == 2:
            City.append(data[i][j])
        elif j == 3:
            Country.append(data[i][j])

conn = sqlite3.connect('top_universities.db')
cur = conn.cursor() 
#  to create table with the sqllite3.
# needed to run the command once.
#cur.execute(''' CREATE TABLE  universities(URank TEXT, UName_of_University TEXT, UCity TEXT, UCountry TEXT)''')

for i in range(len(data)):
    cur.execute(''' INSERT INTO universities VALUES (?, ?, ?, ?)''', (Rank[i], Name_of_University[i], City[i], Country[i]))

conn.commit()
cur.execute('''SELECT * from universities''')
result = cur.fetchall()


def home(request):
    contex = {
        'post' : result
    }
    return render(request, 'home.html', contex)