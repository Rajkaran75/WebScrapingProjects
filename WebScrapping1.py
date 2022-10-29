from bs4 import BeautifulSoup as bs
from selenium import webdriver
import time,pathlib,os
import pdb
from collections import Counter
browser=webdriver.Chrome(r'c:\chromedriver.exe')
browser.get("https://satindersartaaj.com")
tag=browser.find_element(by='xpath',value="""//*[@id="xenav"]/ul/li[5]/a""").click()
time.sleep(4)
list_of_albumLinks=browser.find_elements(by='xpath',value="""//a[contains(text(),"SONGS")]""")
time.sleep(4)
urls_of_each_album=[a.get_attribute('href') for a in list_of_albumLinks]
album=0
for url_for_each in urls_of_each_album:
    count=1
    browser.get(url_for_each)
    time.sleep(3)
    try:
        div_section_each_song=browser.find_elements(by='xpath',value='//div[@class="col-md-12 songlyrics"]')
        album+=1
    except:
        continue
    dir_path=f'C:\\Users\\PC-1\\Desktop\\sartaj\\folder{album}'
    os.mkdir(f'C:\\Users\\PC-1\\Desktop\\sartaj\\folder{album}')
    count=1
    for each in div_section_each_song:
        path=pathlib.Path(dir_path)
        raw_data=each.get_attribute('innerHTML').replace("<br>","\n")
        path=(path / f"song{count}.txt").write_text(raw_data)
        count+=1

for each_file in (pathlib.Path(r'C:\users\PC-1\Desktop\sartaj').rglob("*.txt")):
    with open(each_file,'r') as r1:
        try:
            refined_lyrics=r1.read().replace("’","").replace(","," ").replace(".","")
        except:
            pdb.set_trace()
    with open(each_file,'w') as w1:
        each_file.write_text(refined_lyrics)


most_most=Counter()
for song in pathlib.Path(r'c:\users\PC-1\Desktop\sartaj').rglob("*.txt"):
    temp_list=song.read_text().lower().split()
    most_most.update(temp_list)
print(most_most.most_common(30))