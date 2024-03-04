from flask import Flask

from HW_03.functions.generate_students import generate_students_route
from HW_03.functions.get_bitcoin_value import get_bitcoin_value_route

app = Flask(__name__)

app.register_blueprint(generate_students_route)
app.register_blueprint(get_bitcoin_value_route)


if __name__ == "__main__":
    app.run(port=5000, debug=True)
