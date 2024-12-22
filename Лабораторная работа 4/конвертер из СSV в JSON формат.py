import csv # TODO импортировать необходимые молули
import json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, mode='r', encoding='utf-8') as csv_file:  # TODO считать содержимое csv файла
        csv_reader = csv.DictReader(csv_file)
        data = [row for row in csv_reader]

    with open(OUTPUT_FILENAME, mode='w', encoding='utf-8') as json_file:  # TODO Сериализовать в файл с отступами равными 4
        json.dump(data, json_file, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
