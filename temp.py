geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]

tmp_list=[]

for visit in geo_logs:
    location = visit.values()
    for city, country in location:
        if country == 'Россия':
            tmp_list.append(visit)

geo_logs.clear()
geo_logs += tmp_list
print(type(geo_logs))
# for visit_ in geo_logs:
#     print(type(visit_))