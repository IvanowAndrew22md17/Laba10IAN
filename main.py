import json
x = int(input("введите номер задания:"))

#10.1
def f1():
    with open('10lab.json', encoding="utf-8") as j:
        s = json.load(j)
    for i in range(len(s.get('products'))):
        a = s.get('products')[i]
        print('Название: ' + str(a.get('name')))
        print('Цена: ' + str(a.get('price')))
        print('Вес: ' + str(a.get('weight')))
        if str(a.get('available: true')):
            print('В наличии')
        else:
            print('Нет в наличии!''\n')
if x==1:
    f1()

#10.2
def f2():
    with open('10lab.json', 'r', encoding='utf8') as j:
        s = json.load(j)
    for i in range(len(s.get('products'))):
        a = s.get('products')[i]
        print('Название: ' + str(a.get('name')))
        print('Цена: ' + str(a.get('price')))
        print('Вес: ' + str(a.get('weight')))
        if str(a.get('name')):
            print('В наличии')
        else:
            print('Нет в наличии!''\n')
        print('')
    ent = {}
    ent['name'] = input('Название: ')
    ent['price'] = input('Цена: ')
    ent['available'] = input('В наличии?: ')
    ent['weight'] = input('Вес: ')
    s['products'].append(ent)
    with open('10lab.json', 'w', encoding='utf8') as j:
        json.dump(s, j, indent=4, ensure_ascii=False)
        print(s)
if x==2:
    f2()

#10.3
def f3():
    d = open('en-ru.txt ', encoding="utf-8").read().split('\n')
    s = {}
    for i in range(len(d)):
        d[i] = d[i].split(' - ')
        s[d[i][0]] = d[i][1:]
    print(s)
    a = {}
    for i in s:
        for k in s[i]:
            k = k.split(', ')
            for j in k:
                if j not in a:
                    a[j] = i
                else:
                    a[j] = a[j] + ', ' + i
    a = dict(sorted(a.items()))
    print(a)
if x==3:
    f3()
if x< 0 or x > 3:
    print("Такой задачи нет(")