random_list=['2018-01-01', 'yandex', 'cpc', 100, "weasd", "asdasd", "dajkhkajsnd"]
dict={random_list[-2]:random_list[-1]}
for items in range(len(random_list)-3,-1,-1):
    dict={random_list[items]:dict}
print(dict)