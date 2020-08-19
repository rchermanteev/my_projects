import sys
s = sys.stdin.readlines()
arr = [float(st.split(' ')[-1].replace('\n', '')) for st in s]
mean = round(sum(arr)/len(arr), 2)
count = 0
m1 = mean+(mean/100)*10
m2 = mean-(mean/100)*10
for item in arr:
    if (item >= m1) or (item <= m2):
        count += 1

print(count)
