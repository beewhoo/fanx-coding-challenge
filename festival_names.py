import sys
from festival_names_methods import open_file, unique_ordered



'''Program accepts file in command line if 'none'- program refers to the file data.txt'''

if __name__ == '__main__':
    if len(sys.argv) > 1:
        text_file = sys.argv[1]
    else:
        text_file = 'data.txt'
festivals = open_file(text_file)
unique_festivals = unique_ordered(festivals)


print('----------FESTIVALS--------------')

for f in unique_festivals:
    print f
print('---------------------------------')
