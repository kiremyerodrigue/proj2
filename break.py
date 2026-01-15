num = int(input("Enter the number you want the multiplication table for: "))

for i in range(1, 11):
    if i == 7:
        break
    print(num, "x", i, "=", num * i)
