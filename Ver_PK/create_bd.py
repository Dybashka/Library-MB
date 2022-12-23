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
    sql_create_database = '''CREATE TABLE books (
                                    book_id SERIAL PRIMARY KEY,
                                    title VARCHAR(50) NOT NULL,
                                    author VARCHAR(50) NOT NULL,
                                    publ_house VARCHAR(50) NOT NULL,
                                    price NUMERIC(9, 2) NOT NULL,
                                    pages_cnt INT NOT NULL,
                                    pictures_cnt INT,
                                    book_year INT NOT NULL
                                );

                                CREATE TABLE students (
                                    student_id SERIAL PRIMARY KEY,
                                    student_fname VARCHAR(30) NOT NULL,
                                    student_lname VARCHAR(30) NOT NULL,
                                    student_mname VARCHAR(30)
                                );

                                CREATE TABLE branches (
                                    br_name VARCHAR(50) PRIMARY KEY
                                );

                                CREATE TABLE departments (
                                    dp_name VARCHAR(50) PRIMARY KEY
                                );

                                CREATE TABLE issuance (
                                    book_id INT NOT NULL,
                                    student_id INT NOT NULL,
                                    PRIMARY KEY (book_id, student_id),
                                    FOREIGN KEY (book_id) REFERENCES books (book_id),
                                    FOREIGN KEY (student_id) REFERENCES students (student_id)
                                );

                                CREATE TABLE storing (
                                    br_name VARCHAR(50) NOT NULL,
                                    book_id INT NOT NULL,
                                    PRIMARY KEY(br_name, book_id),
                                    book_cnt INT NOT NULL,
                                    FOREIGN KEY (br_name) REFERENCES branches (br_name),
                                    FOREIGN KEY (book_id) REFERENCES books (book_id)
                                );

                                CREATE TABLE use (
                                    dp_name VARCHAR(50) NOT NULL,
                                    book_id INT NOT NULL,
                                    PRIMARY KEY(dp_name, book_id),
                                    FOREIGN KEY (dp_name) REFERENCES departments (dp_name),
                                    FOREIGN KEY (book_id) REFERENCES books (book_id)
                                );

                                CREATE TABLE belonging (
                                    br_name VARCHAR(50) NOT NULL,
                                    dp_name VARCHAR(50) NOT NULL,
                                    PRIMARY KEY(br_name, dp_name),
                                    FOREIGN KEY (br_name) REFERENCES branches (br_name),
                                    FOREIGN KEY (dp_name) REFERENCES departments (dp_name)
                                );'''
    cursor.execute(sql_create_database)
    connection.commit()
except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")