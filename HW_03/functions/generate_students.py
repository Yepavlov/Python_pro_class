import csv
from typing import List
from flask import render_template, Blueprint
from faker import Faker
from webargs import fields, validate
from webargs.flaskparser import use_kwargs

generate_students_route = Blueprint("generate_students", __name__)

CSV_FILE_PATH = "generated_students.csv"
fake = Faker()
FIELDNAMES = ["first_name", "last_name", "email", "password", "date_of_birth"]


@generate_students_route.route("/generate-students")
@use_kwargs(
    {
        "number_of_students": fields.Int(
            missing=1, validate=validate.Range(max=1000, max_inclusive=True)
        )
    },
    location="query",
)
def generate_students(number_of_students: int) -> str:
    """
    Generate student data, write it to a CSV file, and render a template with the generated data.

    Parameters:
    - number_of_students (int): The number of students to generate.

    Returns:
    - str: HTML content rendered from the template ("students.html") with the generated student data.
    """
    students = generate_students_data(number_of_students)
    write_students_to_csv(students)
    return render_template("students.html", students=students)


def generate_students_data(number_of_students: int) -> List[dict]:
    """
    Generate student data based on the specified number of students.

    Parameters:
    - number_of_students (int): The number of students to generate.

    Returns:
    - list: A list of dictionaries containing generated student data.
    """
    students = []
    for _ in range(number_of_students):
        student = {
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "email": fake.email(),
            "password": fake.password(),
            "date_of_birth": fake.date_of_birth(minimum_age=18, maximum_age=60),
        }
        students.append(student)
    return students


def write_students_to_csv(students: List[dict]):
    """
    Write student data to a CSV file.

    Parameters:
    - students (List[dict]): A list of dictionaries containing student data.

    The CSV file will have the following columns:
    - first_name: First name of the student.
    - last_name: Last name of the student.
    - email: Email address of the student.
    - password: Password of the student.
    - date_of_birth: Date_of_birth of the student.
    This function creates or overwrites the existing CSV file specified by the CSV_FILE_PATH global variable.
    Returns:
    None
    """
    with open(CSV_FILE_PATH, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
        for student in students:
            writer.writerow(student)
