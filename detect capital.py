f="USA"
b="leetcode"
e="Google"
a="flaG"

def detectCapitalUse(a):
    if  a[0].isupper():
        if a[1].isupper():
            flag = True
            for i in range(len(a)):
                if a[i].isupper():
                    continue
                else:
                    flag = False
            return flag 
        elif a[1] ==None:
            return True
        elif not a[1].isupper():
            flag = True
            for i in range(len(a)-2):
                if a[i+2].islower():
                    continue
                else:
                    return False
            return flag
    elif not a[0].isupper():
        flag=True
        for i in range(len(a)):
            if  a[i].islower():
                continue
            else:
                flag = False
        return flag



print(detectCapitalUse(a))