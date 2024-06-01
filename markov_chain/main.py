# Markov chain sentence generator
# Use Markov chains to generate random sentences based on a given text.
# The text can be a sentence, a paragraph or a whole book.
# The Markov chain model will be based on the frequency of words appearing after each other.
# The more text you provide, the more accurate the sentences will be.
sentence_length = 100

import random

"""
loop through all the words
for every word, check if the previous word is in the dictionary as a key
if it is, add this word to the list value for the key
if it is not, make a dictionary with the previous word as the key and the current word as a value
"""


def markov_chain(text):
    text_list = text.split()
    dictionary = {}
    for j, i in enumerate(
        text_list
    ):  # j is index, i is the word, first index is removed to present it from looping all the way around
        if text_list[j - 1] in dictionary.keys():
            dictionary[text_list[j - 1]] = dictionary[text_list[j - 1]] + i.split()
        else:
            dictionary.update({text_list[j - 1]: i.split()})
        pass
    return dictionary


"""
generate a string with n words using m model, where m is the dictonary generated from markov_chain()
chooose a random wrod from m.keys
add that word to output string
choose a random word from the value dictionary
add that to the output string
repeat n-1 times because the inital word counts


"""


def generate_sentence(length, model):
    output = ""
    current_word = random.choice(list(model.keys()))
    output += current_word
    for i in range(length):
        current_word = random.choice(model[current_word])
        output += " " + current_word
    return output


with open("input.txt", "r") as file:
    text_input = file.read()

model = markov_chain(text_input)


print(generate_sentence(sentence_length, model))
