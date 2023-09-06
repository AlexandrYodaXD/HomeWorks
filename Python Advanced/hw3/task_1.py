# ✔ Три друга взяли вещи в поход. Сформируйте
# словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции
# с множествами. Код должен расширяться
# на любое большее количество друзей

friends = {
    'Kirill "Stone" P.': ('water', 'bread', 'guitar', 'knife'),
    'Alexander "YodaXD" A.': ('sausages', 'mangal', 'knife', 'water'),
    'Anton "Stuffy" M.': ('stuffy questions', 'water', 'matches', 'bread')
}

friends_sets_list = [set(i) for i in friends.values()]
q1 = 'Какие вещи взяли все три друга'
a1 = set.intersection(*friends_sets_list)
print(f"{q1}: {', '.join(a1)}")


q2 = "Какие вещи уникальны, есть только у одного друга"
a2 = set()
v = list(friends.values())
for i in range(len(v)):
    segment = v[:i] + v[i+1:]
    if i == len(v) - 1:
        segment = v[:-1]
    a2 = a2 | (set(v[i]) - set.union(*map(set, segment)))
print(f"{q2}: {', '.join(a2)}")


q3 = "Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует"
a3 = {}

items_set = set.union(*[set(x) for x in friends.values()])
friends_set = set(friends.keys())
items_to_friends = {item: set() for item in items_set}

for k, v in friends.items():
    for item in v:
        items_to_friends[item].add(k)

for k, v in items_to_friends.items():
    items_to_friends[k] = friends_set - v

a3 = {k: v.pop() for k, v in items_to_friends.items() if len(v) == 1}
print(q3)
for item, friend in a3.items():
    print(f'\tтолько {friend} не взял {item}')
