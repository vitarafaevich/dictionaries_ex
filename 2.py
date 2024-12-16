def dictionary_translations(n):
    dict = {}
    for i in range(n):
        rus, eng = input('enter the word and its translation (u are russian) separated by a space: ').split()
        dict[rus] = eng
    return dict


def translate_text(dict, sent):
    trnsl = [dict.get(word, word) for word in sent]    #get(key, value)
    print(*trnsl)


number = int(input('enter the number of word-pairs: '))
sentence = input('enter the sentence to translate: ').split()
dictionary = dictionary_translations(number)
translate_text(dictionary, sentence)
