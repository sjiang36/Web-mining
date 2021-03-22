# -*- coding: utf-8 -*-
"""
Created on Tue May 12 15:28:03 2020

@author: bfzh1
"""

import csv
import requests
from bs4 import BeautifulSoup

FILENAME = 'H-index.csv'
F = open(FILENAME, 'w')

HEADERS = 'h-index \n'
F.write(HEADERS)


filename = 'C:/Users/bfzh1/OneDrive/Desktop/660/Final/urls.csv'
with open(filename) as f:
   reader = csv.reader(f)
   lst = list(reader)
   
   for key in lst :
      url = "/".join(key)
      if url != "NULL":
          r=requests.get(url)
          soup=BeautifulSoup(r.content,'html.parser')
          m =  soup.findAll('td', {'class':'gsc_rsb_std'})
          if m != []:
              hindex = m[2].text
              F.write(hindex + '\n')
          else:
              F.write("not found" + '\n')
              #print("noooooooo")
                   
      else:
          F.write("not found" + '\n') 
          
          
F.close()
    

