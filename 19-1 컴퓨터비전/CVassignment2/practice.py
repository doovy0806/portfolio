n = int(input())
alist = input()
alist = alist.split()
numlist = []
plist = {}
for i in alist:
    numlist.append(int(i))
for i in range(len(numlist)):
    for j in range(i, len(numlist)):
        if i == j:
            plist[(i, j)] = numlist[i]
        else:
            cur_p = 1
            for k in range(i, j + 1):
                cur_p *= numlist[k]
            plist[(i, j)] = cur_p
maxp = 0
for a in range(n - 2):
    if a is 0:
        pa = plist[(0, 0)]
    else:
        pa = plist[(0, a - 1)]
    for b in range(a+1, n - 1):
        if b is a + 1:
            pb = plist[(a, a)]
        else:
            pb = plist[(a, b - 1)]
        for c in range(b+1, n):
            if c is b + 1:
                pc = plist[(b, b)]
            else:
                pc = plist[(b, c - 1)]

            pd = plist[(c,n-1)]
            maxp = max(pa + pb + pc+pd, maxp)
print(maxp)

