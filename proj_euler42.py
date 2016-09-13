#proj_euler42.py

import numpy as np

t_n = np.zeros((100))
for n in range(1,100):
    t_n[n-1] = 0.5*n*(n+1)

fp = open("p042_words.txt")
wordlist = [word.strip() for line in fp.readlines() for word in line.split(',') if word.strip()]

n_triangle_words = 0

for current_word in range(0,len(wordlist)):
    word_total = 0
    for i in range(1,len(wordlist[current_word])-1):
        word_total += ord(wordlist[current_word][i]) - 64
    if word_total in t_n:
        n_triangle_words += 1

print n_triangle_words
#162 is correct answer