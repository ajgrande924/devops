# python3

# 3. What is the average number of requests per day? - (# of days / total requests?)

import re
from datetime import datetime

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
    dt_iso = datetime.strptime(res['time'], "%d/%b/%Y:%H:%M:%S %z")
    dt_custom = dt_iso.strftime("%m_%d_%y")
    if dt_custom in my_dict:
      my_dict[dt_custom] += 1
    else:
      my_dict[dt_custom] = 1

print('custom_date', 'count', 'percentage')

for x in my_dict:
  my_pct = (int(my_dict[x]) / my_total) * 100
  print(x, my_dict[x], round(my_pct, 2))
