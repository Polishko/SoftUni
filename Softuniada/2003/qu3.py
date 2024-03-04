# Longest Valid Parentheses

import re

input_str = input()
pattern = r'(\(\))+'

matches = re.finditer(pattern, input_str)

longest = 0
for match in matches:
    longest = max(len(match.group(0)), longest)

print(longest)
