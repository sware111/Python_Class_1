a = int(input())
b = int(input())
c = int(input())

if a < 0 or b < 0 or c < 0:
    print("invalid Number")
elif a> 0 or b> 0 or c > 0:
    if a==b==c:
        print("flamn")
    elif a+b==c or a+c==b or c+b==a:
        print("ggg")
    else:
        print("ok")