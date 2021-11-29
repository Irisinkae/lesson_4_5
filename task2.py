import collections
persons = [
    {
        "name": "Anna",
        "age": 9,
        "gender": "female"
    }, {
        "name": "Feris",
        "age": 36,
        "gender": "male",
    },{
        "name": "Frederik",
        "age": 37,
        "gender": "male"
    },{
        "name": "Anna",
        "age": 45,
        "gender": "female"
    },{
        "name": "Lina",
        "age": 5,
        "gender": "female"
    }, {
        "name": "Feris",
        "age": 63,
        "gender": "male",
    }, {
        "name": "Filipp",
        "age": 36,
        "gender": "male",
    }, {
        "name": "Fiona",
        "age": 10,
        "gender": "female",
    }, {
        "name": "Irina",
        "age": 25,
        "gender": "female",
    }, {
        "name": "Leonid",
        "age": 45,
        "gender": "male",
    }, {
        "name": "Irina",
        "age": 33,
        "gender": "female",
    }, {
        "name": "Feris",
        "age": 34,
        "gender": "male",
    }, {
        "name": "Irina",
        "age": 32,
        "gender": "female",
    }, {
        "name": "Fedor",
        "age": 63,
        "gender": "male",
    }, {
        "name": "Irina",
        "age": 17,
        "gender": "female",
    }
]

all_people = len(persons)
all_name = [item['name'] for item in persons]
all_name_uniq = {item['name'] for item in persons}
men_count = len([item['gender'] for item in persons if item['gender']=='male'])
women_count = len([item['gender'] for item in persons if item['gender']=='female'])
old_count = len([item['age'] for item in persons if item['age']>=18])
ages={item['age'] for item in persons}
men_names_35 = [item['name'] for item in persons if item['gender']=='male' and item['age']>35 and str(item['name'])[0]=='F']
popular_names = dict(collections.Counter(all_name))
popular_names=sorted(popular_names, key=popular_names.get, reverse=True)
print(f'Количество людей в списке: {all_people}')
print(f'Количество мужчин: {men_count}')
print(f'Количество женщин: {women_count}')
print(f'Количество совершеннолетних: {old_count}')
print(f'Список всех имен: {all_name}')
print(f'Все имена без повторений по алфавиту: {sorted(all_name_uniq)}')
print(f'Отсортированный список всех возрастов без повторений: {sorted(ages)}')
print(f'3 самых популярных имени: {popular_names[:3]}')
print(f'Все имена на "F" мужчин старше 35 лет: {men_names_35}')


