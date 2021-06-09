import re
x="[A-Z]"
matcher=re.finditer(x,"abt c@5kGz")
for match in matcher:
    print(match.start())
    print(match.group())