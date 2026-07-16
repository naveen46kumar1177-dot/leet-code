class Solution:
    def pivotIndex(self, l):
        for i in range(len(l)):
            pivot=i
            sum1=sum(l[0:pivot])
            sum2=sum(l[pivot+1:len(l)])
            if sum1==sum2:
                return pivot
        return -1