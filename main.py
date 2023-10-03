from src.scripts import *

filename = "src/operations.json"



#Извлекаем из файла список операций
extracted_list = extract_operations_list(filename)

#Оставляем только те, что EXECUTED
filtered_list = filter_executed(extracted_list)

#Сортируем список по полю date
sorted_list = sort_for_date(filtered_list)

#Выводим в консоль первые 5 элементов в правильном виде
for operation in sorted_list[:5]:
    show = comb_text(operation) +"\n"
    print(show)
