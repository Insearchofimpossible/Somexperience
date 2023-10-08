import time
st = time.time()
n = 3*10**5
k = 23
a = [x for x in range(1, n + 1)]
temp = 0
while len(a) > 1:
    temp = (temp + k - 1) % len(a)
    a.pop(temp)
print(a)
end = time.time()
print(end - st)
