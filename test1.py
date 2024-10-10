A = input("What's string? ")
B = ""
i = 0
while i < len(A):
    C = ""
    while A[i].isdigit():
        C += A[i]
        i += 1
    number = int(C)
    char = A[i]
    B += char * number
    i += 1
print(B)
