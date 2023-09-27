from bs4 import BeautifulSoup
import requests

page = requests.get('https://www.badmintonalberta.ca/page/11046/PLAYER-PROFILES-Alberta') # Getting page HTML through request
soup = BeautifulSoup(page.content, 'html.parser') # Parsing content using beautifulsoup
soup.find('table')
soup.find_all('table')[1]
soup.find('table', class_ = 'ruler')
table = soup.find_all('table')[1]
print(table)
world_titles = table.find_all('th')
world_titles
world_table_titles = [title.text.strip() for title in world_titles]

print(world_table_titles)
import pandas as pd
df = pd.DataFrame(columns = world_table_titles)

df
column_data = table.find_all('tr')
for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    
    length = len(df)
    df.loc[length] = individual_row_data
df
df.to_csv(r'/home/colin/Desktop/Python/assets/player.csv', index = False)
