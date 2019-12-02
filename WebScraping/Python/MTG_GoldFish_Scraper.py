import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import sqlite3
from sqlite3 import Error
import json


def scrape():

    htmldoc = "https://www.mtggoldfish.com/prices/paper/standard"
    page = requests.get(htmldoc)
    if page.status_code == 200:
        print("succesfull request")
    else:
        print("request unsuccesfull")
        raise Exception("Unsuccsefull request")
    soup = BeautifulSoup(page.content,'html.parser')
    # print(type(soup.prettify()))
    html_list = soup.get_text().splitlines()
    # print(len(html_list))
    start_index = 0
    stop_index = 0
    for line in html_list:
        if line.lower().__contains__("Mythic".lower()):
            print("start found")
            break
        start_index += 1
    for line in html_list:
        if line.lower().__contains__("last updated".lower()):
            print("end found")
            break
        stop_index +=1
    text_list = html_list[start_index:stop_index]
    filter_list = []
    skip = ""
    for each in text_list:
        if each == skip:
            skip = skip
        else:
            filter_list.append(each)
    
    dictn = createDict(filter_list)

    return dictn
    

#createDict is passed our filter_list

def createDict(filter_list):

    fl = filter_list
    fl.insert(0,"Throne of Eldraine")
    print(fl)
    set_list = ["Throne of Eldraine", "Core Set 2020", "War of the Spark", "Ravnica Allegiance", "Guilds of Ravnica" ]
    rarity_list = ["Common", "Uncommon", "Sealed Product", "Rare", "Mythic"]

    outdict = { set:{rarity:[] for rarity in rarity_list} for set in set_list}
    cur_set = ""
    cur_rarity = ""
    for cnt,word in enumerate(fl):
        if(word in set_list):
            cur_set = word
            continue
        if(word in rarity_list):
            cur_rarity = word
            continue
        try:
            float(word) #Do nothing, it's a price
        except ValueError:
            outdict[cur_set][cur_rarity].append(fl[cnt] + " = " + fl[cnt + 1])
    return outdict


# a little overkill, but it would be important to know if we have
# --an error connecting to our db
# Method creates a connection to our database and returns cursor object




def db_connection():

	try:
		con = sqlite3.connect('group9.db')
		return con.cursor()
	except Error:
		print(Error)

def add_card(card_name,rarity,set_name)
	
con = db_connection()
			
	
