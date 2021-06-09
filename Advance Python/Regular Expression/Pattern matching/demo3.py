import re
x="[abc]"
matcher=re.finditer(x,"ab c@5kz")
for match in matcher:
    print(match.start())
    print(match.group())