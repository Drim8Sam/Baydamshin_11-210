text = input('Введите текст: ')statistic = dict()for i in text:    if i.isalpha():        if i.lower() not in statistic.keys():            statistic[i.lower()] = 1        else:            statistic[i.lower()] += 1for key in statistic.keys():    print(key, '-', statistic[key])