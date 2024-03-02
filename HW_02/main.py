from flask import Flask
import pandas as pd
import random
import string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Test Website</title>
    <style>
        body {
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100vh;
            margin: 0;
        }
        .content {
            text-align: center;
            font-size: 1.5em;
        }
    </style>
</head>
<body>
    <div class="content">
        %s
    </div>
</body>
</html>
"""


@app.route("/count-average-value")
def count_average_value_students():
    file_path = "hw.csv"

    df = pd.read_csv(file_path)
    columns = [" Height(Inches)", " Weight(Pounds)"]
    average_value = df[columns].mean().round(2)
    content = f"<p> The average values for all students are: average height = {average_value[' Height(Inches)']}" \
              f" inches and average weight = {average_value[' Weight(Pounds)']} pounds! <p/>"
    return HTML_TEMPLATE % content


@app.route("/get-random-password")
def get_random_password():
    length = random.randint(10, 20)
    all_characters_list = [string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation]
    all_characters_str = string.ascii_letters + string.digits + string.punctuation
    random_four_chars_of_each_type = [random.choice(type_of_chars) for type_of_chars in all_characters_list]
    random_chars = random.choices(all_characters_str, k=(length - 4))
    password = "".join(random_chars + random_four_chars_of_each_type)
    content = f"<p> Your random password is  {password} <p/>"
    return HTML_TEMPLATE % content


if __name__ == '__main__':
    app.run(
        port=5000,
        debug=True
    )
