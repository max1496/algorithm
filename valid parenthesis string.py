def isvalid(s):
    stack = []
    c={')':'(','}':'{',']':'[',')':'*','}':'*',']':'*'}
    if len(s)==0:
        return True
    for i in s:
        if i =='(' or i=='[' or i=='{' or i=='*':
            stack.append(i)
        elif i ==')' or i==']' or i=='}':
            if c[i]==stack[-1]:
                stack.pop()
    return stack==[] or stack == ['*']
s="()"
print(isvalid(s))