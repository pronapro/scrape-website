#import packages 
import requests 
from bs4 import BeautifulSoup
import pandas as pd 

#send request to website 
url = "https://en.wikipedia.org/wiki/List_of_national_independence_days"
html_content = requests.get(url).text

#fetch the data using beautiful soup 
    #parse the data
soup = BeautifulSoup(html_content, "lxml")
#print(soup.title.text)
#analyze the tags 
tables = soup.find_all("table", class_="wikitable sortable")
print(len(tables))
#print(tables)
"""
#print(tables[0].find_all('tr'))
for row in tables[0].find_all('tr'):
    cells =row.find_all("th")
    if len(cells)!=0:
        for i in cells:
            print(i.text)
##
"""

country =[]
name_of_holiday =[]
date_of_holiday =[]
year_of_event =[]
independence_from =[]
event_notes =[]

#tbody
for row in tables[0].find_all('tr'):
    cells =row.find_all("td")
    if len(cells) ==6:
        country.append(cells[0].text.replace('\n', '').strip())
        name_of_holiday.append(cells[1].text.replace('\n', '').strip())
        date_of_holiday.append(cells[2].text.replace('\n', '').strip()) 
        year_of_event.append(cells[3].text.replace('\n', '').strip())
        independence_from.append(cells[4].text.replace('\n', '').strip())
        event_notes.append(cells[5].text.replace('\n', '').strip())                

#tfooter 
print(country)

#output 
df = pd.DataFrame({

'Country': country,
'Name of holiday': name_of_holiday,
'Date of holiday': date_of_holiday,
'Year of event':year_of_event,
'Independence from':independence_from,
"Event commemorated and notes":event_notes

})
df.to_csv('indepence_dates.csv', index=False)

