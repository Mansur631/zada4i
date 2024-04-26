def count_words(text):
    words = text.split()
    dictionary_word = {}
    for word in words:
        if dictionary_word.get(word) is not None:
            dictionary_word[word] += 1
        else:
            dictionary_word[word] = 1
    return dictionary_word


print(count_words("Вы можете изменить Вы логику функции в зависимости"))