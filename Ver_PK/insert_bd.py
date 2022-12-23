import psycopg2
from psycopg2 import Error

user = input("Введите имя пользователя: ")
password = input("Введите пароль: ")
try:
    # Подключение к существующей базе данных
    connection = psycopg2.connect(user=user,
                                  password=password,
                                  host="db.local",
                                  port="5432",
                                  database="libraryMB")
    # Курсор для выполнения операций с базой данных
    cursor = connection.cursor()
    sql_create_database = ''' INSERT INTO public.books(book_id, title, author, publ_house, price, pages_cnt, pictures_cnt, book_year) VALUES (1, 'Капитанская дочка', 'Пушкин А.С.', 1836, 400, 123, 123, 123);
    INSERT INTO public.books(book_id, title, author, publ_house, price, pages_cnt, pictures_cnt, book_year) VALUES (2, 'Мастер и Марагарита', 'Булгаков М.А.', 1928, 300, 123, 123, 123);
    INSERT INTO public.books(book_id, title, author, publ_house, price, pages_cnt, pictures_cnt, book_year) VALUES (3, 'Война и мир', 'Толстой Л.Н.', 1863, 540, 123, 123, 123);
    INSERT INTO public.books(book_id, title, author, publ_house, price, pages_cnt, pictures_cnt, book_year) VALUES (4, 'Сумерки', 'Стефани Майер', 2005, 400, 123, 123, 123);
    
    INSERT INTO public.branches(br_name) VALUES ('Электро');
    INSERT INTO public.branches(br_name) VALUES ('Автаз');
    INSERT INTO public.branches(br_name) VALUES ('Павла Корчагина');
    INSERT INTO public.branches(br_name) VALUES ('Пряники');
    
    INSERT INTO public.storing(br_name, book_id, book_cnt) VALUES ('Электро', 4, 4);
    INSERT INTO public.storing(br_name, book_id, book_cnt) VALUES ('Автаз', 3, 22);
    INSERT INTO public.storing(br_name, book_id, book_cnt) VALUES ('Автаз', 1, 13);
	'''
    cursor.execute(sql_create_database)
    connection.commit()
except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")