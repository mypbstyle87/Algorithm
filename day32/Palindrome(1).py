# Palindrome!

def isPalindrome(s: str) -> bool:
    strs = []
    for char in s:
        if char.isalpha():
            strs.append(char)

    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False

    return True


s = input()
print(isPalindrome(s))
