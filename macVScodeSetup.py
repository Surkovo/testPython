# This program says hi


import requests

r = requests.get("https://www.theverge.com/")

print(r.status_code)
