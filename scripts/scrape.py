from io import StringIO

import pandas as pd
import requests

link = (
    "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies#S&P_500_component_stocks"
)

response = requests.get(
    link,
    headers={"User-Agent": "Mozilla/5.0 (compatible; dataset-updater/1.0)"},
    timeout=30,
)
response.raise_for_status()

df = pd.read_html(StringIO(response.text), header=0)[0]

# Write to CSV
df.to_csv("data/constituents.csv", index=False)
