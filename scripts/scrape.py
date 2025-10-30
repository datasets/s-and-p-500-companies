import pandas as pd
import requests
import random

link = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies#S&P_500_component_stocks"

# new: Wikipedia requires User-Agent identifier in header.
n = random.randint(1, 100)
identifier = f"mySeriouslyGoodProject/1.0 (https://github.com/friendlyUser{n}/coolRepo, coder{n}@gmail.com)"

headers = {
    'User-Agent': identifier}

response = requests.get(link, headers=headers)
content = response.content


df = pd.read_html(content)[0]

# Write to CSV
df.to_csv("data/constituents.csv", index=False)
