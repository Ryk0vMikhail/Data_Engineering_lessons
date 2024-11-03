import json

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


    def delete_person_data(self, name):
        for person in self.data:
            if person['name'] == name:
                self.data.remove(person)

    def rename_age_person_data(self, name, age):
        for person in self.data:
            if person['name'] == name:
                person['age'] = age

dict2 = {'a': 2, 'b': 5}

d_one = Connect()
d_one.add_person({'name': 'Mikhail', 'surname': 'Popov', 'age': 21})
d_one.add_person({'name': 'Sofa', 'surname': 'Popova', 'age': 25})

get_person = d_one.get_name_person_data('Sofa')

json_object = json.dumps(get_person, indent=4)


with open("sample.json", "w") as outfile:
    outfile.write(json_object)

with open("sample.json", 'r') as openfile:
    json_object = json.load(openfile)

print(json_object)

print(json_object['name'])

merged_dict = json_object | dict2

print(merged_dict)
