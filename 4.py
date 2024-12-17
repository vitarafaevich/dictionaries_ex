def dictionary(num):
    dict = {}
    for i in range(num):
        line = input('enter the object type and some objects: ').split()
        dict[line[0]] = line[1:]      #value is a list
    return dict


def getting_form(dct, wrd):
    keys = []
    for key, value in dct.items():    #.items() returning tuple of all "key-value" in the dict.
        if wrd in value:
            keys.append(key)
    if keys:
        return ''.join(keys)
    else:
        return "we don't have a key for your value"


number = int(input('enter the number of word-pairs: '))
word = input('enter the subject you want to know the shape of: ')
print(getting_form(dictionary(number), word))
