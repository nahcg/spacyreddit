import praw
import pandas as pd
from bs4 import BeautifulSoup 
from selenium import webdriver
import time
import csv
import regex as re
import html
from selenium.webdriver.common.by import By


browser=webdriver.Chrome()
browser.get("https://www.reddit.com/r/SkincareAddiction/wiki/hg_threads_index/")

reddit = praw.Reddit(client_id="6gEhnarV7u-PMem0MM8Q_Q",
                               client_secret="ULEh9zduEBhUuMQhB_P4tX7_60OJkQ",
                               user_agent="webscrape")

link = []
links = browser.find_elements(By.XPATH, "//div[@class='md wiki']/table/tbody/tr/td/a")
for i in links:
     link.append(i.get_attribute('href'))

comments = []

for x in link:
    submission = reddit.submission(url=x)
    submission.comments.replace_more(limit=None)
    for top_level_comment in submission.comments:
        comments.append(top_level_comment.body)

comments2 = []

for x in link:
    submission = reddit.submission(url=x)
    submission.comments.replace_more(limit=None)
    for top_level_comment in submission.comments:
        for second_level_comment in top_level_comment.replies:
            comments2.append(second_level_comment.body)

comments2.extend(comments)
        
final = []

for y in comments2:
    s = y.replace("\r", "").replace("\n", "").replace("**", "").replace(">", "").replace("<", "").replace("[", "").replace("]", "").replace("*", "").replace("\\", "").replace("-", " ").replace("!", " ")
    s = re.sub("\(https:\/\/.*?\)|\(http:\/\/.*?\)|https:\/\/.*?\)", "", s)
    x = re.search("(?<=Product [Nn]ame:).*?(?=Price)", s)
    if x != None:
        x = x.group(0)
        x = x.strip()
        final.append(x)

final2 = []

for i in final:
     i = re.sub("[Tt]ype and amount.*", "", i)
     i = re.sub("[Tt]ype and %.*", "", i)
     i = re.sub("[Pp]roduct type.*", "", i)
     i = re.sub("\(.*\)", "", i)
     final2.append(i)
        
df = pd.DataFrame(final2)
df.to_csv("reddittesting.csv", sep=',',index=False, encoding='utf-8-sig')
