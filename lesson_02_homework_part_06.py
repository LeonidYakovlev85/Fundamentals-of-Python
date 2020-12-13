goods_dictionary = {'название': None, 'цена': None, 'количество': None, 'единица измерения': None}
goods_list = []

item_number = 0
while True:
    user_decision = input("Для ввода данных о товаре нажмите Enter, для завершения ввода данных введите 'Exit': ")
    if user_decision == '':
        item_number += 1
        goods_dictionary.update({'название': input("Введите название товара: ")})
        goods_dictionary.update({'цена': input("Введите цену товара, руб.: ")})
        goods_dictionary.update({'количество': input("Введите количество товара: ")})
        goods_dictionary.update({'единица измерения': input("Введите единицу измерения товара: ")})
        goods_tuple = [item_number, goods_dictionary.copy()]
        goods_list.append(tuple(goods_tuple))
    elif user_decision == 'Exit' or user_decision == 'exit':
        break

print("Вы создали структуру из следующих элементов: ")
for element in goods_list:
    print(element)

result_dictionary = {}
keys_list = list(goods_dictionary.keys())
for index, key in enumerate(keys_list):
    index_values_list = []
    for element in goods_list:
        element_values_list = list(element[1].values())
        index_element_value = element_values_list[index]
        index_values_list.append(index_element_value)
    result_dictionary.update({key: index_values_list})

print("\nАналитика о товарах выглядит следующим образом:")
for key, value in result_dictionary.items():
    print(f'{key}: {value}')
