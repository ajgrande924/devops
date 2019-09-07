# python3

# Write a script that prints out all lines in the text that contain a 'q'.

import re

file = './jumping_frog.txt'

with open(file, 'r') as log:
  for line in log:
    instances = re.findall('q', line) # list
    if len(instances) != 0:
      print(line)
