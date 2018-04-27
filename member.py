import random
import string

class Member:
    '''A member of the bank.'''

    def __init__(self, firstname, lastname, telephone, email=None, balance=0, account_number=None):
        self.firstname = firstname
        self.lastname = lastname
        self.telephone = telephone
        self.balance = balance

    def get_email(self):
        return '{}.{}@gmail.com'.format(self.firstname.lower(), self.lastname.lower())

    def fullname(self):
        return '{} {}'.format(self.firstname, self.lastname)

    def generate_account_number(self):
        self.account_number = ''
        account_number_length = 20
        characters = string.ascii_uppercase + string.digits

        for i in range(account_number_length):
            self.account_number += characters[random.randint(0, len(characters)-1)]

        return self.account_number

    def account_number(self):
        account_number = self.generate_account_number()
        return account_number

    def set_balance(self, new_balance):
        self.balance = new_balance

    def deposit(self, amount):
        if  isinstance(amount, int) == True:
            if amount > 1 and amount < 10000:
                self.balance += amount
            else:
                print('You can only deposit between 1 - 100000 Shillings')
        else:
            print('Please deposit a valid amount')
        return self.balance

    def withdraw(self, amount):
        if isinstance(amount, int) == True:
            if amount > 1 and amount <= 10000:
                if amount < self.balance:
                    self.balance -= amount
                else:
                    print('You can only Withraw between 1 - 100000 Shillings')
            else:
                print('The amount exceeds your balance of {}'.format(self.balance))
        else:
            print('Please withdraw a valid amount')
        return self.balance

    def get_balance(self):
        return self.balance

    def __str__(self):
        return 'Member {}: {}'.format(self.fullname, self.account_number)




# m = Member('Erick', 'Mwaz', '0723456782',  3000)
# print(m.email())
# print(m.fullname())
# print(m.account_number())
# print(m.get_balance())
