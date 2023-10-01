a = int(input("請輸入三角形的最短邊:"))
b = int(input("請輸入三角形的最長邊:"))
c = int(input("請輸入第三邊:"))

if a+b > c and a*a+b*b < c*c:
    print("三線段構成鈍角三角形")
elif a+b > c and a*a+b*b == c*c:
    print("三線段構成直角三角形")
elif a+b > c and a*a+b*b > c*c:
    print("三線段構成銳角三角形")
else:
    print("三線段無法構成三角形")
