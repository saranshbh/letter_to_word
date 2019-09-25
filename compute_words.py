
import pandas as pd
import numpy as np
from nltk.corpus import brown
import itertools
import time

# Word check size is:
print('Sample size is: ' + str(len(brown.words())))

# Take input of letters needed
words_list = []
words_list = brown.words()
word_list = np.array(words_list)
num = input("Enter how many elements you want:")
print('Enter characters on paper: ')
num_array = []
all_words = []

# Take input of letters
for i in range(int(num)):
    n = input("num :")
    num_array.append(n)
print('ARRAY: ', num_array)

# Concatenate all words into the list
for i in range(4, int(num)+1):
    for subset in itertools.permutations(num_array, i):
        all_words.append(''.join(subset))

all_words = list(set(all_words))

final = np.array(all_words)
all_words = []
list_len = len(final)

print('Total Word Count in test size is: ' + str(list_len))

start_time = time.time()

# Check for all valid words
for word in final:
    if word.lower() in word_list:
        all_words.append(word)
    print("--- %s seconds ---" % (time.time() - start_time))

