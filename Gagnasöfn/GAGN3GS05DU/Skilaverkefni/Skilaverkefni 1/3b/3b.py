from good_or_bad_words import *
import re

good_word_count = 0
bad_word_count = 0

good_words_lower = [word.lower() for word in good_words]
bad_words_lower = [word.lower() for word in bad_words]

with open("3b/article.txt", "r", encoding="UTF-8") as skra:
    for lina in skra:
        for word in re.split(r"\W+", lina):
            if word.lower() in good_words_lower: good_word_count += 1
            if word.lower() in bad_words_lower: bad_word_count += 1

print("Number of good words:",good_word_count)
print("Number of bad words:",bad_word_count)