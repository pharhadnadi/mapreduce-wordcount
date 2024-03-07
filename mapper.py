from sys import stdin
import re
for line in stdin:
    token = re.findall(r'\w+', line)
    for word in token:
        print(f'{word.lower()}\t1')