import subprocess
import pandas as pd
from pathlib import Path
from PIL import Image
from selenium import webdriver
import time

driver = webdriver.Chrome()
user = 'elonmusk'

posX = 282
posY = 63
width = 640

#panda dataframe = panda read csv of desired format
df = pd.read_csv("data/{}.csv".format(user))

#return a list of the urls in the csv

istweetreply = df["in_reply_to_screen_name"].values

#doesnt work
#statusonly = df.drop(df[df.in_reply_to_screen_name != ""].index)

#drop rows from the dataframe that don't have an empty istweetreply string
#https://www.quora.com/How-should-I-delete-rows-from-a-DataFrame-in-Python-Pandas
#this creates a new dataframe with only rows where the reply string is empty
#df2 = df.ix[df["in_reply_to_screen_name"].values == ""]

#df2[df.in_reply_to_screen_name == '']

df = df[df.in_reply_to_screen_name.isnull()]

#sort by favorites
sortdf = df.sort_values(['favorite_count'], ascending = False)

#only keep the top 50
smalldf = sortdf.head(50)

print(smalldf)

#now that extraneous data is gone, get the urls from remaining rows
urls = smalldf["url"].values
filepath = smalldf["img_file"].values

for index, singleurl in enumerate(urls):
    #print(singleurl)
    driver.get(singleurl)
    time.sleep(3)
    element = driver.find_element_by_class_name("permalink-tweet-container")
    singleshorturl = singleurl[33:]
    #need a way to filter actual statuses from the general replies that are stored in the list of urls
    if singleurl[:33] == "https://www.twitter.com/statuses/":
        driver.save_screenshot(singleshorturl + '.png')
        im = Image.open(singleshorturl + '.png')
        height= element.size['height']
        width = element.size['width']
        ##custom begin x/y coordinate, plus padding around the element
        im = im.crop((300*1.881, 75*1.881, 285*1.881+width*1.881+100, 50+70*1.881+height*1.881))
        im.save(str(index) + '-crop-' + singleshorturl +'.png')
    time.sleep(1)



driver.quit
