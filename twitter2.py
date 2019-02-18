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
    >>> get_twit_json_values()
    Enter please your account:atkaterunner
    {users|next_cursor|next_cursor_str|previous_cursor|previous_cursor_str|total_count}
    users
    [element_0|element_1|element_2|element_3|element_4|element_5|element_6|element_7|element_8|element_9|element_10|element_11|element_12|element_13|element_14|element_15|element_16|element_17|element_18|element_19]
    0
    {id|id_str|name|screen_name|location|description|url|entities|protected|followers_count|friends_count|listed_count|created_at|favourites_count|utc_offset|time_zone|geo_enabled|verified|statuses_count|lang|status|contributors_enabled|is_translator|is_translation_enabled|profile_background_color|profile_background_image_url|profile_background_image_url_https|profile_background_tile|profile_image_url|profile_image_url_https|profile_banner_url|profile_link_color|profile_sidebar_border_color|profile_sidebar_fill_color|profile_text_color|profile_use_background_image|has_extended_profile|default_profile|default_profile_image|following|live_following|follow_request_sent|notifications|muting|blocking|blocked_by|translator_type}
    entities
    {url|description}
    url
    {urls}
    urls
    [element_0]
    0
    {url|expanded_url|display_url|indices}
    url
    https://t.co/fBSzOW6fRe
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
