

import json
from pprint import pprint
import os
os.system('clear')





#.................... Read In simple_json.json File ................
print '\n\n\n -------------- simple.json ------------------ \n'
Fjson = '1-simple.json'
with open(Fjson) as data_file:
  json_data = json.load(data_file)



first_name = json_data['first_name']
last_name  = json_data['last_name']
online     = json_data['online']
car_year   = json_data['car_year']


print ' Raw File Read In: ' 
pprint(json_data) 
print '\n First Name: %s'%first_name
print ' Last Name : %s'%last_name
print ' Online    : %s'%online
print ' Car Year  : %s'%car_year

print '\n ---------- End simple.json ----------------- \n'
#-----------------------------------------------------------------



#................... Read In nested_json.json File ...............
print '\n\n\n -------------- nested.json ------------------ \n'
Fjson = '2-nested.json'
with open(Fjson) as data_file:
  json_data = json.load(data_file)

brandon    = json_data['Brandon']
b_username = json_data['Brandon']['username']     # OR brandon['username']
b_year     = brandon['year']                      # OR json_data['brandon']['year']
melodie    = json_data['Melodie']
m_username = json_data['Melodie']['username']     # OR melodie['username']
m_year     = melodie['year']                      # OR json_data['melodie']['year']

print ' Raw File Read In : ' 
pprint(json_data) 
print '\n Brandon        : %s'%brandon
print ' Brandon Username : %s'%b_username
print ' Brandon Year     : %s'%b_year
print ' Melodie          : %s'%melodie
print ' Melodie Username : %s'%m_username
print ' Melodie Year     : %s'%m_year

print '\n ---------- End nested.json ----------------- \n'
#----------------------------------------------------------------


#................... Read In nested_array_json.json File ...............
print '\n\n\n -------------- nested_array.json ------------------ \n'
Fjson = '3-nested_array.json'
with open(Fjson) as data_file:
  json_data = json.load(data_file)

name     = json_data['name']
websites = json_data['websites']
nweb     = len(websites)
social   = json_data['social_media']
nsoc     = len(social)

print ' Raw File Read In : ' 
pprint(json_data) 
print '\n Name: %s'%name

print '\n Websites:'
for jw in range(nweb):
  url = websites[jw]['url']
  des = websites[jw]['description']
  print '   URL: %s'%url
  print '   Description: %s'%des

print '\n Social Media:'
for js in range(nsoc):
  url = social[js]['url']
  des = social[js]['description']
  print '   URL: %s'%url
  print '   Description: %s'%des

print '\n ---------- End nested_array.json ----------------- \n'
#----------------------------------------------------------------



#................... Read In nested_array2_json.json File ...............
print '\n\n\n -------------- nested_array2.json ------------------ \n'
Fjson = '4-nested_array2.json'
with open(Fjson) as data_file:
  json_data = json.load(data_file)

users  = ['Brandon','Melodie']
nusers = len(users)

print ' Raw File Read In : ' 
pprint(json_data) 

print '\n Loop  Over Users: \n'
for user in users:
  print ' User Name: %s'%user
  user_data = json_data[user]
  websites  = user_data['websites']
  nweb      = len(websites)
  social    = user_data['social_media']
  nsoc      = len(social)
  
  print '\n Websites for %s:'%user
  for jw in range(nweb):
    url = websites[jw]['url']
    des = websites[jw]['description']
    print '   URL: %s'%url
    print '   Description: %s'%des

  print '\n Social Media for %s: '%user
  for js in range(nsoc):
    url = social[js]['url']
    des = social[js]['description']
    print '   URL: %s'%url
    print '   Description: %s'%des
  
  print '\n'
print '\n ---------- End nested_array2.json ----------------- \n'
#----------------------------------------------------------------



print '\n\n\n'
