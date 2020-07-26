Hello World
list1 = []
list2 = []

N = int(input())

for i in range(0, N):
    num = int(input())
    list1.append(num)

def count(num):
    b = d = num
    count = 1

    while num != 0:
        num //= 10
        count += 1

    if count > 2:
        a = 0
        while a <= 1:
            d = d / 10
            a = a + 1

        d = int(d)

        c = b - d * 100
        list2.append(c)
    else:
        list2.append(b)


def digits(n):
    largest = 0
    smallest = 9

    while (n):
        r = n % 10

        smallest = min(r, smallest)
        largest = max(r, largest)

        n = n // 10

    bit = smallest * 7 + largest * 11
    count(bit)

for j in list1:
    digits(j)

pair = 0
count = 0

for k in range(0, len(list2) - 1):
    l = 2

    while k + l < len(list2):
        if list2[k] == list2[k + l]:
            pair += 1
        elif int((list2[k]) / 10) == int((list2[k + l]) / 10):
            count += 1
        l += 2

if count > 2:
    pair = pair + 2
elif count == 0:
    pair = pair + 0
else:
    pair = pair + 1
print(pair)



