import sys
s = sys.stdin.readline()
s = s.split(' ')
s = [si.replace('\n', '') for si in s]

s[0] = int(s[0])
s[2] = (s[2])[6:]


if s[0]<30:
    day = 42302
elif s[0]>30 and s[0]<90:
    day = 42303
elif s[0]>90 and s[0]<180:
    day = 42304
elif s[0]>180 and s[0]<365:
    day = 42305
elif s[0]>365 and s[0]<365*3:
    day = 42306
elif s[0]>365*3:
    day = 42307
day = str(day)
if s[1] == 'USD':
    val = 840
elif s[1] == 'RUR':
    val = 810
elif s[1] == 'EUR':
    val = 978
elif s[1] == 'GBP':
    val = 826

val = str(val)
kod = s[2]


kod_d= kod+day+val+'0'*5+s[3]
kod_d = list(kod_d)
valid_kod = '71371371371371371371371'
valid_kod = list(valid_kod)


kod_d = [int(i) for i in kod_d]
valid_kod = [int(i) for i in valid_kod]


arr = []
for i in range(len(valid_kod)):
    arr.append(valid_kod[i]*kod_d[i])

arr = [(a % 10) for a in arr]
avg = sum(arr)
new_kod = str((avg%10*3)%10)

ans = day+val+new_kod+'0'*4+s[3]
print(ans)
