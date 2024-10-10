A = input("What's string? ")
B = ""
for i in range(0, len(A), 2):
    number = int(A[i])
    char = A[i+1]
    B += char * number
print(B)