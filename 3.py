def dictionary(n):
    dict = {}
    for i in range(n):
        word_1, word_2 = input('enter the word and its antonym separated by a space: ').split()
        dict[word_1] = word_2
        dict[word_2] = word_1
    return dict


def antonyms(dct, wrd):
    antonym = dct.get(wrd, wrd)
    return antonym


num = int(input('enter the number of words-pairs: '))
word = input('enter the word to find the antonym for: ')
words = dictionary(num)
print(antonyms(words, word))