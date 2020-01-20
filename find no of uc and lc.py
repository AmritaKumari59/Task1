str = input("enter any sentence\n")
lc = 0
uc=0
for i in str:
    if i>='a' and i<='z':
        lc +=1
    elif i>='A' and i<='Z':
        uc +=1
print("LowerCase: ",lc,"\nUpperCase:",uc)
