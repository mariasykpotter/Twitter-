import urllib.request, urllib.parse, urllib.error
import twurl
import json
from geopy import Nominatim
from os.path import exists

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'


def save_twit_json(acct='Mariann01001908'):
    '''
    :param acct: your twitter @account without symbol @
    :return: None, but will save your followers twitts in twitts.json file in current directiory
    '''
    url = twurl.augment(TWITTER_URL, {'screen_name': acct})
    page = urllib.request.urlopen(url)
    with open("data/twitts.json", "wb") as tj:
        tj.write(page.read())
    return None


def get_twit_json_values(*key):
    '''
    :param key: enter custom quantity of keys from twitts.json file
    :return: new list of dicts contains introduced above keys and their values
    '''
    with open("data/twitts.json", "r") as tj:
        data = json.loads(tj.read())
        data = data['users']
        new_list = list()
        for i in data:
            new_dict = dict()
            new_list.append(new_dict)
            for n in key:
                new_dict[n] = i[n]
        if 'location' in key:
            nom = Nominatim()
            for i in new_list:
                n = nom.geocode(i['location'])
                i['latitude'] = n.latitude
                i['longitude'] = n.longitude
            return new_list
        else:
            return new_list


if __name__ == '__main__':

    if exists("data/twitts.json"):
        with open("data/twitts.json", "r") as tj:
            data = json.loads(tj.read())
            data = data['users']
            list_keys = list(data[0].keys())
            print(list_keys, '\n')
    else:
        save_twit_json()

    while True:
        x = input('Please chose and enter keys from the list above: ')
        x = x.replace(',', ' ').split()
        try:
            for i in get_twit_json_values(*x):
                print(i)
        except:
            print(
                'Maybe you enter something wrong, please check yuorself and try again.')
            continue
