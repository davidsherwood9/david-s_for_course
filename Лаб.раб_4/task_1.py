import json
file_path = "C:/Users/david/PycharmProjects/Course Python английский/Работа с источниками данных/" \
            "Лабораторная работа/Найти сумму произведений из списка словарей/input.json"
with open(file_path) as f:    # import of the dictionary with data from .json
    data = json.load(f)


def scr_x_wght(info):   # function "score x weight" defining
    sum_of_mul = 0    # zero value of "sum of score and weight production" for cycle
    for d in info:
        one_mul = d["score"] * d["weight"]    # one production defined
        sum_of_mul += one_mul    # sum of weight and score productions

    return round(sum_of_mul, 3)
print(scr_x_wght(data))
