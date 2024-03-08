from flask import Flask

from HW_04.views.count_tracks_time import count_tracks_time_for_each_album_route, count_tracks_time_for_all_albums_route
from HW_04.views.orders_price import order_price_route
from HW_04.views.tracks_info import tracks_info_route

app = Flask(__name__)

app.register_blueprint(order_price_route)
app.register_blueprint(tracks_info_route)
app.register_blueprint(count_tracks_time_for_each_album_route)
app.register_blueprint(count_tracks_time_for_all_albums_route)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
