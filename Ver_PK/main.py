import psycopg2
import time
from psycopg2 import Error

print("ДОбро пожаловать ")
user = input("Введите имя пользователя: ")
password = input("Введите пароль: ")
try:
    # Подключение к существующей базе данных
    connection = psycopg2.connect(user=user,
                                  password=password,
                                  host="127.0.0.1",
                                  port="5432",
                                  database="libraryMB")

    # Курсор для выполнения операций с базой данных
    cursor = connection.cursor()
    # Выполнение SQL-запроса
    cursor.execute("SELECT version();")
    # Получить результат
    record = cursor.fetchone()
    print("Вы подключены к - ", record, "\n")
    msg = """
    Выполнить:
    0. Завершение работы
    1. Добавление информации о книгах в библиотеку
    2. Изменить информацию о книге в библиотеке
    3. Посмотреть информацию о всех книгах в библиотеке
    4. Добавить информацию о филиале
    5. Изменить информацию о филиале
    6. Для указанного филиала посчитать количество экземпляров указанной книги, находящихся в нем
    7. Для указанной книги посчитать количество факультетов, на которых она используется в данном филиале, и вывести названия этих факультетов
    """
    n = int(input(msg))
    while n != 0:
        if n == 1:
            values = list(input("Введите через пробел: название филиала, id киги, кол-во книг\n").split())
            for i in range(len(values)):
                values[i] = values[i].encode('utf-8', 'replace').decode('utf-8')
            values = tuple(values)
            q = "INSERT INTO storing(br_name, book_id, book_cnt) VALUES (%s, %s, %s);"
            cursor.execute(q, values)
            connection.commit()
        if n == 2:
            print("non")
        if n == 3:
            q = "SELECT * FROM storing;"
            cursor.execute(q)
            mobile_records = cursor.fetchall()
            print("Вывод каждой строки и ее столбцов")
            for row in mobile_records:
                print("название филиала =", row[0], )
                print("Id книги =", row[1])
                print("Количество книг =", row[2], "\n")
            connection.commit()
        if n == 4:
            print("non")
        if n == 5:
            print("non")
        if n == 6:
            print("non")
        if n == 7:
            print("non")
        n = int(input(msg))

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
else:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")
        time.sleep(3)
