#sum of 1 to 100
print("****For Loop****")
s = 0
for i in range(1, 100):
    s += i
print(s)

print("****While Loop****")
i = 1
s = 0
while i < 100:
    s += i
    i += 1
print(s)