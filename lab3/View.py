class View_db:
    @staticmethod
    def show_table(db):
        i = 1
        for element in db:
            print(i, ': ', element)
            i += 1

    @staticmethod
    def show(db):
        for element in db:
            print(element)

    @staticmethod
    def menu():
        print('''
                1 : Insert
                2 : Delete
                3 : Update
                0 : Exit''')

    @staticmethod
    def show_author():
        print('''
                author_id
                name''')

    @staticmethod
    def show_books():
        print('''
                books_id
                author_id
                name
                size
                isavailable''')

    @staticmethod
    def show_reader():
        print('''
                reader_id
                name
                address
                number''')

    @staticmethod
    def show_subscription():
        print('''
                subscription_id
                books_id
                reader_id
                startdate
                duedate''')

    @staticmethod
    def display_insert(tname, insert):
        print('Successful insert', insert, 'in ', tname)

    @staticmethod
    def display_delete(tname, delete):
        print('Successful delete', delete, 'in ', tname)

    @staticmethod
    def display_update(tname, update):
        print('Successful update', update, 'in ', tname)

    @staticmethod
    def display_random(tname, random_count):
        print('Successful generation of', random_count, 'data in ', tname)

    @staticmethod
    def choose_option():
        print('''
                1 : Start date, Due date [date] ; Reader name [char] (Reader | Subscription)
                2 : IsAvailable [bool] ; Books size [int] ; Author name [char] (Author | Books)
                3 : Book name [char] ; Due date [date] ; Books size [int] (Books | Subscription''')

    @staticmethod
    def display_search(tname, search_res):
        print('Successful search of', search_res, ' in ', tname)
