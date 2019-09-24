# python3

# 2. Surface statistics on what kind of browsers tried to access the website.

import re

parts = [
  r'(?P<host>\S+)',       # host %h
  r'\S+',                 # indent %l (unused)
  r'(?P<user>\S+)',       # user %u
  r'\[(?P<time>.+)\]',    # time %t
  r'"(?P<request>.+)"',   # request "%r"
  r'(?P<status>[0-9]+)',  # status %>s
  r'(?P<size>\S+)',       # size %b (careful, can be '-')
  r'"(?P<referer>.*)"',   # referer "%{Referer}i"
  r'"(?P<agent>.*)"',     # user agent "%{User-agent}i"
]

pattern = re.compile(r'\s+'.join(parts)+r'\s*\Z')

file = './apache.logz'

my_dict = {}
my_total = 0

with open(file, 'r') as log:
  for line in log:
    my_total += 1
    m = pattern.match(line)
    res = m.groupdict()
    browser = res['agent'].split(' ')[0]
    if browser in my_dict:
      my_dict[browser] += 1
    else:
      my_dict[browser] = 1

print('browser', 'count', 'percentage')

for x in my_dict:
  my_pct = (int(my_dict[x]) / my_total) * 100
  print(x, my_dict[x], round(my_pct, 2))
