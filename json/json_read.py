

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
year       = json_data['year']

print ' Raw File Read In: ' 
pprint(json_data) 
print '\n First Name: %s'%first_name
print ' Last Name : %s'%last_name
print ' Online    : %s'%online
print ' Year      : %s'%year

print '\n ---------- End simple.json ----------------- \n'
#-----------------------------------------------------------------



#................... Read In nested_json.json File ...............
print '\n\n\n -------------- nested.json ------------------ \n'
Fjson = '2-nested.json'
with open(Fjson) as data_file:
  json_data = json.load(data_file)

will       = json_data['Will']
w_username = json_data['Will']['username']        # OR will['username']
w_year     = will['year']                         # OR json_data['will']['year']
deanna     = json_data['Deanna']
d_username = json_data['Deanna']['username']      # OR deanna['username']
d_year     = deanna['year']                       # OR json_data['deanna']['year']

print ' Raw File Read In : ' 
pprint(json_data) 
print '\n Name          : %s'%will
print ' Will Username   : %s'%w_username
print ' Will Year       : %s'%w_year
print ' Deanna          : %s'%deanna
print ' Deanna Username : %s'%d_username
print ' Deanna Year     : %s'%d_year

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

users  = ['Will','Deanna']
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
