# This program says hi
import math
import os
import sys

import requests

print(sys.version)
print(sys.executable)

r = requests.get("https://www.theverge.com/")

print(r.status_code)
