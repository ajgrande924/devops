# python3

# Count the number of lines where one word occurs twice.

import re

file = './jumping_frog.txt'

print_line = 0

with open(file, 'r') as log:
  for line in log:
    words = line.split(' ')
    if len(words) != len(set(words)):
      print_line += 1
      
print('# of lines where one word occurs twice:', print_line)
