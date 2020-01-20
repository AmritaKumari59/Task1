str = input("enter string\n")
a = [0]*256
for i in str:
    if a[ord(i)]==0:
        a[ord(i)]==1
        print(i,end="")
