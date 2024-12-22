# TODO импортировать необходимые молули
import json  # подключение библиотеки json
import csv  # подключение библиотеки csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"
indent = 4  # отступ для json в 4 пробела по заданию


def task():
    list = []  # пустой список

    # Десериализация из csv в список словарей при помощи .DictReader
    with open(INPUT_FILENAME, 'r') as f_csv:
        reader = csv.DictReader(f_csv)

        # Перевод из типа данных `OrderedDict` в обыкновенный словарь
        for row in reader:
            list.append(row)

    # Сериализация списка словарей в формат json
    with open(OUTPUT_FILENAME, 'w') as f_json:
        json.dump(list, f_json, indent=indent)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
