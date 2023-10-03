import json


def extract_operations_list(filename):
    """
    Извлекаем из файла список операций
    """
    with open(filename, "r", encoding="utf-8") as trans_file:
        operations = json.load(trans_file)
    return operations



def filter_executed(operations_list):
    """
    Оставляем только те записи, что EXECUTED
    """
    filtered_list = []

    for operation in operations_list:
        if operation.get("state") == "EXECUTED":
            filtered_list.append(operation)

    return filtered_list


def sort_for_date(filtered_file):
    """
    Сортируем список по полю date по убыванию
    """

    return sorted(filtered_file, key=lambda x: x["date"], reverse=True)


def make_card_number(card):
    """
    Если пустой текст, то отдаем пустую строку
    Если это счет, то в счете меняем на * всё кроме последних 4 цифр
    Иначе это карта, тогда разбиваем число в переданной строке на 4 блока по 4, причем в середине 6 - звёздочки
    """
    text_num = ""

    if not card:
        return text_num

    if "Счет" in card:
        return f"{card[:5]}{'*' * 16}{card[-4:]}"
    else:
        head = card[:-16]
        squad_1 = card[-16:-12]
        squad_2 = f"{card[-12:-9]}**"
        squad_3 = "****"
        squad_4 = card[-4:]
        return f"{head} {squad_1} {squad_2} {squad_3} {squad_4}"


def make_date(date):
    """
    Из даты формата 2019-08-26T10:50:58.294041
    делаем дату типа 26.08.2019
    """
    return f"{date[8:10]}.{date[5:7]}.{date[:4]}"


def comb_text(operation):
    """
    Формируем текст вида:
    14.10.2018 Перевод организации
    Visa Platinum 7000 79** **** 6361 -> Счет **9638
    82771.72 руб.
    """
    text = f"{make_date(operation['date'])} {operation['description']}" + "\n"
    text += f"{make_card_number(operation.get('from'))} -> {make_card_number(operation.get('to'))}" + "\n"
    text += f"{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}"

    return text
