'''
n= int(input())
def find(a,b):
    array= []
    target=1
    if a>b:
        temp1=a
        temp2=b
        array.append(temp1)
    else:
        temp1=b
        temp2=a
        array.append(temp1)
    while True:
        if temp1==1:
            break
        else:
            if temp1%2==0:
                temp1=temp1//2
            else:
                temp1=(temp1-1)//2
        array.append(temp1)
    while True:
        if temp2==1:
            break
        for j in range(len(array)):
            if temp2 ==array[j]:
                target=temp2
                break
        if target !=1:
            break
        if temp2%2==0:
            temp2=temp2//2
        else:
            temp2=(temp2-1)//2
    print(target*10)
    ##for x in array:
      ##  print(x)

for i in range(0,n):
    a,b= map(int,input().split())
    find(a,b)
'''
n= int(input())
def find(a,b):
    while a!=b:
        if a>b:
            a//=2
        else:
            b//=2
    print(a*10)
for _ in range(n):
    a,b=map(int,input().split())
    find(a,b)


        

    





