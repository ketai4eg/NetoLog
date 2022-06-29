stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 130, 'email': 42, 'ok': 98}
ref=0
for comp, num in stats.items():
    if int(num)>ref:
        ref=num
        thebestone=comp
print(thebestone)

print(max(stats))