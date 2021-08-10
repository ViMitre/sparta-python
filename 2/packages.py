import requests
import os

pwd = os.getcwd()
print(pwd)

bbc_r = requests.get("https://bbc.co.uk/news")
print(bbc_r.headers)