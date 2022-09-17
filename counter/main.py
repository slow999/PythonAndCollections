from collections import Counter

c = Counter(['a', 'b', 'c', 'c', 'b'])
print(c['a'])
print(c['d'])
c['d'] += 1

# print(sorted(c.elements()))
print(c.most_common(1))
print(list(c.elements()))