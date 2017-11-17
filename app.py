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
for name in names:
  if name.text.strip().encode('utf8') != '':
    name_after_splitted = name.text.strip().split('\n')
    
    for x in range(0, len(name_after_splitted)):
      name_after_splitted[x] = name_after_splitted[x].encode('utf8')
    result_name.append([name_after_splitted[:1], name_after_splitted[1:len(name_after_splitted)]])

disease_detail = []
result_symptoms = []
result_causes = []
result_comments = []
result_managements = []
symptoms = soup.find_all('div', class_='symptoms')
causes = soup.find_all('div', class_='cause')
comments = soup.find_all('div', class_='comments')
managements = soup.find_all('div', class_='management')
# print symptoms
for symptom in symptoms:
  if symptom.text.strip().encode('utf8') != '':
    symptom_after_splitted = symptom.text.strip().encode('utf8')
    result_symptoms.append(symptom_after_splitted)
# print causes
for cause in causes:
  if cause.text.strip().encode('utf8') != '':
    cause_after_splitted = cause.text.strip().encode('utf8')
    result_causes.append(cause_after_splitted)
# print comments
for comment in comments:
  if comment.text.strip().encode('utf8') != '':
    comment_after_splitted = comment.text.strip().encode('utf8')
    result_comments.append(comment_after_splitted)
# print managements
for management in managements:
  if management.text.strip().encode('utf8') != '':
    management_after_splitted = management.text.strip().encode('utf8')
    result_managements.append(management_after_splitted[23:])

for i in range(0, len(result_name)):
  result_name[i].append(result_symptoms[i])
  result_name[i].append(result_causes[i])
  result_name[i].append(result_comments[i])
  result_name[i].append(result_managements[i])

descriptions = soup.find_all('div', class_='info ')
print descriptions
# for description in descriptions:
#   if description.text.strip().encode('utf8') != '':
#     description_after_splitted = description.text.strip().encode('utf8')
#     print description_after_splitted
# print result_symptoms
# print result_causes
# print result_comments
# print result_managements

# print len(result_name)
# print len(symptoms)
# print len(causes)
# print len(comments)
# print len(managements)