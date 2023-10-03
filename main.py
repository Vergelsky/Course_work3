from src import *


filename = "operations.json"

#Извлекаем из файла список операций
operations_list = extract_operations_list(filename)

#Оставляем только те, что EXECUTED
operations_list = filter_executed(operations_list)

#Сортируем список по полю date
operations_list = sort_for_date(operations_list)

#Выводим в консоль первые 5 элементов в правильном виде
for operation in operations_list[:5]:
    repr = comb_text(operation)
    print(repr, end="/n")