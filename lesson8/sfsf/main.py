# # функция декоратора
# def result_message(func):
#     """Добавляет сообщение перед функцией."""
#
#     # локальная функция внутри декоратора
#     def wrapper(*args, **kwargs):
#         print('Результат операции:')
#         return func(*args, **kwargs)
#
#     return wrapper
#
# # привязываем декоратор к функции
# @result_message
# def summa(a, b):
#     """Возвращает сумму переданных a и b."""
#     return a + b
#
# print(summa(1, 2))
#=================================
# import time
#
# def timer(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         res = func(*args, **kwargs)
#         end_time = time.time()
#         print(f'программа выполнена за:{end_time - start_time} секунд')
#         return res
#     return wrapper
#
# @timer
# def nums(n):
#     for i in range(n):
#         print(i+1)
#
# print(nums(10_000_000))
# =======================================================
#
#
# def repeat(n):
#     def func_wrapper(func):
#         def wrapper(*args, **kwargs):
#             for i in range(n):
#                 func(*args, **kwargs)
#         return wrapper
#     return func_wrapper
#
# @repeat(10)
# def massage(massage):
#     print(massage)
#
# massage('hallo!')
#====================================================
# open('TEXT.txt', 'w').close()
#
# def txt(func):
#     def wrapper(*args, **kwargs):
#         f = open('TEXT.txt', 'a')
#         res = func(*args, **kwargs)
#         f.write(f'{str(res)}\n')
#         f.close()
#         return res
#     return wrapper
#
# def repeat(n):
#     def func_wrapper(func):
#         def wrapper(*args, **kwargs):
#             for i in range(n):
#                 func(*args, **kwargs)
#         return wrapper
#     return func_wrapper
#
# @repeat(10)
# @txt
# def calculate(a, b, operation='+'):
#     """
#         Получает на вход два числа и операцию.
#         Возвращает результат указанной операции с передаными числами.
#     """
#     if operation == '+':
#         return a + b
#     elif operation == '-':
#         return a - b
#     elif operation == '*':
#         return a * b
#     elif operation == '/':
#         return a / b
#     elif operation == '%':
#         return a % b
#     elif operation == '//':
#         return a // b
#     elif operation == '**':
#         return a ** b
#     else:
#         print('Указанная операция не распознана.')
#         return None
#
#
#
# calculate(1, 2, '/')
#=============================================


import telebot

TOKEN = '6300342207:AAFBgMVVmFI5Gp3UOe5F51AjXcODrEpOMlU'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(massage):
    bot.send_message(massage.chat.id, 'привет')

@bot.message_handler(commands=['my_command'])
def start(massage):
    bot.send_message(massage.chat.id, 'абоба')

@bot.message_handler(content_types=['text'])
def text(massage):
    bot.send_message(massage.chat.id, 'пользователь написал текст')
    if 'фото' in massage.text:
        with open('./img.png', 'rb') as image:
            bot.send_photo(massage.chat.id, image)
        for i in range(100):
            bot.send_photo(massage.chat.id, 'https://masterpiecer-images.s3.yandex.net/afebd78a54c211eea9bd3a7ca4cc1bdc:upscaled')

print('Сервер запущен.')
bot.polling(
    non_stop=True,
    interval=1
)