import requests
from bs4 import BeautifulSoup

page = requests.get("https://republika.co.id/")

obj = BeautifulSoup(page.text, 'html.parser')

print('\nMenampilkan kategori')
print('======================')
for publish in obj.find_all('div',class_='teaser_conten1_center'):
        print(publish.find('a').text)

print ('\nMenampilkan semua teks headline')
print ('==================================')
for headline in obj.find_all('div', class_='conten1'):
    print (headline.find('h2').text)

print('\nMenampilkan waktu publish')
print('===========================')
for publish in obj.find_all('div',class_='date'):
        print(publish.text)

print('\nMenampilkan waktu scrapping')
print('=============================')        
from datetime import datetime
waktu_sekarang = datetime.now()
waktu_scraping = waktu_sekarang.strftime("%Y-%m-%d %H:%M:%S")
print("Waktu Scraping = ", waktu_scraping)

# Import Package Json
import json

data=[]

f=open('E:\Polban\hasil_scraping.json','w')
for publish in obj.find_all('div',class_='conten1'):
    data.append({"judul":publish.find('h2').text, "kategori":publish.find('a').text, "waktu_publish":publish.find('div',class_='date').text,"waktu_scraping":waktu_sekarang.strftime("%Y-%m-%d %H:%M:%S")})
jdumps = json.dumps(data, indent=2)
f.writelines(jdumps)
f.close()
