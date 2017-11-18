from bs4 import BeautifulSoup
import requests
from datas import links

from flask import Flask
from flask import request as req
import json
app = Flask(__name__)

# headers = {'Accept-Encoding': ''}
# page = requests.get('https://plantvillage.org/topics/alfalfa/infos', headers=headers)
# page = requests.get('http://plantvillage.org/topics/aloe-vera/infos')
  # return info_id, {'Content-Type': 'application/json'}

@app.route('/')
def get_data():
  info_id = req.args.get('id')
  info_id = int(info_id)
  if (info_id >= len(links)):
    return json.dumps({'message': 'ERROR: link_id have to less than ' + str(len(links))}), {'Content-Type': 'application/json'}
  print info_id
  the_result = {}
  # the_array = []
  # the_array.append({'first_dic': 'first_dic'})
  # # the_array.append({second_dic: 'second_dic'})
  # print the_array
  # return json.dumps(the_array), {'Content-Type': 'application/json'}
  page = requests.get(links[info_id])
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
        name_after_splitted[x] = name_after_splitted[x]
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
      symptom_after_splitted = symptom.text.strip()
      result_symptoms.append(symptom_after_splitted)
  # print causes
  for cause in causes:
    if cause.text.strip().encode('utf8') != '':
      cause_after_splitted = cause.text.strip()
      result_causes.append(cause_after_splitted)
  # print comments
  for comment in comments:
    if comment.text.strip().encode('utf8') != '':
      comment_after_splitted = comment.text.strip()
      result_comments.append(comment_after_splitted)
  # print managements
  for management in managements:
    if management.text.strip().encode('utf8') != '':
      management_after_splitted = management.text.strip()
      result_managements.append(management_after_splitted[23:])

  # for i in range(0, len(result_name)):
    # result_name[i].append(result_symptoms[i])
    # result_name[i].append(result_causes[i])
    # result_name[i].append(result_comments[i])
    # result_name[i].append(result_managements[i])

  
  page_filtered = requests.get(links[info_id])
  soup_filtered = BeautifulSoup(page.text.encode('utf8'), 'html.parser')
  # for script in soup_filtered(["script", "style"]):
  #   script.extract()

  descriptions = soup_filtered.find_all('div', class_='info ')
  # print descriptions
  result_descriptions = []
  the_description = 'None'
  second_content = 'None'
  third_content = 'None'
  inc = 0
  print len(descriptions)
  for description in descriptions:
    if description.text.strip().encode('utf8') != '':
      if (inc == 0):
        the_description = description
        the_description.contents = the_description.contents[2:5]
        # description_after_splitted = the_description.text.strip()
        # result_descriptions.append(description_after_splitted)
        # print the_description.prettify(formatter="html")
      elif inc == 1:
        the_propagation = description
        for some_thing in the_propagation.find_all('a', {'class': 'prev'}):
          some_thing.decompose()
        for some_thing in the_propagation.find_all('a', {'class': 'next'}):
          some_thing.decompose()
        for some_thing in the_propagation.find_all('a', {'class': 'close'}):
          some_thing.decompose()
        # the_propagation.find_all('a', {'class': ''})
        subcontent = the_propagation
        the_content = subcontent.prettify(formatter="html")
        # the_fence = '<html><head><link rel="stylesheet" media="all" href="http://plantvillage.org/assets/application-1e61d2e1c058399262f0694302df5913f0295f25350b7fba3cb6d15aff363abf.css" /><script src="http://plantvillage.org/assets/application-9cbfdabf2cbd79ac64622e50d34de10a0bf7e2398146002fdb3230bc1d8e0be5.js"></script></head><body>'
        second_content = the_content
        # print second_content
        # for content in basic_req.contents:
        #   print content
        # basic_req_after_splitted = basic_req.text.strip()
        # print basic_req_after_splitted.split('\n\n')
      elif inc == 2:
        the_propagation = description
        for some_thing in the_propagation.find_all('a', {'class': 'prev'}):
          some_thing.decompose()
        for some_thing in the_propagation.find_all('a', {'class': 'next'}):
          some_thing.decompose()
        for some_thing in the_propagation.find_all('a', {'class': 'close'}):
          some_thing.decompose()
        # the_propagation.find_all('a', {'class': ''})
        subcontent = the_propagation
        the_content = subcontent.prettify(formatter="html")
        # the_fence = '<html><head><link rel="stylesheet" media="all" href="http://plantvillage.org/assets/application-1e61d2e1c058399262f0694302df5913f0295f25350b7fba3cb6d15aff363abf.css" /><script src="http://plantvillage.org/assets/application-9cbfdabf2cbd79ac64622e50d34de10a0bf7e2398146002fdb3230bc1d8e0be5.js"></script></head><body>'
        third_content = the_content
      # elif inc == 3:
      #   the_propagation = description
      #   for some_thing in the_propagation.find_all('a', {'class': 'prev'}):
      #     some_thing.decompose()
      #   for some_thing in the_propagation.find_all('a', {'class': 'next'}):
      #     some_thing.decompose()
      #   for some_thing in the_propagation.find_all('a', {'class': 'close'}):
      #     some_thing.decompose()
      #   # the_propagation.find_all('a', {'class': ''})
      #   subcontent = the_propagation
      #   the_content = subcontent.prettify(formatter="html")
      #   the_fence = '<html><head><link rel="stylesheet" media="all" href="http://plantvillage.org/assets/application-1e61d2e1c058399262f0694302df5913f0295f25350b7fba3cb6d15aff363abf.css" /><script src="http://plantvillage.org/assets/application-9cbfdabf2cbd79ac64622e50d34de10a0bf7e2398146002fdb3230bc1d8e0be5.js"></script></head><body>'
      #   fourth_content = the_fence + the_content + '</body></html>'
      #   print fourth_content
      else:
        pass
        # description_after_splitted = description.text.strip().encode('utf8')
        # print description_after_splitted
      # print '========================'
      inc += 1
  
  nama_tanaman = soup.find('h1')
  result_the_name = nama_tanaman.text.strip()
  print result_the_name
  return json.dumps({'name': result_the_name, 'result_name': result_name, 'result_cause': result_causes, 'result_management': result_managements, 'descriptions': str(the_description), 'second_content': str(second_content), 'third_content': str(third_content), 'result_symptoms': result_symptoms, 'result_comments': result_comments}), {'Content-Type': 'application/json'}
  

if __name__=='__main__':
  import os
  port = int(os.getenv('PORT', 5000))
  app.run(host='0.0.0.0', port=port, debug=False)

# # print result_symptoms
# # print result_causes
# # print result_comments
# # print result_managements

# # print len(result_name)
# # print len(symptoms)
# # print len(causes)
# # print len(comments)
# # print len(managements)