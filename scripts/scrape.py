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

# Write constituents
df.to_csv("data/constituents.csv", index=False)

# Derive sector counts
sector_counts = (
    df.groupby("GICS Sector", sort=False)
    .size()
    .reset_index(name="count")
    .rename(columns={"GICS Sector": "sector"})
    .sort_values("count", ascending=False)
)
sector_counts.to_csv("data/sector-counts.csv", index=False)
