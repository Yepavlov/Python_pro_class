from flask import Flask

from HW_05.hw_with_flask.blueprints.views import city_by_genre_blueprint

app = Flask(__name__)

app.register_blueprint(city_by_genre_blueprint)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
