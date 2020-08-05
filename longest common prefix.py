
strs=["aa","aa"]

def longestCommonPrefix(strs):
    if len(strs) == 0:
        return ""
    lengths = [len(x) for x in strs]
    if min(lengths)==0:
        return ""
    if min(lengths)==1:
        return strs[0]
    
    for i in range(min(lengths)):
        tmp = ""
        flag = True
        #if strs[0][i] == strs[1][i]
        for j in range(len(strs)):
            if j == 0:
                tmp = strs[j][i]
                continue
            if strs[j][i] == tmp:
                continue
            else:
                flag = False
                break
        if flag:
            continue
        else:
            break
    return strs[0][:i]
print(longestCommonPrefix(strs))