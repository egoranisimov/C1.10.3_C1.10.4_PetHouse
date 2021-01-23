class Person:
    def __init__(self, name):
        self.name = name


class Client(Person):
    def __init__(self, name, balance):
        Person.__init__(self, name)
        self.balance = balance

    def change_balance(self, change_balance):
        if isinstance(change_balance, int):
            self.balance += change_balance

    def __str__(self):
        return f'Клиент "{self.name}". Баланс: {self.balance} руб.'


if __name__ == '__main__':
    client_1 = Client('Иван Петров', 50)
    client_2 = Client('Петр Иванов', 75)
    print(str(client_1), str(client_2), sep='\n', end='\n\n')

    client_1.change_balance(-25)
    client_2.change_balance(50)
    print(str(client_1), str(client_2), sep='\n', end='\n\n')
