import re
x="[^A-Za-z0-9]"
matcher=re.finditer(x,"ab c@5kz")
for match in matcher:
    print(match.start())
    print(match.group())