from requests_html import HTMLSession
from bs4 import BeautifulSoup

url = 'https://www.topmba.com/emba-rankings/global/2018'


ses  = HTMLSession()
res  = ses.get(url)

res.html.render(sleep = 5, timeout = 10.0)

soup = BeautifulSoup(res.html.html, "html.parser") 
  

data =  []
table = soup.find('table', {'id': "qs-rankings"})
table_body = table.find('tbody')
rows = table_body.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele])
print(data)
