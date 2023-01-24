subjects_db = dict()

main_data = ['{Русский язык: {ФИО: Иванов И. И.; Оценки: [5, 5, 5, 4, 5]}, {ФИО: Петров П. П.; Оценки: [4, 5, 3, 4, 5]}',
        '{Математика: {ФИО: Иванов И. И., Оценки: [2, 3, 2, 4, 3]}, {ФИО: Петров П. П., Оценки: [5, 5, 2, 5, 5}}']

for subject in main_data:
    data = subject.split(': {')
    data[0] = data[0].replace('{', '')
    subjects_db[data[0]] = data[1]
    print(subjects_db)
    for key in subjects_db:
        subjects_db[key] = subjects_db[key].split('}, {')
        for i in range(len(subjects_db[key])):
            subjects_db[key][i] = subjects_db[key][i].split('; ')
            temp_dict = dict()
            for j in range(len(subjects_db[key][i])):
                subjects_db[key][i][j] = subjects_db[key][i][j].split(': ')
                temp_dict[subjects_db[key][i][j][0]] = subjects_db[key][i][j][1]
            subjects_db[key][i] = temp_dict
    print('THIS', subjects_db)
    for subject in subjects_db:
        for i in range(len(subjects_db[subject])):
            my_str = subjects_db[subject][i]['Оценки']
            subjects_db[subject][i]['Оценки'] = [int(x) for x in my_str if x.isdigit()]
            print(subjects_db[subject][i]['Оценки'])

print('FINAL', subjects_db)