from django.shortcuts import render
from django.http import HttpResponse
from firstapp.models import Uniinf, Program_Highlights
import requests 
from bs4 import BeautifulSoup 
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
import time 
import sqlite3
# Create your views here.


#url of the page we want to scrape 
url = "https://www.topmba.com/emba-rankings/global/2018"
  
# initiating the webdriver. Parameter includes the path of the webdriver. 
#path = r'C:\Users\putwi\Desktop\chromedriver_win32\chromedriver'
driver = webdriver.Chrome(r'C:\Users\tahir\Desktop\chromedriver_win32\chromedriver.exe')  
driver.get(url)  
  
# this is just to ensure that the page is loaded 
time.sleep(5)
html = driver.page_source
  
# this renders the JS code and stores all 
# of the information in static HTML code. 
  
# Now, we could simply apply bs4 to html variable
soup = BeautifulSoup(html, "html.parser") 
data =  []
table = soup.find('table', {'id': "qs-rankings"})
table_body = table.find('tbody')
rows = table_body.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele])



driver.close()
conn = sqlite3.connect('top_universities.db')
cur = conn.cursor() 
#  to create table with the sqllite3.
# needed to run the command once.
#cur.execute(''' CREATE TABLE  universities(Rank TEXT, Name_of_University TEXT, City TEXT, Country TEXT)''')

def home(request):
    contex = {
        'post' : data
    }
    return render(request, 'home.html', contex)
