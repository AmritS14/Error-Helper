import subprocess as sb
import requests
import os
import time

# save error message into a file
from requests import Response

p = sb.Popen(["python", "test.py", "2>", "error.txt"], shell=True)
time.sleep(1)

with open("error.txt", "r") as file:
    lines: list[str] = file.readlines()
    if len(lines) > 0:

        last_line: str = lines[-1]
        print(last_line)

        # api-endpoint
        URL = "https://api.stackexchange.com/2.3/search?site=stackoverflow"

        # defining a params dict for the parameters to be sent to the API
        PARAMS = {'order': "desc",
                  "sort": "votes",
                  "intitle": last_line,
                  "tagged": "python"}

        # sending get request and saving the response as response object
        r: Response = requests.get(url=URL, params=PARAMS)

        # max number of links to display
        nLinks: int = 5

        # convert response to JSON
        data = r.json()

        i = 0
        for item in data['items']:
            if i < nLinks:
                print(item['link'])
                i += 1

    else:
        print("No errors found")

os.remove("error.txt")
