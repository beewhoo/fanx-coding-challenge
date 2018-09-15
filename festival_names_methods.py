''' Unique list without loosing order '''

def unique_ordered(list):
    seen = []
    for f in list:
        if f not in seen:
            seen.append(f)
    return seen



''' Compares two lists - breaks when not matched - returns matched list or empty list'''

def compare_lists(list1, list2):
    match = []
    smaller_line = min(len(list1),len(list2))
    for i in range(0, smaller_line):
      if list1[i] == list2[i]:
          match.append(list1[i])
      else:
          break
    return ' '.join(match)


'''Opens file two lines at a time - splits two lines into two lists -calls compare lists and unique functions to return festival names'''

def open_file(text_file):
    with open(text_file, 'r') as f:
        festivals = []
        previous = next(f)
        for line in f:
            festival = compare_lists(previous.split(' '), line.split(' '))
            previous = line
            if festival != '':
                festivals.append(festival)
        return festivals
