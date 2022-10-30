from bs4 import BeautifulSoup as bs
from selenium import webdriver
import time,pathlib,os
import pdb,re
from collections import Counter
import requests

browser=requests.session()
a=browser.get('https://www.azlyrics.com/j/jackson.html').content
clean_page=bs(a,'lxml')
all_div=clean_page.find_all('div',{"class":"listalbum-item"})
all_links=["https://www.azlyrics.com"+a.find('a')['href'] for a in all_div]
for one in all_links:
    current_page=browser.get(one).content
    unrefined=bs(current_page,'lxml')
    title=unrefined.find('div',{"class":"col-xs-12 col-lg-8 text-center"}).findChildren('b')[1].text.replace('"',"").replace("'","")
    song= unrefined.find('div',{"class":"col-xs-12 col-lg-8 text-center"}).findChildren('div')[5].get_text()
    path1=pathlib.Path(r'c:\users\PC-1\desktop\jackson') / f"""{title}.txt"""
    path1.write_text(song)



#this code removes unwanted data from lyrics
# newdata=bs(data,'lxml')
# a=newdata.text
# b=re.sub(r'(\[.*\])',"",a).strip()
# c=re.sub(r"[']|[']|[,]|[)]|[(]","",b).replace("-"," ")
# print(c)
# import unicodedata
# xyz = unicodedata.normalize("NFKD",varaible_name)

