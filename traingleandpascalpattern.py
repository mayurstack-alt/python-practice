
rows = int(input("Enter rows: "))
print("\nAlphabet Triangle Pattern:")
ch = 65   # ASCII value of 'A'
for i in range(1, rows + 1):
    for j in range(i):
        print(chr(ch), end=" ")
        ch += 1
    print()

print("\nPascal's Triangle Pattern:")

for i in range(rows):
    num = 1
    for j in range(i + 1):
        print(num, end=" ")
        num = num * (i - j) // (j + 1)
    print()