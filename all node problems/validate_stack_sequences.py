class Solution:
    def validateStackSequences(self,pushed:List[int],popped: List[int])->bool:
        stack=[0]
        j=0
        for x in pushed:
            stack.append(x)
            while stack and stack[-1]==popped[j]:
                stack.pop()
                j+=1
        return stack ==[]