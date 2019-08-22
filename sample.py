import re

with open('log', 'r') as f:
    lines = f.readlines()
    for line in reversed(lines):
        if re.search('paused', line):
            print(re.findall('\d{1,6}', line)[0])
            break


# log file content
"""
started 123
stopped 245
paused  111
started 333
stopped 222
paused 444
started 555
stopped 333
paused 666
started 777
stopped 888"""

# Out Put:
"""
PS C:\Users\gopikrishna\Desktop> python .\sample.py
666
PS C:\Users\gopikrishna\Desktop>
"""
