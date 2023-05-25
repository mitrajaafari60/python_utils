import re


def split_sentences(paragraph):
    sentences = re.split(r'(?<=[.!?])\s+', paragraph)
    text=""
    for sentence in sentences:
        words = sentence.split()  # Split the sentence into a list of words
        removed_first_word = ' '.join(words[1:])  # Join the words (excluding the first word) back into a sentence
        text = text+removed_first_word
    return text

def find_indexed_words(text):
    words = re.findall(r'\b[A-Z][a-z]*\b', text)
    indexed_words = {}
    index = 2

    for word in words:
        isEnd=False
        if word[-1] == '.' or word[-1] == ',':
            word = word[:-1]  # Remove trailing period or comma
            isEnd= True

        indexed_words[index] = word
        index += 1
        if isEnd:
            index += 1

    if indexed_words:
        for index, word in indexed_words.items():
            print(f"{index}:{word}")
    else:
        print("None")

text = input()

find_indexed_words(split_sentences(text))
