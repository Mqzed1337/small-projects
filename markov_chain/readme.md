replace the text in input.txt with your input text
change sentence length at the top of main.py to specify how many words should be generated using the markov chain

current input text is [moby dick](https://www.gutenberg.org/cache/epub/2701/pg2701.txt)


further improvements:

pre generating the model and storing it as a json/csv
generating in a way that repeats of words are not stored seperately and instead a counter is present

checking if the hash of the input text matches the hash present in the model file


changes should allow for faster processing and allow for the processing of larger files