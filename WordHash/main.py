# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
from WordsHashMap import WordsHashMap
import re

PUNCTUATIONS = '''!()-[]{};:'"\\,<>./?@#$%^&*_~'''

if __name__ == '__main__':

    size_str = input("Enter hashmap size wanted (by default choose 1033): ")
    size_int = 1033 if (size_str == '') else int(size_str)

    hashmap = WordsHashMap(size_int)

    f = open("wordsList.txt", "r", encoding="utf-8")
    data = f.readlines()
    f.close()

    for line in data:
        for word in line.split(' '):
            word = re.sub(r'\s+', '', word)
            if word == "":
                continue
            word = word.lower().strip(PUNCTUATIONS)
            hashmap.insert(word, 1)

    hashmap.delete("alice")
    print(hashmap.find("alice"))
    print(hashmap.print_hash())

    f = open("output.txt", "w", encoding="utf-8")
    f.write(hashmap.print_hash())
    f.close()
