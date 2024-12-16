def dictionary_counting(sent):
    dict = {}   #ключи это слова, а значения - количество их вхождений
    for word in sent:
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1
    sorted_dict = sorted(dict, key=dict.get, reverse=True)
    print(*sorted_dict)


sentence = input('enter the words separated by a space: ').lower().split()
dictionary_counting(sentence)
