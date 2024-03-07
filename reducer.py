from sys import stdin
index = {}

for line in stdin:
    word, num = line.split('\t')

    index.setdefault(word, 0)
    index[word] += int(num)
for word in index:
    print(f'{word}\t{index[word]}')