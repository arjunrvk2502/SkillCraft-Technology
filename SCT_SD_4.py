import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import numpy as np

url = "https://www.amazon.in/s?k=lg+washing+machine+front+load&crid=W9PLA53FG9CD&sprefix=lg%2Caps%2C264&ref=nb_sb_ss_mvt-t11-ranker_2_2"
header = ({"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0' , "Accept-Language" : "en-us , en;q=0.5"})

webpage = requests.get(url , headers=header)
soup = bs(webpage.text , "html.parser")

links = soup.find_all("a" , attrs={"class":"a-link-normal s-line-clamp-2 s-line-clamp-3-for-col-12 s-link-style a-text-normal"})

link_list = []

for link in links:
    link_list.append(link.get("href"))

d = {"name":[] , "price":[] , "ratings":[]}

for link in link_list:
    new_webpage = requests.get("https://www.amazom.in"+ link , headers=header)
    new_soup = bs(new_webpage.text , "html.parser")
    try:
        title = new_soup.find("h1", attrs={"id": "title"}).find("span", attrs={"id": "productTitle"}).text.strip()
        d["name"].append(title)
    except:
        d["name"].append("N/A")
    try:
        price = new_soup.find("span" , attrs={"class" : "a-price-whole"}).text.strip()
        d["price"].append(price)
    except:
        d["price"].append("N/A")
    try:
        rating = ratings = new_soup.find("span" , attrs={"class" : "a-size-medium a-color-base"}).text.strip()
        d["ratings"].append(rating)
    except:
        d["ratings"].append("N/A")



df = pd.DataFrame.from_dict(d)
df["name"] = df["name"].replace("", np.nan)
df = df.dropna(subset=["name"])
df.to_csv("C:/Users/Administrator/Desktop/SCT_SD_4.csv", header=True , index=False)
print("Data saved to SCT_SD_4.csv")
