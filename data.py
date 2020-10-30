import pandas as pd
import json

Mephi = ['МИФИ', "НИЯУ", 'Mephi', "MEPHI"]
it = ['computer science', 'computer', '/dev', 'IT', 'комп']


with open("./groups_data.json", "r", encoding="utf-8") as groups_data:
     group = json.load(groups_data)

j =0
groups= pd.DataFrame(columns = ['user_id', 'group_id', 'name', 'status', 'target'])
for i in range(len(group)):
    groups.loc[i + j] = [group[i]["user_id"], group[i]["id"], group[i]["name"], '', '']
    j = groups.shape[0]


print(groups)