import os


def read_data_file(file_path):
    """Read file in data folder and return its content as string"""
    data_folder = os.path.join(os.path.dirname(__file__), "data")
    file_path = os.path.join(data_folder, file_path)

    with open(file_path, "r", encoding="utf8") as file:
        file_content = file.read()

    return file_content
