dictionary = {'ram':'he is a boy',
            'shyam':'he is ram friend',
            'apple':'red color',
            'mango':'sweet'}

#print(dictionary.items())

user_choise = input('search your word in dictionary: ')
if 1:
    if user_choise == 'ram' in dictionary:
        res = dictionary.get('ram')
        print(res)
        #print("word is present in dictionary")

    elif user_choise == 'shyam' in dictionary:
        res = dictionary.get('shyam')
        print(res)

    elif user_choise == 'apple' in dictionary:
        res = dictionary.get('apple')
        print(res)

    elif user_choise == 'mango' in dictionary:
        res = dictionary.get('mango')
        print(res)
    else:
        print("word is not present in dictionary")
        


