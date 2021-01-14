import requests 
from bs4 import BeautifulSoup 
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
import time 
import sqlite3


#if __name__ == '__main__':
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
#print(data)
        #print(all_divs)


#print(data[0][0], data[0][1])
#Rank = data[0][0] # rank of the university 
#Name_of_University = data[0][1] # Name of University 
#Name_of_Coourse = []
#Link_to_the_program = []
#City = [data[0][2]]
#Country = [data[0][3]]

#print(data[0][:])

conn = sqlite3.connect("top_universities.db")
cur =  conn.cursor()
# first needed to create table then commented the create table code.
#cur.execute(''' CREATE TABLE Universities(Rank TEXT, Name_of_University TEXT, City TEXT, Country TEXT)''')
#for iteam in data:
#cur.execute(''' INSERT INTO Universities VALUES(?, ?, ?, ?, ?, ?)''', (Rank, Name_of_University, Name_of_Coourse, Link_to_the_program_highlights, City,Country))
  
driver.close() # closing the webdriver 

Rank = []
Name_of_University = []
City = []
Country = []
for i in range(len(data)):
    for j in range(7):
        if j == 0:
            Rank.append(data[i][j])
        elif j == 1:
            Name_of_University.append(data[i][j])
        elif j == 2:
            City.append(data[i][j])
        elif j == 3:
            Country.append(data[i][j])
#print(Rank)
#print(Name_of_University)
#print(City)
#print(Country)

#for j, v in enumerate(data):
#    print(v)

for i in range(len(data)):
    cur.execute(''' INSERT INTO universities VALUES (?, ?, ?, ?)''', (Rank[i], Name_of_University[i], City[i], Country[i]))
conn.commit()

print("complet")
            


            

