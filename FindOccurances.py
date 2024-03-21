from  collections import Counter
s=input()

# for i in range(len(s)):
#     if s[i] in l:
#         l[s[i]]+=1
#     else:
#         l[s[i]]=1
#
# print(l)
print(dict(Counter(s)))