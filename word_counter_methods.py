
import collections
from collections import OrderedDict
import string


'''Outputs the word count after removing punctuation'''
def word_count(text_file):
    counter = 0
    with open(text_file) as file:
        for line in file:
            counter += len(remove_punctuation_and_split(line))
    return counter

''' Remove punctuation and split words'''
def remove_punctuation_and_split(line):
        return line.translate(None,string.punctuation).split()

''' Top 10 words ordered'''
def ten_most_common_words(text_file):
    words = collections.Counter()
    with open(text_file, "r") as text_file:
         for line in text_file:
              words.update(remove_punctuation_and_split(line))
    return OrderedDict(words.most_common(10)).items()
