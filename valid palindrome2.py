s="abbbca"
def validpalindrome(s):
    l,r = 0,len(s)-1
    if not s:
        return True
    while l<r:
        if s[l]!=s[r]:
            one, two = s[l:r], s[l+1:r+1]
            print(one, two)
            return one==one[::-1] or two==two[::-1]
        l+=1;r-=1
    
    return True

print(validpalindrome(s))