import pandas as pd
import json

Mephi = ['МИФИ', "НИЯУ", 'Mephi', "MEPHI"]
it = ['computer science', 'computer', '/dev', 'IT', 'комп']


with open("./groups_data.json", "r", encoding="utf-8") as groups_data:
     group = json.load(groups_data)


df= pd.DataFrame(columns = ['user_id', 'group_id', 'name', 'status', 'activity'])

df = pd.DataFrame.from_dict(group, orient='columns')
df.drop(["screen_name", "is_advertiser"], axis='columns', inplace=True)
df.drop(["photo_50", "photo_200"], axis='columns', inplace=True)
print(df)
df.to_csv(r'C:\Users\000\Desktop\питон\vk_analyieser\file3.csv', encoding = 'utf-8')