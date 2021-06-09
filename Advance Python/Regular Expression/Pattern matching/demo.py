#pattern matching
#....................
#used for email matching
#pswrd matching etc
#package used here is 're'



import re
count =0
matcher=re.finditer("ab","abaaabbbab")
print(matcher)
for match in matcher:
    count+=1
print("count=",count)