import sqlite3

class MemberOperations:
    ''' A class representation of a bank.'''

    def __init__(self, db_name='bank.db'):
        self.db_name = db_name
        self.conn = None
        self.cursor = None


    def connect(self):
        '''Connect to the database.'''
        self.conn = sqlite3.connect(self.db_name)
        # acces the columns of query by name instead of index
        self.conn.row_factory = sqlite3.Row

    def get_cursor_object(self):
        self.cursor = self.conn.cursor()

    def disconnect(self):
        '''Database disconnection.'''
        try:
            self.conn.close()
        except AttributeError:
            print('Make an Initial connection to the database')

    def create_table(self):
        '''Create a database table.'''

        with self.conn:
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS members (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    account_number VARCHAR (10) UNIQUE NOT NULL,
                    firstname TEXT NOT NULL,
                    lastname TEXT NOT NULL,
                    telephone VARCHAR (10) NOT NULL,
                    email VARCHAR (255) NOT NULL,
                    balance INTEGER (8)
                )
            ''')

    def insert_single_member(self, member):
        '''Insert a member into the bank.'''

        with self.conn:
            self.cursor.execute(
                '''INSERT INTO members (account_number, firstname, lastname, telephone, email, balance)
                    VALUES(:account_number, :firstname, :lastname, :telephone, :email, :balance)''',
                {'account_number': member.account_number, 'firstname': member.firstname,
                'lastname': member.lastname, 'telephone': member.telephone,
                'email': email, 'balance': balance}
            )

    def insert_many_members(self, members):
        '''Insert many members into the bank.'''

        with self.conn:
            self.cursor.executemany(
                '''INSERT INTO members (account_number, firstname, lastname, telephone, email, balance)
                    VALUES(:account_number, :firstname, :lastname, :telephone, :email, :balance)''',
                    members
            )

    def find_member_by_telephone(self, telephone):
        '''Find a member by their account number'''

        with self.conn:
            found_member = self.cursor.execute(
                    '''SELECT DISTINCT * FROM members WHERE telephone = :telephone''',
                    {'telephone': telephone}
            )
        return found_member.fetchone()

    def update_balance(self, telephone, balance):
        found_member = self.find_member_by_telephone(telephone)

        if found_member is not None:
            self.cursor.execute(
                '''UPDATE members SET balance = :balance WHERE telephone = :telephone''',
                {'balance': balance, 'telephone': telephone}
            )
            self.conn.commit()
        else:
            print('The member with this account number does not exist')

    def remove_member(self, member):
        '''Delete a member from the bank.'''

        found_member = self.find_member(member)

        if found_member is not None:
            self.cursor.execute(
                '''DELETE FROM members WHERE account_number = :account_number''',
                {'account_number': member.account_number}
            )
            self.conn.commit()
        else:
            print('The member with this account number does not exist')


    def search_member_by_account_number(self, account_number):
        '''Search a member by their account number'''
        self.conn.row_factory = sqlite3.Row

        with self.conn:
            found_member = self.cursor.execute(
                    '''SELECT DISTINCT * FROM members WHERE account_number = :account_number''',
                    {'account_number': account_number}
            )
            found_member.fetchone()

        if found_member:
            self.cursor.execute(
                    '''SELECT DISTINCT * FROM members WHERE account_number = :account_number''',
                    {'account_number': account_number}
            )
            for row in self.cursor:
                print('{}: {} - {} {}, {}, {}'
                    .format(row['id'], row['account_number'], row['firstname'],
                            row['lastname'], row['telephone'],  row['email'],
                            row['balance'])
                    )

        else:
            print('The member with this account number does not exist')


    def get_all_members(self):
        with self.conn:
            self.cursor.execute('SELECT DISTINCT * FROM members')

            for row in self.cursor:
                print('{}: {} - {} {}, {}, {}, {}'
                    .format(row['id'], row['account_number'], row['firstname'],
                            row['lastname'], row['telephone'], row['email'], row['balance']))
