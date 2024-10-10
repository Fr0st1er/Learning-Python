A = int(input("What's x? "))
B = ""
while A > 0:
    B = str(A%2) + B
    A = A//2
print(B)