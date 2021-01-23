from ClientPethouse import Person


class Guest(Person):
    def __init__(self, name, city, status):
        Person.__init__(self, name)
        self.city = city
        self.status = status

    def __str__(self):
        return f'«{self.name}, г. {self.city}, статус "{self.status}"»'


class GuestList:
    def __init__(self, name, guest_list=None):
        if guest_list is None:
            guest_list = []
        self.guest_list = guest_list
        self.name = name

    def add_guest(self, guest):
        return self.guest_list.append(str(guest))

    def remove_guest(self, guest):
        if str(guest) in self.guest_list:
            return self.guest_list.remove(str(guest))

    def get_guest_list(self):
        if self.guest_list:
            print(f'Список гостей "{self.name}":')
            guest_list = ''
            for i in range(len(self.guest_list)):
                guest_list += f'{i + 1}. {self.guest_list[i]}\n'
            return guest_list
        else:
            return f'Список гостей "{self.name}" пуст\n'


guest_1 = Guest('Иван Петров', 'Москва', 'Наставник')
guest_2 = Guest('Петр Иванов', 'СПб', 'Наставник')
guest_3 = Guest('Василий Алексеев', 'Сызрань', 'Куратор')
guest_4 = Guest('Алексей Васильев', 'Киров', 'Координатор')

team_building = GuestList('Корпоратив')
team_building.add_guest(guest_1)
team_building.add_guest(guest_2)
print(team_building.get_guest_list())

christmas_party = GuestList('Рождественская вечеринка')
christmas_party.add_guest(guest_3)
christmas_party.add_guest(guest_4)
print(christmas_party.get_guest_list())

women_day = GuestList('8 марта')
print(women_day.get_guest_list())

christmas_party.remove_guest(guest_3)
print(christmas_party.get_guest_list())