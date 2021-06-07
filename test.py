import re

import requests

r = requests.get("https://www.amfiindia.com/spages/NAVAll.txt")
data = r.text.split('\n')
amcSet = set()
for amc in data:
    if re.search("Mutual Fund", amc):

        amcSet.add(amc)

for amc in amcSet:
    print("""\"""" + amc)
pass
