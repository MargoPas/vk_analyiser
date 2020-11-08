import requests
import re
from bs4 import BeautifulSoup as bs
import pandas as pd
from tqdm import tqdm

mainUrl = 'https://habr.com/ru/post/'

habrParse_df = pd.DataFrame(columns = ["postNum", "currPostUrl", "response_title", "response_post", "response_numComment","response_rating"])


def get_post(postNum):
    currPostUrl = mainUrl + str(postNum)
    try:
        response = requests.get(currPostUrl)
        response.raise_for_status()
        response_title, response_post, response_numComment, response_rating = executePost(response)
        dataList = [postNum, currPostUrl, response_title, response_post, response_numComment, response_rating]
        habrParse_df.loc[len(habrParse_df)] = dataList
    except requests.exceptions.HTTPError as err:
        pass

def executePost(page):
    soup = bs(page.text, 'html.parser')
# Получаем заголовок статьи
    title = soup.find('meta', property='og:title')
    title = str(title).split('="')[1].split('" ')[0]
# Получаем текст статьи
    post = soup.find('div', id="post-content-body").text
    post = re.sub('\n', ' ', post)
    # Получаем количество комментариев
    num_comment = soup.find('span', id='comments_count').text
    num_comment = int(re.sub('\n', '', num_comment).strip())
    # Ищем инфо-панель и передаем ее в переменную
    info_panel = soup.find('ul', attrs={'class' : 'post-stats post-stats_post js-user_'})
# Получаем рейтинг поста
    try:
        rating = int(info_panel.find('span', attrs={'class' : 'voting-wjt__counter js-score'}).text)
    except:
        rating = info_panel.find('span', attrs={'class' : 'voting-wjt__counter voting-wjt__counter_positive js-score'})
        if rating:
            rating = int(re.sub('/+', '', rating.text))
        else:
            rating = info_panel.find('span', attrs={'class' : 'voting-wjt__counter voting-wjt__counter_negative js-score'}).text
            rating = - int(re.sub('–', '', rating))
# Получаем количество положительных и отрицательных голосов за рейтинг статьи
        vote = info_panel.find_all('span')[0].attrs['title']
    # Получаем количество добавлений в закладки
        bookmk = int(info_panel.find_all('span')[1].text)
# Получаем количество просмотров поста
        views = info_panel.find_all('span')[3].text
    return title, post, num_comment, rating
postCount = 50
for pc in tqdm(range(postCount)):
    postNum = pc + 1
    get_post(postNum)

habrParse_df.to_csv(r'C:\Users\000\Desktop\питон\vk_analyieser\analys text\file3.csv', encoding = 'utf-8')
print(habrParse_df)