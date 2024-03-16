import requests as r
from bs4 import BeautifulSoup as B
import sys


url = input("url: ")

res = r.get(url)

soup = B(res.text, 'html.parser')

bio = soup.find('p')
dp = soup.find('img', class_='img-fluid')
im = soup.find_all('img', class_='bg-img')

ofin = soup.find_all('a', class_='color-blue-dark')
try:
  onlyfans = ofin[0]['href']
except:
  onlyfans = None
try:
  instagram = ofin[1]['href']
except:
  instagram = None
user = soup.find_all('h3')[1]

username = user.text.lower()

if " " in username:
  username = username.replace(' ', '_')



create_user = r.post(
url = "https://fapegram.com/api/v1/create/",
data = {"u" : username})

print(create_user.json())

dow = r.get(dp['src'])

f = open(f"{username}.jpg", "wb")
f.write(dow.content)


create_profile = r.post(
url = "https://fapegram.com/model/api/v1/prof/",
data = {
   'u': username,
   'b':  user.text + ' ' + '/' + ' ' +  bio.text,
   'o': onlyfans,
   'i': instagram
},

files = {
'd':open(f"{username}.jpg", "rb")
}
)


print(create_profile.json())

for n, i in enumerate(im):
  xx = r.get(i['src'])
  sv = open(f"{username}-{n}.jpg", "wb")
  sv.write(xx.content)
  sv.close()
  xxx = r.post(
     url = "https://fapegram.com/model/api/v1/art/",
     data = {'u':username},
     files = {'im': open(f"{username}-{n}.jpg", "rb")}

)
  print(xxx.json())




