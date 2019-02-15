from flask import Flask
from folium import Map, Marker
from twitter2 import *
from flask import render_template

app = Flask(__name__)


def render_map():
    try:
        save_twit_json()
        print('1/3 - SUCCESSFUL load twitts.json')
    except:
        print('load twitts.json ERROR !!!')

    m = Map(location=[20.0, -1.0], tiles="Mapbox Bright", zoom_start=2.5)

    try:
        place = get_twit_json_values('name', 'location')
        print('2/3 - SUCCESSFUL geolocation computing')
        for i in place:
            Marker([i['latitude'], i['longitude']], tooltip=i['name']).add_to(m)
        m.save('templates/map.html')
        print('3/3 - map saved SUCCESSFUL')
    except:
        print('ERROR map saving !!!')


@app.route('/')
def index():
    render_map()
    return render_template('map.html')


if __name__ == '__main__':
    app.run()