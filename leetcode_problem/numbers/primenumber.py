a,b=1,100
for n in range(1,12):
    count=0
    for i in range(2,n):
        if n % i==0:
         count+=1
         if count==0:
            print("Prime number:")