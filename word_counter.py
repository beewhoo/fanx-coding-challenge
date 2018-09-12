import sys
from word_counter_methods import *


'''Program accepts file in command line if none- program refers to the file test_most_common_words.txt'''

if __name__ == '__main__':
    if len(sys.argv) > 1:
        text_file = sys.argv[1]
    else:
        text_file = './tests/most_common_words.txt'
    occuring_words = ten_most_common_words(text_file)
    word_count = word_count(text_file)
    print('-------------program starting---------------')
    print("Loading file: %s" % (text_file))
    print ('------------word count---------------------')
    print "Word Count: %s" % (word_count)
    print ('------------most occuring words ordered------------')
    print "Top words: %s" %(occuring_words)
    print ('-------------------------------------------')
