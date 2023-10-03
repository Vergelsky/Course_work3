
def extract_operations_list(filename):
    """
    Извлекаем из файла список операций
    """
    pass

def filter_executed(operations_list):
    """
    Оставляем только те записи, что EXECUTED
    """
    pass

def sort_for_date(operations_list):
    """
    Сортируем список по полю date по убыванию
    """
    pass

def make_card_number(card_number):
    """
    Разбиваем переданное число на 4 блока по 4, причем последние 6 - звёздочки
    """
    pass


def make_id_number(card_number):
    """
    Меняем первые два числа на звёздочки
    """
    pass


def make_date(card_number):
    """
    Из даты формата 2019-08-26T10:50:58.294041
    делаем дату типа 26.08.2019
    """
    pass


def comb_text(operation):
    """
    Формируем текст вида:
    14.10.2018 Перевод организации
    Visa Platinum 7000 79** **** 6361 -> Счет **9638
    82771.72 руб.
    """
    pass