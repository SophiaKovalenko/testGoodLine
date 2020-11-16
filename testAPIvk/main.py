'''
Для запуска программы требуется установить Python 3.5 или выше
Установить requests: pip install requests
*Используется ключ: {fee97c90465e69115951741d2ff9657a959d1f8443fd64469d5f38168d45ab0261bf083458d3e3fc643ee},
    без срока годности
'''

import requests

def likes_getList(payload):
    #Получает список идентификаторов пользователей, которые добавили заданный объект в свой список Мне нравится

    print('------------------------------')
    print('likes_getList(payload): ')

    base_URL = 'https://api.vk.com/method/likes.getList?v=5.52'
    r = requests.get(base_URL, params=payload)

    print(f"url: {r.url}\n text: {r.text}")
    r_dict = r.json()

    q_likes = r_dict['response']['count']
    print(f"Всего подписчиков: {q_likes}")

    for item in range(int(q_likes)):
        print(f"№{item+1} ID: {r_dict['response']['items'][item]['id']}"
              f" имя: {r_dict['response']['items'][item]['first_name']}"
              f" фамилия: {r_dict['response']['items'][item]['last_name']}")


def users_getFollowers(payload):
    #Возвращает список идентификаторов пользователей, которые являются подписчиками пользователя
    print('------------------------------')
    print('users_getFollowers(payload): ')

    base_URL = 'https://api.vk.com/method/users.getFollowers?v=5.52'
    r = requests.get(base_URL, params=payload)

    print(f"url: {r.url}\n text: {r.text}")
    r_dict = r.json()

    q_followers = r_dict['response']['count']
    print(f"Всего подписчиков: {q_followers}")

    print(f"Первые {int(payload['count'])} подписчиков")
    for item in range(int(payload['count'])):
        print(f"№{item} ID: {r_dict['response']['items'][item]['id']}"
              f" имя: {r_dict['response']['items'][item]['first_name']}"
              f" фамилия: {r_dict['response']['items'][item]['last_name']}")

def board_getComments (payload):
    # Возвращает список сообщений в указанной теме.
    print('------------------------------')
    print('board_getComments (payload): ')

    base_URL = 'https://api.vk.com/method/board.getComments?v=5.52'
    r = requests.get(base_URL, params=payload)

    print(f"url: {r.url}\n text: {r.text}")
    r_dict = r.json()

    q_comments = r_dict['response']['count']
    print(f"Всего комментариев в обсуждении: {q_comments}")

    for item in range(int(payload['count'])):
        print(f"\nКомментарий №{item+1} from_id: {r_dict['response']['items'][item]['from_id']}"
              f" текст:\n {r_dict['response']['items'][item]['text']}")


if __name__ == '__main__':

    ACCESS_TOKEN = 'fee97c90465e69115951741d2ff9657a959d1f8443fd64469d5f38168d45ab0261bf083458d3e3fc643ee'

    payload_topic = {
        'access_token': ACCESS_TOKEN,
        'group_id': '274672',
        'topic_id': '29710884',
        'count': '20',
        'extended': '1',
        'sort': 'asc '
    }

    board_getComments(payload_topic)

    payload_followers = {
        'access_token': ACCESS_TOKEN,
        'user_id': '22180705',
        'fields': 'id,first_name,last_name,city,last_seen',
        'count': '100'
    }

    users_getFollowers(payload_followers)

    payload_likes = {
        'access_token': ACCESS_TOKEN,
        'type': 'photo',
        'fields': 'id,first_name,last_name,city,last_seen',
        'owner_id': '-274672',
        'extended': '1',
        'count': '100',
        'item_id': '457252924'
    }

    likes_getList(payload_likes)