import os
import argparse
from collections import ChainMap


defaults = {'color': 'red', 'user': 'guest'}

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args()
command_line_args = {k: v for k, v in vars(namespace).items() if v}

combined = ChainMap(command_line_args, os.environ, defaults)

print(combined['color'])
print(combined['user'])

a = {'a': 1}
b = {'b': 2}
for x in b:
    a[x] = b[x]
print(a)

c = ChainMap(a, b)
print(c)