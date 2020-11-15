import requests

def nearest_stationsGet(payload_nearest_stations):
    # Список ближайших станций
    print('------------------------------')
    print('def nearest_stationsGet():')

    base_URL = 'https://api.rasp.yandex.net/v3.0/nearest_stations/?'
    r = requests.get(base_URL, params=payload_nearest_stations)

    print(f"url: {r.url}")
    #print(f"text: \n {r.text}")

    r_dict=r.json()
    number_station = int(r_dict['pagination']['total'])
    print(f"В радиусе {payload_nearest_stations['distance']}км от Б15 кол-во станций:{number_station}")

    for i in range(number_station):

        transport_type = r_dict['stations'][i]['transport_type']
        if transport_type == 'plane':
            transport_type = 'Самолет'
        elif transport_type == 'train':
            transport_type = 'Поезд'
        elif transport_type == 'bus':
            transport_type = 'Автобус'
        else:
            continue

        station_type_name = r_dict['stations'][i]['station_type_name']
        title = r_dict['stations'][i]['title']
        distance = round(r_dict['stations'][i]['distance'],4)

        print(f'{i+1}. Тип транспорта: {transport_type},\t'
              f'название: {station_type_name},\t'
              f'название станции: "{title}",\t'
              f'находится на расстоянии {distance}км от Б15')

def nearest_nearest_settlementGet(payload_nearest_settlement):
    # Ближайший город к указанной точке
    print('------------------------------')
    print('def nearest_nearest_settlementGet(payload_nearest_settlement):')

    base_URL = 'https://api.rasp.yandex.net/v3.0/nearest_settlement/?'
    r = requests.get(base_URL, params=payload_nearest_stations)

    print(f"url: {r.url}")
    # print(f"text: \n {r.text}")

    r_dict = r.json()
    name_settlement = r_dict['title']
    distance = r_dict['distance']

    print(f"В радиусе {payload_nearest_settlement['distance']}км (от Б15) Ближайший город:{name_settlement}, на расстоянии: {round(distance,4)}км")

    '''for i in range(number_station):

        station_type_name = r_dict['stations'][i]['station_type_name']
        title = r_dict['stations'][i]['title']
        distance = round(r_dict['stations'][i]['distance'],4)

        print(f'{i+1}. Тип транспорта: {transport_type},\t'
              f'название: {station_type_name},\t'
              f'название станции: "{title}",\t'
              f'находится на расстоянии {distance}км от Б15')
    '''

def searchGet(payload_search):
    # Расписание рейсов между станциями
    print('------------------------------')
    print('def searchGet(payload_search):')

    base_URL = 'https://api.rasp.yandex.net/v3.0/search/?'

    r = requests.get(base_URL, params=payload_search)
    print(f"url: {r.url}")
    # print(f"text: \n {r.text}")

    r_dict = r.json()

    number_flights = int(r_dict['pagination']['total'])
    print("Кол-во рейсов ", payload_search['date'],
          ' в направлении ', r_dict['segments'][0]['thread']['title'],
          ': ', number_flights, 'без пересадок')

    for i in range(number_flights):

        date_departure = r_dict['segments'][i]['departure'][:10]
        time_departure = r_dict['segments'][i]['departure'][11:19]

        date_arrival = r_dict['segments'][i]['arrival'][:10]
        time_arrival = r_dict['segments'][i]['arrival'][11:19]

        transport_type = r_dict['segments'][i]['thread']['transport_type']
        if transport_type == 'plane':
            transport_type = 'Самолет'
        elif transport_type == 'train':
            transport_type = 'Поезд'
        elif transport_type == 'bus':
            transport_type = 'Автобус'
        else:
            continue

        print(f'{i+1}. {transport_type}\t ОТПРАВЛЕНИЕ: дата: {date_departure}, время: {time_departure}; '
              f'ПРИБЫТИЕ: дата {date_arrival}, время: {time_arrival}')

    uid = r_dict['segments'][0]['thread']['uid']
    return(uid)

if __name__ == '__main__':

    payload_search = {'apikey': '6e715e39-9e14-4981-9e3c-a4a3d5b5251c',
               'from': 'c146',
               'to': 'c213',
               'lang': 'ru_RU',
               'date': '2020-11-15',
               'transfers': 'false'}

    searchGet(payload_search)

    payload_nearest_stations = {'apikey': '6e715e39-9e14-4981-9e3c-a4a3d5b5251c',
                      'lat': '55.388645',
                      'lng': '86.098903',
                      'distance': '50',
                      'limit': '200',
                      }

    nearest_stationsGet(payload_nearest_stations)

    payload_nearest_settlement = {'apikey': '6e715e39-9e14-4981-9e3c-a4a3d5b5251c',
                                'lat': '55.388645',
                                'lng': '86.098903',
                                'distance': '50',
                                }

    nearest_nearest_settlementGet(payload_nearest_settlement)