import json #подключение библиотеки json

# TODO решите задачу
def task() -> float:
    filename = 'input.json' #задание переменной с названием JSON файла
    sum = 0 #сумма произведений

    with open(filename) as file: #открытие файла для чтения
        data = json.load(file) #запись списка словарей из json файла в переменную

    for i in data:
        sum = sum + i.get("score") * i.get("weight") #подсчёт результата

    return round(sum, 3)

print(task())
