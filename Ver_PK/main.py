import psycopg2
import time
from psycopg2 import Error

def choice(n):
    connection = psycopg2.connect(user="postgres",
                                  password="library",
                                  host="172.17.0.3",
                                  port="5432",
                                  database="libraryMB")

    # Курсор для выполнения операций с базой данных
    cursor = connection.cursor()
    # Выполнение SQL-запроса
    cursor.execute("SELECT version();")
    # Получить результат
    #record = cursor.fetchone()
    #print("Вы подключены к - ", record, "\n")

    # if n != [1, 2, 3, 4, 5, 6, 7, 0]:
    # print('Error')
    # return "Fail"

    if n == 1:
        values = tuple(input("Введите через пробел: название филиала, id книги, кол-во книг\n").split())
        q = "INSERT INTO storing(br_name, book_id, book_cnt) VALUES (%s, %s, %s);"
        cursor.execute(q, values)
        connection.commit()
        return 'Success'
        connection.close()
    elif n == 2:
        values = tuple(input("Введите через пробел: название филиала,кол-во книг, id книги\n").split())
        q = "UPDATE %s SET book_cnt = %s WHERE book_id = %s"  # UPDATE books SET book_year = 2019 WHERE book_id = 5
        cursor.execute(q, values)
        connection.commit()
        return 'Success'
        connection.close()
    elif n == 3:
        q = "SELECT * FROM storing;"
        cursor.execute(q)
        mobile_records = cursor.fetchall()
        for row in mobile_records:
            print("название филиала =", row[0], )
            print("Id книги =", row[1])
            print("Количество книг =", row[2], "\n")
        return 'Success'
        connection.close()
    elif n == 4:
        q = "SELECT * FROM branches;"
        cursor.execute(q)
        mobile_records = cursor.fetchall()
        cnt = 0
        for row in mobile_records:
            print(row[0])
            cnt += 1
        return cnt
        connection.close()
    elif n == 5:
        print("non")
    elif n == 6:
        values = tuple(input("Введите id книги\n").split())
        q = "SELECT book_cnt from storing where book_id = %s"
        cursor.execute(q, values)
        mobile_records = cursor.fetchall()
        for row in mobile_records:
            print("Количество книг =", row[0], "\n")
        return 'Success'
        connection.close()
    elif n == 7:
        print("non")
    elif n == 0:
        connection.close()
    else:
        return "Fail"
    n = int(input("Введите действие: "))


#def auth(user,password):
    #if user == 'postgres' and password == 'library':
        #print('Вы подключены!')

    #else:
        #print('Неверные данные, доступ закрыт')
        #return 'auth Fail'

def menu():
    msg = """
        Выполнить:
        0. Завершение работы
        1. Добавление информации о книгах в библиотеку
        2. Изменить информацию о книге в библиотеке
        3. Посмотреть информацию о всех книгах в библиотеке
        4. Просмотр филиалов
        5  Добавить информацию о филиале
        6. Посчитать количество экземпляров указанной книги
        7. Для указанной книги посчитать количество факультетов, на которых она используется в данном филиале, и вывести названия этих факультетов
        """
    #n = int(input(msg))
    print(msg)
    #n = int(input(msg))
    n = 0
    choice(n)


print('Welcome to Library-MB!')
menu()
#user = input("Введите имя пользователя: ")  # postgres
#password = input("Введите пароль: ")  # library
#auth(user,password)

"""
try:
    # Подключение к существующей базе данных
    connection = psycopg2.connect(user=user,
                                  password=password,
                                  host="172.19.0.2",
                                  port="5432",
                                  database="libraryMB")

    # Курсор для выполнения операций с базой данных
    cursor = connection.cursor()
    # Выполнение SQL-запроса
    cursor.execute("SELECT version();")
    # Получить результат
    record = cursor.fetchone()
    print("Вы подключены к - ", record, "\n")

    msg =
    Выполнить:
    0. Завершение работы
    1. Добавление информации о книгах в библиотеку
    2. Изменить информацию о книге в библиотеке
    3. Посмотреть информацию о всех книгах в библиотеке
    4. Просмотр филиалов
    5  Добавить информацию о филиале
    6. Посчитать количество экземпляров указанной книги
    7. Для указанной книги посчитать количество факультетов, на которых она используется в данном филиале, и вывести названия этих факультетов

    n = int(input(msg))
    choice(n)


except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
else:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")
        time.sleep(3)
"""
