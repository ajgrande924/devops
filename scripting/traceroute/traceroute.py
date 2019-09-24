import argparse
import os

def dir_path(string):
  if os.path.isdir(string):
    return string
  else:
    raise NotADirectoryError(string)

def file_path(string):
  if os.path.isfile(string):
    return string
  else:
    raise FileNotFoundError(string)

parser = argparse.ArgumentParser()

parser.add_argument("-t", "--txt_path", type=file_path, help="traceroute text file path")

args = parser.parse_args()

print("file:", args.txt_path)

def count_hops(file):
  hops = 0
  with open(file, 'r') as log:
    for line in log:
      print(line, end="")
  print("Total # of hops:", hops)

count_hops(args.txt_path)


