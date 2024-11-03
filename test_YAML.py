import yaml


connection = [
    {
        'name': 'Name',
        'surname': 'Surname',
        'age': 23
    },
    {
        'one': 1,
        'two': 2
    }
]

with open('connections.yaml', 'w') as writefile:
    yaml.dump(connection, writefile)


with open('connections.yaml', 'r') as openfile:
    document = yaml.load(openfile, Loader=yaml.FullLoader)
    print(document)