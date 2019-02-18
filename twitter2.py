import urllib.request, urllib.parse, urllib.error
import json
import twurl
from geopy import Nominatim
from os.path import exists
from copy import deepcopy
TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'
history = []
history = []


def save_twit_json(acct):
    '''
    :param acct: your twitter @account without symbol @
    :return: None, but will save your followers twitts in twitts.json file in current directiory
    '''
    url = twurl.augment(TWITTER_URL, {'screen_name': acct})
    page = urllib.request.urlopen(url)
    with open("data/twitts.json", "wb") as tj:
        tj.write(page.read())
    return None
def get_twit_json_values():
    """
    :param key: enter custom quantity of keys from twitts.json file
    :return: new list of dicts contains introduced above keys and their values
    """
    with open("data/twitts.json", "r") as tj:
        data = json.loads(tj.read())
        while isinstance(data, dict) or isinstance(data, list):
            printer(data)
            next_value = input()
            if next_value == '..':
                if history:
                    data = history.pop()
            elif isinstance(data, dict):
                history.append(deepcopy(data))
                data = data[next_value]
            elif isinstance(data, list):
                history.append(deepcopy(data))
                data = data[int(next_value)]
        printer(data)

def printer(data):
    msg = str(data)
    if isinstance(data, dict):
        data = data.keys()
        msg = '|'.join(data)
        msg = '{' + msg + '}'
    elif isinstance(data, list):
        data = ['element_{}'.format(i) for i in range(len(data))]
        msg = '|'.join(data)
        msg = '[' + msg + ']'
    print(msg)

if __name__ == '__main__':
    acount = input("Enter please your account:")
    save_twit_json(acount)
    get_twit_json_values()
