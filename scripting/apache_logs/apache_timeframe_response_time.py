# python3

# 4. You implemented a rating feature on the website and users rate the website significantly worse between 6pm and 9pm. 
# Your boss thinks this is because there are more users during those hours which slows down the response time. 
# Evaluate whether:
# - This timeframe actually experiences most users.
# - The response time is actually slower during this timeframe.

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

file = './apache.log'

my_dict = {}
my_total = 0

with open(file, 'r') as log:
  for line in log:
    my_total += 1
    m = pattern.match(line)
    res = m.groupdict()
    dt_iso = datetime.strptime(res['time'], "%d/%b/%Y:%H:%M:%S %z")
    dt_custom = dt_iso.strftime("%H")
    if dt_custom in my_dict:
      my_dict[dt_custom]['count'] += 1
    else:
      my_dict[dt_custom] = {}
      my_dict[dt_custom]['count'] = 1
      my_dict[dt_custom]['status'] = {}
    if res['status'] in my_dict[dt_custom]['status']:
      my_dict[dt_custom]['status'][res['status']] += 1
    else:
      my_dict[dt_custom]['status'][res['status']] = 1
      
print('custom_date', 'count', 'percentage', 'status_obj')

for x in my_dict:
  my_pct = (int(my_dict[x]['count']) / my_total) * 100
  print(x, my_dict[x]['count'], round(my_pct, 2), my_dict[x]['status'])
