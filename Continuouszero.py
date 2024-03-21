s=input()
m=0

for i in range(len(s)):
    temp = 0
    while i<len(s) and s[i] == '0':
        temp += 1
        i += 1
    m=max(temp, m)
print(m)


