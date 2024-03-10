from typing import List


def return_cities_by_genre(data: List[tuple]) -> List[tuple]:
    result_list = []
    init_value = 1
    for el in data:
        if el[1] >= init_value:
            init_value = el[1]
            result_list.append(el)
    return result_list
