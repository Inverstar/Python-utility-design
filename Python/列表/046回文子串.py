#给定一个字符串，输出所有长度至少为2的回文子串。
#回文子串即从左往右输出和从右往左输出结果是一样的字符串，比如：abba，cccdeedccc都是回文字符串。
def isPalindrome(str):
    if str == str[::-1]:
        return True
    else:
        return False
s = input()
Palindrome = []
for i in range (len(s)-1):
    for j in range(i+2,len(s)+1):
        if isPalindrome(s[i:j]):
            Palindrome.append((i,s[i:j]))
Palindrome.sort(key = lambda x: (len(x[1]),x[0]))
for x in Palindrome:
    print(x[1])