import psycopg2


class Controller_db:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def get_table_list(self):
        try:
            print('===========')
            n = self.model.get_table_names()
            self.view.show_table(n)
        except (Exception, psycopg2.Error) as error:
            print("Не вдалося отримати назви таблиць", error)

    def get_columns(self, table_name):
        try:
            print('===========')
            cl = self.model.get_column_types(table_name)
            self.view.show(cl)
        except (Exception, psycopg2.Error) as error:
            print("Не вдалося отримати колонки таблиці", error)

    def get_names(self, table_name):
        try:
            # print('===========')
            cl = self.model.get_column_names(table_name)
            # self.view.show(cl)
            return cl
        except (Exception, psycopg2.Error) as error:
            print("Не вдалося отримати назви колонок таблиці", error)

    def show_table(self, table_name):
        try:
            print('===========')
            t = self.model.get_table_data(table_name)
            self.view.show(t)
        except (Exception, psycopg2.Error) as error:
            print("Не вдалося отримати дані таблиці", error)

    def digit_to_table_name(self):
        print('===========')
        number = input('Table : ')
        if str(number).isdigit():
            if number == '1':
                return 'books'
            elif number == '2':
                return 'reader'
            elif number == '3':
                return 'author'
            elif number == '4':
                return 'subscription'
        else:
            print('Incorrect input')
            self.digit_to_table_name()

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

    def insert(self, table_name, values):
        try:
            print('===========')
            self.model.insert_data(table_name, values)
            self.view.display_insert(table_name, values)
        except (Exception, psycopg2.Error) as error:
            print("Не вдалося додати дані в таблицю", error)

    def delete(self, table_name, column, value):
        try:
            print('===========')

            if table_name == 'author':
                self.delete_author(table_name, column, value)
            elif table_name == 'books':
                self.delete_books(table_name, column, value)
                # self.delete_author(table_name, column, value)
            elif table_name == 'reader':
                self.delete_reader(table_name, column, value)
                # self.delete_author(table_name, column, value)
            else:
                self.model.delete_data(table_name, column, value)
                self.view.display_delete(table_name, value)
        except (Exception, psycopg2.Error) as error:
            print("Не вдалося видалити дані з таблиці", error)

    def delete_author(self, table_name, column, value):
        try:
            print('===========')
            self.model.delete_with_fk('subscription', 'books', 'books_id', 'books_id', 'author_id', value)
            self.model.delete_data('books', 'author_id', value)
            self.model.delete_data(table_name, column, value)
            self.view.display_delete(table_name, value)
        except (Exception, psycopg2.Error) as error:
            print("Не вдалося видалити дані з таблиці author", error)

    def delete_books(self, table_name, column, value):
        try:
            print('===========')
            self.model.delete_data('subscription', 'books_id', value)
            self.model.delete_data(table_name, column, value)
            self.view.display_delete(table_name, value)
        except (Exception, psycopg2.Error) as error:
            print("Не вдалося видалити дані з таблиці books", error)

    def delete_reader(self, table_name, column, value):
        try:
            print('===========')
            self.model.delete_data('subscription', 'reader_id', value)
            self.model.delete_data(table_name, column, value)
            self.view.display_delete(table_name, value)
        except (Exception, psycopg2.Error) as error:
            print("Не вдалося видалити дані з таблиці reader", error)

    def update(self, table_name, values):
        try:
            print('===========')
            self.model.change_data(table_name, values)
            self.view.display_update(table_name, values)
        except (Exception, psycopg2.Error) as error:
            print("Не вдалося оновити дані в таблиці", error)

    def random(self, table_name, count):
        try:
            print('===========')
            self.model.generate_data(table_name, count)
            # self.show_table(table_name)
            self.view.display_random(table_name, count)
        except (Exception, psycopg2.Error) as error:
            print("Не вдалося згенерувати дані в таблиці", error)

    def search(self, num):
        try:
            print('===========')
            if num == '1':
                tname = 'Reader | Subscription'
                startd = input('Start date (xxxx-yy-zz) : ')
                dued = input('Due date (xxxx-yy-zz) : ')
                rname = input('Reader name : ')
                cond = str("s.startdate >= " + "'" + str(startd) + "'" + " AND s.duedate <= " + "'" + str(dued) + "'" +
                           " AND r.name LIKE " + "'" + str(rname) + "%'")
                # print(cond)
                c = self.model.join_reader_subscription(cond)
                if not c:
                    print("Row not found")
                else:
                    self.view.display_search(tname, cond)
                    self.view.show(c)
            elif num == '2':
                tname = 'Author | Books'
                b = input('(True or False : ')
                size = input('Book size : ')
                aname = input('Part of author name : ')
                cond = str("b.isavailable = " + str(b) + " AND b.size >= " + str(size)
                           + " AND a.name LIKE " + "'" + str(aname) + "%'")
                # print(cond)
                c = self.model.join_author_books(cond)
                if not c:
                    print("Row not found")
                else:
                    self.view.display_search(tname, cond)
                    self.view.show(c)
            elif num == '3':
                tname = 'Books | Subscription'
                ch = input('Part of book name : ')
                duedate = input('Due date (xxxx-yy-zz) : ')
                size = input('Book size : ')
                cond = str("b.name LIKE " + "'" + str(ch) + "%'"
                           + " AND s.duedate <= " + "'" + str(duedate) + "'"
                           + " AND b.size >= " + str(size))
                # print(cond)
                c = self.model.join_author_books(cond)
                if not c:
                    print("Row not found")
                else:
                    self.view.display_search(tname, cond)
                    self.view.show(c)
            else:
                print("Incorrect input")
        except (Exception, psycopg2.Error) as error:
            print("Не вдалося знайти дані в таблицях", error)

    def main_menu(self):
        is_exit = False
        while not is_exit:
            self.view.menu()
            choice = input('Menu: ')

            if choice == '0':
                is_exit = True
            elif choice == '1':
                self.get_table_list()
                tn = self.digit_to_table_name()
                print(tn)
                self.show_table(tn)
                self.model.clear_transaction()
            elif choice == '2':
                self.get_table_list()
                tn = self.digit_to_table_name()
                print(tn)
                self.get_columns(tn)
                columns = input("Columns (type all) : ").split()

                if columns == ['all']:
                    columns = self.get_names(tn)

                # print(columns)
                val = input("Values : ").split(' ')
                values = {key: value for (key, value) in zip(columns, val)}
                self.insert(tn, values)
                self.model.clear_transaction()
            elif choice == '3':
                self.get_table_list()
                tn = self.digit_to_table_name()
                print(tn)
                self.get_columns(tn)
                t_id = self.table_name_to_pk(tn)
                condition = input("Condition : ")
                self.delete(tn, t_id, condition)
                self.model.clear_transaction()
            elif choice == '4':
                self.get_table_list()
                tn = self.digit_to_table_name()
                print(tn)
                self.get_columns(tn)
                columns = (input("Column : ") + ' condition').split(' ')
                val1 = input("Change : ").split(' ')
                print('pk_id : ')
                val2 = (self.table_name_to_pk(tn) + '=' + input('')).split(' ')
                val = (val1 + val2)
                print(val)
                values = {key: value for (key, value) in zip(columns, val)}
                self.update(tn, values)
                self.model.clear_transaction()
            elif choice == '5':
                self.get_table_list()
                tn = self.digit_to_table_name()
                print(tn)
                count = input('Count : ')
                self.random(tn, count)
                self.model.clear_transaction()
            elif choice == '6':
                self.view.choose_option()
                c = input('Search : ')
                self.search(c)
                self.model.clear_transaction()
            else:
                print('Incorrect input')
