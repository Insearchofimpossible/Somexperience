import time
st = time.time()
n,k,temp = 3*10**5,23,0
a = [x for x in range(1, n + 1)]
while len(a) > 1:
    temp = (temp + k - 1) % len(a)
    a.pop(temp)
print(a)
print(time.time() - st)
