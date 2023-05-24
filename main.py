import subprocess as sb
import requests
import os

# s1 = sb.Popen(["echo", "\"\"\""], shell=True)
p = sb.Popen(["python", "test.py", "2>", "error.txt"], shell=True)

with open("error.txt", "r") as file:
    last_line = file.readlines()[-1]

# print(last_line)

# api-endpoint
URL = "https://api.stackexchange.com/2.3/search?site=stackoverflow"

# location given here
# location = "delhi technological university"

# defining a params dict for the parameters to be sent to the API
PARAMS = {'order': "desc",
          "sort": "votes",
          "intitle": last_line,
          "tagged": "python"}

# sending get request and saving the response as response object
r = requests.get(url=URL, params=PARAMS)

nLinks = 5

# print(r.json())

data = r.json()
i = 0
for item in data['items']:
    if i < nLinks:
        print(item['link'])
        i += 1

os.remove("error.txt")
"""
file = open("error.txt", "r")
li = file.readlines()
#print(li[len(li) - 1])

import re
thelist = li # ['','"0=SYSEV,1=APPEV,2:3=VECEV"','"ASEN"+$y','"FALSE"','0x0000FFFF']

newlist = []

for item in thelist:
    newlist.append(re.sub('["]','',item))

print(newlist)
print(newlist[len(li) - 1])



_, err = p.communicate()

msg = err.decode()

if len(msg) == 0:
    print("No errors found")

else:
    print(f"{err}\n{msg}")

# print(f"{len(err)}\n{len(msg)}")
# output = p.stdout.read()

# print(test)
"""
