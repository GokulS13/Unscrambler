import tensorflow as tf
from itertools import permutations

def idictionary():
    dictionary = []
    try:
        file = open("/usr/share/dict/british-english", "r")
        fileContents = file.readlines()
    finally:
        file.close()
    for i in range(len(fileContents)):
        dictionary.extend(fileContents[i].split())
    return dictionary


dicto=idictionary()




ch=raw_input();
l=len(ch);
perms = [''.join(p) for p in permutations(ch)]

matchedWords = []


for word in dicto:
    count = 0
    for x in perms:
        if x == word:
            matchedWords.append(word)

print matchedWords
