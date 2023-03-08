documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}

def get_name():
    number = input('Введите номер документа ')
    for data in documents:
        if data.get("number") == number:
            return data.get('name')
    return 'Документа с таким номером нет'

def get_shelf():
    number = input('Введите номер документа ')
    for key in directories:
        if number in directories.get(key):
            return key
    return 'В полках документа с данным номером нет.'

def get_list(docs):
    for doc in documents:
        return f"{doc['type']} {doc['number']} {doc['name']};"

def add_doc():
    shelf = input('Введите номер полки куда положить документ. ')
    if shelf not in directories:
        return 'Нет такой полки'
    doc = {}
    for info in ('type', 'number', 'name'):
        doc[info] = input(f'{info}: ')
    directories[shelf] = directories.get(shelf).append(doc['number'])
    return 'Документ добавлен'

while True:
    print('Возможные команды: p, s, l, a; q - выход')
    comand = input('Введите название команды: ')
    if comand == 'p':
        print(get_name())
    elif comand == 's':
        print(get_shelf())
    elif comand == 'l':
        print(get_list(documents))
    elif comand == 'a':
        print(add_doc())
    elif comand == 'q':
        break