def isvalid(s):
    stack = []
    c={')':'(','}':'{',']':'['}
    if len(s)==0:
        return True
    if len(s)%2==1:
        return False
    for i in s:
        if i=='(' or i=='[' or i=='{':
            stack.append(i)
        elif i==')' or i==']' or i=='}':
            if c(i)==stack(-1):
                stack.pop(-1)
        else:
            return False
    return stack == []
s="([])"
print(isvalid(s))