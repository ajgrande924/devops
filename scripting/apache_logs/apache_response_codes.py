# python3

# 1. Surface statistics of HTTP response codes: What percentage of requests return code 200, 400 etc?

file = './apache.log'

my_dict = {}
my_total = 0

with open(file, 'r') as log:
  for line in log:
    my_total += 1
    info = line.split(' ')
    if info[8] in my_dict:
      my_dict[info[8]] += 1
    else:
      my_dict[info[8]] = 1

print('response_code', 'count', 'percentage')

for x in my_dict:
  my_pct = (int(my_dict[x]) / my_total) * 100
  print(x, my_dict[x], round(my_pct, 2))
