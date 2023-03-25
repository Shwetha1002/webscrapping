from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd
import requests
import csv

# NASA Exoplanet URL
START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

# Webdriver
browser = webdriver.Chrome("chromedriver_win32/chromedriver.exe")
browser.get(START_URL)

time.sleep(10)

dwarf_star_data = []

headers = ["star name", "radius", "mass", "distance"]

def scrape():
    for i in range(1,2):
        while True:
            time.sleep(2)

            soup = BeautifulSoup(browser.page_source, "html.parser")

            # Check page number    
            
            star_table = soup.find_all("table")
            table_rows = star_table[7].find_all('tr')
            table_data = table_rows[1].find_all('td')
            
            temp_list = []
            for index, td_tag in enumerate(table_data):
                if index == 0:
                    temp_list.append(td_tag.find_all("a")[0].contents[0])
                else:
                
                        temp_list.append("")
                if index == 5:
                   temp_list.append(td_tag.contents[0])
                else:
                 
                        temp_list.append("")
                if index == 7:
                   temp_list.append(td_tag.contents[0])
                else:
                 
                        temp_list.append("")
                if index == 8:
                   temp_list.append(td_tag.contents[0])
                else:
                 
                        temp_list.append("")
    
            
            dwarf_star_data.append(temp_list)

        

            print(f" {i} scraping completed")


# Calling Method
scrape()
    
with open("final.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(dwarf_star_data)