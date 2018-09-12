
'''Parses file - takes the first word and see if it already exsits - if it does it store on a new list '''


def create_festival_list(text_file):
    with open(text_file, 'r') as f:
        seen = set()
        events = set()
        for line in f:
            line_lower = line.lower()
            event = line_lower.split(' ')[0]
            if event in seen:
                events.add(event)
            else:
                seen.add(event)
        return events
