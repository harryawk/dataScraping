from bs4 import BeautifulSoup
import requests

# headers = {'Accept-Encoding': ''}
# page = requests.get('https://plantvillage.org/topics/alfalfa/infos', headers=headers)
page = requests.get('https://plantvillage.org/topics/alfalfa/infos')
# print page.encoding
# print page.text.encode('utf8')
soup = BeautifulSoup(page.text.encode('utf8'), 'html.parser')

names = soup.find_all('h4')
# print names
result_name = []
result_latin_name = []
for name in names:
  result_name.append(name.text.strip().split('\n')[0])
  result_latin_name.append(name.text.strip().split('\n')[1] if name.text.strip().split('\n')[1] else '')
print result_name
# name = names.text.strip()
# print name.split('\n')