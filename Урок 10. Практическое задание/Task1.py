"""
Задание 1.

Каждое из слов «разработка», «сокет», «декоратор» представить
в буквенном формате и проверить тип и содержание соответствующих переменных.
Затем с помощью онлайн-конвертера преобразовать
в набор кодовых точек Unicode (НО НЕ В БАЙТЫ!!!)
и также проверить тип и содержимое переменных.

Подсказки:
--- 'разработка' - буквенный формат
--- '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430' - набор кодовых точек
--- используйте списки и циклы, не дублируйте функции
"""

words = ['разработка', 'сокет', 'декоратор',
         '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430\u000a',
         '\u0441\u043e\u043a\u0435\u0442\u000a',
         '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440\u000a']
for el in words:
    print(f"{el} - {type(el)}")
