from collections import Counter
def anagramInAString(s,p):
    k=len(p)
    pvalue=Counter(p)
    res=[]
    for i in range(len(s)-k+1):
        if Counter(s[i,i+k])==pvalue:
            res.append(i)
    return res
print(anagramInAString("cbaebabacd","abc"))