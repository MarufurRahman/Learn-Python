# Regular expression in python.

import re

pattern = r'Bangla'
result = re.match(pattern, input())
if result:
    print("Found!")
else:
    print('Not Found.')
