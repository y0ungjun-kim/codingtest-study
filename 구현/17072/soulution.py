n,m = map(int,input().split())
array=[]## n개의 줄을 입력 받아서 각 줄에 array를 넣고 싶은 것이다.

def intensity(r,g,b):
    return 2126*r+7152*g+722*b
for i in range(n):
      row =list(map(int,input().split()))
      array.append(row)

for x in array: 
    for j in range(m):
        red=x[3*j]
        green=x[3*j+1]
        blue=x[3*j+2]
        temp=intensity(red,green,blue)
        if temp < 510000:
            print("#", end="")
        elif temp < 1020000:
            print("o", end="")
        elif temp < 1530000:
            print("+", end="")
        elif temp < 2040000:
            print("-", end="")
        else:
            print(".", end="")
    print()
