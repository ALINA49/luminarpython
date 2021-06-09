
def isPalindrome(s):
    return s == s[::-1]
s=input("enter the string.")
res = isPalindrome(s)
if res:
    print(s)
else:
    print("no matching")