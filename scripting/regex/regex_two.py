# python3

# Write a script that prints out all lines in the text that contain a word that start with a 'q' or a 'Q'.
# Count the number of words that contain two consecutive vowels.
# Count the number of lines where one word occurs twice.

import re

file = './jumping_frog.txt'

print_line = 0

with open(file, 'r') as log:
  for line in log:
    words = line.split(' ')
    for word in words:
      satisfy = re.findall('\Aq|\AQ', word)
      if (satisfy):
        print('>>>', word)
        print_line = 1
    if (print_line):
      print(line)  
    print_line = 0