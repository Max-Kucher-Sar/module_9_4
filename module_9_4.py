from random import choice

# Lambda-функция:
first = 'Мама мыла раму'
second = 'Рамена мало было'
result = list(map((lambda x, y: x == y), first, second))
print(result)

# Замыкание:

def get_advanced_writer(file_name):
    file = open(file_name, 'w', encoding='utf-8')
    def write_everything(*data_set):
        for data in data_set:
            if isinstance(data, (list, tuple)):
                file.write(str(data) + '\n')
            else:
                file.write(str(data) + '\n')

    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

# Метод __call__:

class MysticBall:
    def __init__(self, *word):
        self.word = word

    def __call__(self):
        return choice(self.word)

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
