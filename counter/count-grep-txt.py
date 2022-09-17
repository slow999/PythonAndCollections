from collections import Counter
import re

words = re.findall(r'\w+', open('grep.txt').read().lower())
result = Counter(words).most_common(10)
print(result)
