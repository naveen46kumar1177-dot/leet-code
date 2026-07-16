def sortedSquares(l):
        r=[]
        for i in range(len(l)+1):
            s=l[i]**2
            r.append(s)
            f=sorted(r)
            print(f)
        return 
print(sortedSquares([-1,-4,0,3,10]))