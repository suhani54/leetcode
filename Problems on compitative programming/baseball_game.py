#baseball game
class Solution:
    def calpoints(self,operations: List[str])-> int:
        lst=[]
        for i in operations:
            if i=="C":
                lst.pop()
            elif i=="D":
                lst.appened(lst[-1]*2)
            elif i=="+":
                s=lst[-2]+lst[-1]
                lst.append(s)
            else:
                lst.append(int(i))
        print(lst)
        return sum(lst)
                
                
                  
                  
