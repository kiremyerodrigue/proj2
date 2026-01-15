num = int(input("Enter the number you want the multiplication table for: "))

for i in range(1, 11):
    if i == 5:
        continue
    print(num, "x", i, "=", num * i)
