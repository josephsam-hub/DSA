n=int(input())
x=0
while(n>0):
    a=input()
    if "++" in a:
        x+=1
    if "--" in a:
        x-=1
    n-=1
print(x)