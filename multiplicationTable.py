#!/usr/bin/env python3

x = 1

print("*" * 50)

while x < 11:
    y = 1
    while y <= 10:
        print("%4d" % (y * x), end=" ")
        y += 1
    print()
    x += 1
print("*" * 50)


# i = 1
# print("-" * 50)
# while i < 11:
#     n = 1
#     while n <= 10:
#         print("%4d" % (i * n), end=' ')
#         n += 1
#     print()
#     i += 1
# print("-" * 50)
