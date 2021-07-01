#importing necessary packages 
import requests
from bs4 import BeautifulSoup
import pandas as pd

#sending http request to the website we want to scrape 
url = "https://en.wikipedia.org/wiki/List_of_African_countries_by_GDP_(nominal)"
html_content = requests.get(url).text
#fetch the data using beautiful soup 
    #parse the data
soup = BeautifulSoup(html_content, "lxml")
print(soup.title.text)
#analyze the tags 
tables = soup.find_all("table", class_="wikitable sortable")
#print(tables)
#print(tables)

Rank =[]
Country =[]
Nominal_GDP=[]
Nominal_GDP_pc =[]

#print(tables[0].find_all('tr'))
for row in tables[0].find_all('tr'):
    cells =row.find_all("td")
    if len(cells) ==4:
        Rank.append(cells[0].text.replace('\n', '').strip())
        Country.append(cells[1].text.replace('\n', '').strip()) 
        Nominal_GDP.append(cells[2].text.replace('\n', '').strip())
        Nominal_GDP_pc.append(cells[3].text.replace('\n', '').strip())                

#output in format we can use 
df = pd.DataFrame({

'Rank': Rank,
'Country': Country,
'Nominal GDP ($ billions)':Nominal_GDP,
'Nominal GDP per capita (US$)':Nominal_GDP_pc

})
df.to_csv('African gdp.csv', index=False)
