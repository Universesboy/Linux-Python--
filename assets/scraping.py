from bs4 import BeautifulSoup
import requests
url = 'https://www.badminton.ca/ranking/category.aspx?id=36611&category=1994&p=1&ps=100'
page = requests.get(url) 
soup = BeautifulSoup(page.text, 'html')
# print(soup)
table = soup.find('table', class_='ruler')
# print(table)
world_titles = soup.find_all('th')
# print(world_titles)
world_titles_stripped = [title.strip() for title in world_titles if title is not None]
print(world_titles_stripped)
# import pandas as pd
# df = pd.DataFrame(columns = world_table_titles)
# df
# column_data = table.find_all('tr')
# for row in column_data[2:]:
#     row_data = row.find_all('td')
#     individual_row_data = [data.text.strip() for data in row_data]
#     cleaned_row_data = [item for item in individual_row_data if item.strip()]
# #length = len(df)
# #df.loc[length] = individual_row_data
# 
#     print (cleaned_row_data )
# df
# df.to_csv('', index = False)
