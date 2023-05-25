def translate_sentence(dictionary, sentence):
    translations = []
    words = sentence.split()
    
    for word in words:
        if word in dictionary:
            translations.append(dictionary[word])
        else:
            translations.append(word)

    translated_sentence = ' '.join(translations)
    return translated_sentence

n = int(input())
dictionary = {}
for _ in range(n):
    word, english, french, german = input().split()
    dictionary[english] = word
    dictionary[french] = word
    dictionary[german]= word

sentence = input()

translated_sentence = translate_sentence(dictionary, sentence)
print(translated_sentence)
