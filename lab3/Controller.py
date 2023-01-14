import psycopg2
from View import View_db
from Model import Model_db
from Model import s


class Controller_db:

    @staticmethod
    def get_table_list():
        print('''
                1. Author
                2. Books
                3. Reader
                4. Subscription''')

    @staticmethod
    def show_table(table_name):
        try:
            print('===========')
            Model_db.get_table_data(table_name)
        except (Exception, psycopg2.Error) as error:
            print("Не вдалося отримати дані таблиці", error)

    @staticmethod
    def get_columns_names(table_name):
        if table_name == 'author':
            View_db.show_author()
        elif table_name == 'books':
            View_db.show_books()
        elif table_name == 'reader':
            View_db.show_reader()
        elif table_name == 'subscription':
            View_db.show_subscription()
        else:
            print("Incorrect input")

    @staticmethod
    def digit_to_table_name():
        print('===========')
        number = input('Table : ')
        if str(number).isdigit():
            if number == '1':
                return 'author'
            elif number == '2':
                return 'books'
            elif number == '3':
                return 'reader'
            elif number == '4':
                return 'subscription'
        else:
            print('Incorrect input')
            Controller_db.digit_to_table_name()

    @staticmethod
    def table_name_to_pk(table_name):
        if table_name == 'books':
            return 'books_id'
        elif table_name == 'reader':
            return 'reader_id'
        elif table_name == 'author':
            return 'author_id'
        elif table_name == 'subscription':
            return 'subscription_id'
        else:
            print('Incorrect input')
            return ' '

    @staticmethod
    def insert(table_name, values):
        try:
            print('===========')
            Model_db.insert_data(table_name, values)
            View_db.display_insert(table_name, values)
        except (Exception, psycopg2.Error) as error:
            print("Не вдалося додати дані в таблицю", error)

    @staticmethod
    def delete(table_name, value):
        try:
            print('===========')
            Model_db.delete_data(table_name, value)
            View_db.display_delete(table_name, value)
        except (Exception, psycopg2.Error) as error:
            print("Не вдалося видалити дані з таблиці", error)

    @staticmethod
    def update(table_name, values):
        try:
            print('===========')
            Model_db.update_data(table_name, values)
            View_db.display_update(table_name, values)
        except (Exception, psycopg2.Error) as error:
            print("Не вдалося оновити дані в таблиці", error)

    @staticmethod
    def main_menu():
        is_exit = False
        while not is_exit:
            View_db.menu()
            choice = input('Menu: ')

            if choice == '0':
                is_exit = True
            elif choice == '1':
                Controller_db.get_table_list()
                tn = Controller_db.digit_to_table_name()
                print(tn)
                Controller_db.get_columns_names(tn)
                val = input("Values : ").split(' ')
                Controller_db.insert(tn, val)
            elif choice == '2':
                Controller_db.get_table_list()
                tn = Controller_db.digit_to_table_name()
                print(tn)
                Controller_db.get_columns_names(tn)
                val = input("Values : ")
                if val.isdigit():
                    Controller_db.delete(tn, val)
                else:
                    print('Incorrect input')
            elif choice == '3':
                Controller_db.get_table_list()
                tn = Controller_db.digit_to_table_name()
                print(tn)
                Controller_db.get_columns_names(tn)
                val = input("Values (without FKs) : ").split(' ')
                Controller_db.update(tn, val)
            else:
                print('Incorrect input')

            s.rollback()
