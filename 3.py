def dictionary(n):
    dict = {}
    for i in range(n):
        wrd_1, wrd_2 = input('enter the word and its antonym separated by a space: ').split()
        dict[wrd_1] = wrd_2
        dict[wrd_2] = wrd_1
    print(dict)
    return dict


def antonyms(dct, wrd):
    antonym = dct.get(wrd, wrd)    #get(key, value), so it's (key, what to return)
    return antonym


num = int(input('enter the number of word-pairs: '))
word = input('enter the word to find the antonym for: ')
words = dictionary(num)
print(antonyms(words, word))
