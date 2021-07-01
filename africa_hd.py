#importing necessary packages 
from scrape_africa_gdp import Country
import requests
from bs4 import BeautifulSoup
import pandas as pd

#sending http request to the website we want to scrape 
url = "https://en.wikipedia.org/wiki/List_of_African_countries_by_Human_Development_Index"
html_content = requests.get(url).text
#fetch the data using beautiful soup 
    #parse the data
soup = BeautifulSoup(html_content, "lxml")
print(soup.title.text)
#analyze the tags 
tables = soup.find_all("table", class_="wikitable sortable")
print(len(tables))

#thead
#print(tables[0].find_all('tr'))
for row in tables[0].find_all('tr'):
    cells =row.find_all("th")
    #if len(cells)!=0:
        #print(cells)

Africa_rank =[]
global_rank =[]
Country =[]
HDI =[]
HDI_change =[]
#tbody
for row in tables[0].find_all('tr'):
    cells =row.find_all("td")
    if len(cells) ==5:
        Africa_rank.append(cells[0].text.replace('\n', '').strip())
        global_rank.append(cells[1].text.replace('\n', '').strip())
        Country.append(cells[2].text.replace('\n', '').strip()) 
        HDI.append(cells[3].text.replace('\n', '').strip())
        HDI_change.append(cells[4].text.replace('\n', '').strip())                

#tfooter 
print(Country)

#output 
df = pd.DataFrame({

'Africa rank ': Africa_rank ,
'Global rank': global_rank,
'Country': Country,
'HDI value':HDI,
'Change in HDI value 2018–19':HDI_change

})
df.to_csv('African hdi.csv', index=False)