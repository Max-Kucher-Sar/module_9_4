# Lambda-функция:
first = 'Мама мыла раму'
second = 'Рамена мало было'
result = list(map((lambda x, y: x == y), first, second))
print(result)

# Замыкание:

def get_advanced_writer(file_name):
    with open(file_name, 'w') as file:
        def write_everything(*data_set):
            arguments = map(str, data_set)
            file.write(arguments)

    return write_everything

write = get_advanced_writer('example.txt')
result_2 = write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])