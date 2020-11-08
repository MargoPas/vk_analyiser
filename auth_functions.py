import json
import vk
import time
import asyncio
from vk.exceptions import VkAPIError
import requests
id_list  = ['213037282', '88933032', '28698167', '112126728']

def vk_auth():
    vk_session = vk.Session(  access_token='cbbc066fd5c8e31fbd8c1470161840e0dcc8df26b1202ffe52ca7ada94fb461ca2b600e0112509d8fdee5')
    api = vk.API(vk_session)
    return api

def wall_posts(id): #
    posts = vk_auth().wall.get(v ='5.21', owner_id = id, count=20)['items']
    posts_txt = [post['text'] for post in posts] #text of my post
    return(posts)


def get_friends(id):
    try:
        friends = vk_auth().friends.get(v ='5.21', user_id = id)['items']
    except VkAPIError:
        time.sleep(5)
        friends = []
    return friends

def wall_groups(id):
    group= vk_auth().groups.get(v ='5.21', user_id = id, extended = 1, fields = ('status', 'activity'))['items']
    return group


def normal_id(id_list):
    for i in range(len(id_list)):
        id_list[i] = '-' + str(id_list[i])
    return id_list

def user_info(id_list):
    user = vk_auth().users.get(v= '5.89', user_ids = '213037282')
    try:
        for id in id_list:
            user = user + (vk_auth().users.get(v= '5.89', user_ids = id))
    except VkAPIError:
        time.sleep(5)
    return user

friends_2 = []
friends_3 = []


for id in id_list:
    print(id, ' 2')
    print(friends_2)
    friends_2 = friends_2 + get_friends(id)
id_list = friends_2
while True:
    try:
        for id in id_list:
            print(id, ' 3')
            friends_3 = friends_3 + get_friends(id)
    except (requests.exceptions.ReadTimeout, ReadTimeout, urllib3.exceptions.ReadTimeoutError):
            time.sleep(1)
            print('_______Timeout______')

with open("./friends.txt", "a", encoding="utf-8") as friends_data:
    friends_data.write(friends_3)

while True:
    try:
        for id in id_list:
            if (id != ''):
                group = wall_groups(id)
                for index in range(len(group)):
                    group[index]['user_id']= id
                with open("./groups_data.json", "a", encoding="utf-8") as groups_data:
                    json.dump(group, groups_data, ensure_ascii=False, separators= (', \n', ':'))
                    groups_data.write('\n')
    except (requests.exceptions.ReadTimeout, ReadTimeout, urllib3.exceptions.ReadTimeoutError):
                time.sleep(1)
                print('_______Timeout______')
