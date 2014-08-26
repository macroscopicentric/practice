#One-time use to create dict of sorted words for wordplay.
import json
import collections

with open("sowpods.txt") as f:
    d = set(f.read().split('\n'))

with open('sowpods_sorted.txt', 'w') as f:
    sorted_words = collections.defaultdict(list)
    for word in d:
        sorted_words[''.join(sorted(word))] += [word]
    json.dump(sorted_words, f)