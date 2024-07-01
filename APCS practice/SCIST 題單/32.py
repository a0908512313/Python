a = int(input())
if a>=90:
    print("expert")
elif a < 90 and a >= 70:
    print(abs(90-a))
elif a < 70 and a >= 40:
    print(abs(70-a))
else:
    print(abs(40-a))
