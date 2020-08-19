def get_vocabulary():
    words = open('./data/words_alpha.txt')
    word_list = words.readlines()
    dict_words = {}
    for count in range(len(word_list)):
        dict_words[count] = word_list[count].rstrip().title()

    return dict_words
