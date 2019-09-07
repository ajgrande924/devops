# python3

# Count the number of words that contain two consecutive vowels.

import re

file = './jumping_frog.txt'

print_line = 0

with open(file, 'r') as log:
  for line in log:
    words = line.split(' ')
    for word in words:
      satisfy = re.findall('aa|ee|ii|oo|uu', word.lower())
      if (satisfy):
        print('>>>', word)
        print_line = 1
    if (print_line):
      print(line)  
    print_line = 0