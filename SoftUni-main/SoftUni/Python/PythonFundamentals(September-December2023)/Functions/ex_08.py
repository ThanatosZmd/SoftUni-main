def isPalindrome(a: str):
    if a == a[::-1]:
         return True
    return False

ints = list(input().split(", "))
for i in range(len(ints)):
     print(isPalindrome(ints[i]))