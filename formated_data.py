import re
import json
regex = re.compile(r'[\]][\n][\[]]', re.IGNORECASE)
with open("./groups_data.json", "r", encoding="utf-8") as groups_data:
      filedata = groups_data.read()


filedata = filedata.replace(']\n[', ',')

with open("./groups_data.json", "w", encoding="utf-8") as groups_data:
    groups_data.write(filedata)