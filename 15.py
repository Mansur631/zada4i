def count_words(text):
    wordss = text.split()
    words = [word.capitalize() for word in wordss]
    dictionary_word = {}
    for word in words:
        if dictionary_word.get(word) is not None:
            dictionary_word[word] += 1
        else:
            dictionary_word[word] = 1
    return dictionary_word


def word_frequency(word, dictionary):
    for i in dictionary:
        if word == i:
            return dictionary[word]
    return None






# print(count_words("Вы можете изменить Вы логику функции в зависимости"))
dictionary = count_words("Вы можете изменить Вы логику функции в зависимости")
print(word_frequency("Можете",dictionary))