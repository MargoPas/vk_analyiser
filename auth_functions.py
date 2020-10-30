import json
import vk

id_list  = ['213037282', '88933032', '344210747', '139920164', '28698167', '112126728']
Mephi = ['МИФИ', "НИЯУ", 'Mephi', "MEPHI"]
it = ['computer science', 'computer', '/dev', 'IT', 'комп']
def auth_handler():
    """Обработчик двухфакторной аутентификации (если включена)
    """
    key = input('Enter authentication code: ')
    return key, True
def vk_auth():
    vk_session = vk.Session(  access_token='cbbc066fd5c8e31fbd8c1470161840e0dcc8df26b1202ffe52ca7ada94fb461ca2b600e0112509d8fdee5')
    api = vk.API(vk_session)
    return api

def wall_posts(id): #
    posts = vk_auth().wall.get(v ='5.21', owner_id = id, count=20)['items']
    posts_txt = [post['text'] for post in posts] #text of my post
    return(posts)


def wall_friends(id):
    friends = vk_auth().friends.get(v ='5.21', user_id = id)['items']
    return friends

def wall_groups(id):
    group= vk_auth().groups.get(v ='5.21', user_id = id, extended = 1, fields = 'status')['items']
    return group
for id in id_list:
    group = wall_groups(id)
    for index in range(len(group)):
        group[index]['user_id']= id
    with open("./groups_data.json", "a", encoding="utf-8") as groups_data:
        json.dump(group, groups_data, ensure_ascii=False, separators= (', \n', ':'))
        groups_data.write('\n')
