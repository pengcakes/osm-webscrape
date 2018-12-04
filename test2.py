from pprint import pprint

d = {'word': 1, 'word1': 2}
d2 = {'word': 5, 'word1': 2}

pprint(d)
for key,val in d2.items():
    if key in d:
        d[key] = d[key].append(val)

pprint(d)