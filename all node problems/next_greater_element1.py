class Solution:
    def nextGreaterElement(self,nums1 : List[int],num2:List[int]) ->List[int]:
        res=[]
        for i in nums1:
            c=0
            for j in range(num2.index(i),len(num2)):
                if(num2[i]>i):
                    res.append(num2[i])
                    c+=1
                    break
            if(c==0):
                res.append(-1)
        return res