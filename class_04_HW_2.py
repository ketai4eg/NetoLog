ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}
list_unique=[]
for val in list(ids.values()):
       for id in val:
              if id not in list_unique:
                     list_unique.append(id)
print(list_unique)