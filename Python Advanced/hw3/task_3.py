#  В большой текстовой строке подсчитать количество встречаемых
# слов и вернуть 10 самых частых. Не учитывать знаки препинания
# и регистр символов. За основу возьмите любую статью
# из википедии или из документации к языку

PUNCTUATION = '!"#$%&\'()*+,-./…:;<=>?@[\]^_`{|}~—«»“‘’”1234567890'

with open('task_3_data.txt', encoding='utf-8') as file:
    text = file.read().lower()
file.close()

for i in PUNCTUATION:
    while i in text:
        text = text.replace(i, ' ')

words_list = text.split()
words_dict = dict()

for i in words_list:
    words_dict[i] = words_dict.get(i, 0) + 1

print(f'Всего слов в тексте: {len(words_list)}')
print(f'Уникальных слов в тексте: {len(words_dict)}')

# создание списка ключей, отсортированных в порядке убывания их значения
sortedWords = sorted(words_dict, key=words_dict.get, reverse=True)

# Если есть слова, встречающиеся более одного раза, то выполняется этот блок.
if max(words_dict.values()) > 1:
    print(40 * '_')
    repeatedCount = 0
    repeatedResult = ''
    for i in sortedWords:
        if words_dict.get(i) > 1:
            repeatedCount += 1
            repeatedResult += f'\t\'{i}\' встречается {words_dict.get(i)} раз(-а)\n'
    print(f'{repeatedCount} повторяющихся слов(-а):')
    print(repeatedResult)
else:
    print('Нет повторяющихся слов')

# Если есть единожды встречающиеся слова, то этот блок выполняется.
if min(words_dict.values()) == 1:
    print(40 * '_')
    noRepeatedCount = 0
    noRepeatedResult = ''
    solo_words = []
    for i in sortedWords:
        if words_dict.get(i) == 1:
            solo_words.append(i)
    solo_words.sort()

    words_in_row = 10
    new_solo_words = []
    print(f'{len(solo_words)} единожды встречающихся cлов(-а):')
    for i in range(len(solo_words) // words_in_row):
        new_solo_words.append('\t' + ', '.join(solo_words[i * words_in_row:i * words_in_row + words_in_row]))
    print(',\n'.join(new_solo_words))
else:
    print('Нет слов, которые встречаются только один раз')
