

import requests
import pandas as pd


#___GET_DATA___(URL,PARAMS)

url = "https://disease.sh/v3/covid-19/countries"
PARAMS = {}
response = requests.get(url, params = PARAMS, timeout = 10)
print("Status:", response.status_code)

# ___MAKE_TABLE(DATA,RECORDS_KEY)

data = response.json()
print("Type:", type(data))
if isinstance(data, dict):
    print("Keys:", list(data.keys()))      
else:
    print("It is already a list of", len(data), "records")



RECORDS_KEY = None      

records = data[RECORDS_KEY] if RECORDS_KEY else data
table = pd.json_normalize(records, sep="_")
print(table.shape, "(rows, columns)")
print(list(table.columns))
table.head()

#__TIDY_DATA(DF)

RENAME = {}
KEEP = ["country", "continent", "cases", "deaths", "population"]     # <- your columns
MUST_HAVE = ["cases", "continent"]                                   # <- your must-have columns

tidy = table.rename(columns=RENAME)
tidy = tidy[KEEP]
tidy = tidy.dropna(subset=MUST_HAVE)
print(tidy.shape)
tidy.head()