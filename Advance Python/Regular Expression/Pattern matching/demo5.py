import re
x="[0-9]"
matcher=re.finditer(x,"abt c@5Akz")
for match in matcher:
    print(match.start())
    print(match.group())