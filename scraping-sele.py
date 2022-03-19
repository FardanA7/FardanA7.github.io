from selenium import webdriver
import urllib.request
import json
from datetime import datetime

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.nowinquire.com/chart/top-100-smartphones")

time = datetime.now()

ListSmartphone = []

i = 1
while i<=100:
    for smartphone in driver.find_elements_by_tag_name("tbody"):
        for data in smartphone.find_elements_by_tag_name("tr"):
            for img in data.find_elements_by_class_name("prod-img"):
                urllib.request.urlretrieve(img.get_attribute("src"), str(i)+".png")
                i = i + 1
                search = 0
                found = False
                if(len(data.text.split()) > 5):
                    while(found == False):
                        search = search + 1
                        if(data.text.split()[search] == '-'):
                            found = True
                        elif(data.text.split()[search] == 'Phone'):
                            found = True
                        elif(data.text.split()[search] == 'K40'):
                            found = True
                
                        idx = 1
                        model = data.text.split()[idx] + ' '
                        idx = idx + 1
                        while(idx<search+3):
                            model = model + data.text.split()[idx] + ' '
                            idx = idx + 1
        
                    if(len(data.text.split()) > 5):
                        idx = search+3
                        processor = data.text.split()[idx] + ' ' + data.text.split()[idx+1]
                
                if(len(data.text.split()) > 5):
                    ListSmartphone.append(
                        {"Rank": data.text.split("\n")[0],
                         "Image": img.get_attribute("src"),
                         "Model": model,
                         "Processor": processor,
                         "Waktu_Scraping": time.strftime("%Y-%m-%d %H:%M:%S"),
                        }
                    )

hasil_scraping = open("hasilscraping-2.json", "w")
json.dump(ListSmartphone, hasil_scraping, indent = 6)
hasil_scraping.close()
driver.quit()
