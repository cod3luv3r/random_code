def anagramTest(str1, str2):

    dict1 = {}
    dict2 = {}

    for letters in str1:

        if letters != ' ':

            if letters in dict1:
                dict1[letters] += 1
            else:
                dict1[letters] = 0

    for letters in str2:

        if letters != ' ':

            if letters in dict2:
                dict2[letters] += 1
            else:
                dict2[letters] = 0

    return (dict1 == dict2)


print(anagramTest('apple', 'apple'))
