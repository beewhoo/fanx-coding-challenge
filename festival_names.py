import sys
from festival_names_methods import create_festival_list


'''Program accepts file in command line if 'none'- program refers to the file data.txt'''

if __name__ == '__main__':
    if len(sys.argv) > 1:
        text_file = sys.argv[1]
    else:
        text_file = './data.txt'
    print('-------------Festival Names---------------')
    festival_names = create_festival_list(text_file)
    for festivals in festival_names:
        print festivals
    print('-------------------------------------')
