class solution:
    def minimumDiffernce(nums,k):
        if len(nums)<=1:
            return 0
        nums.sort()
        d=float('int')
        for i in range(len(nums)-k+1):
            diff=abs(nums[i]-nums[i+k-1])
            d=min(diff,d)
        return d