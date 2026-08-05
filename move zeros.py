class Solution(object):
    def moveZeroes(self, nums):
        num=[]
        zeros=[]
        if nums==0:
            zeros.append(nums)
        if nums!=0:
            num.append(nums)
print(num+zeros)
