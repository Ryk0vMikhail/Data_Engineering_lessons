class Connect:
    def __init__(self):
        self.data = []

    def add_person(self, person_data):
        if not isinstance(person_data, dict):
            raise TypeError('Person data must be a dict')
        self.data.append(person_data)

    def get_all_person_date(self):
        return self.data

    def get_name_person_data(self, v_name):
        for person in self.data:
            if person['name'] == v_name:
                return person
            else:
                return f'Not name for data'

    def delete_person_data(self, name):
        for person in self.data:
            if person['name'] == name:
                self.data.remove(person)

    def rename_age_person_data(self, name, age):
        for person in self.data:
            if person['name'] == name:
                person['age'] = age
            else:
                return f'Not name for data'


d_one = Connect()
d_one.add_person({'name': 'Mikhail', 'surname': 'Popov', 'age': 21})
d_one.add_person({'name': 'Sofi', 'surname': 'Popova', 'age': 18})
print(d_one.get_all_person_date())

print(d_one.get_name_person_data('Mikhail'))

print(d_one.get_all_person_date())

d_one.delete_person_data('Mikhail')
d_one.rename_age_person_data('Sofi', 13)
print(d_one.get_all_person_date())

