d = {'1': 'one',
     '2': 'Two',
     '3': 'three',
     '4': 'four',
     '5': 'five',
     '6': 'six',
     '7': 'seven',
     '8': 'eight',
     '9': 'nine',
     '0': 'zero'
     }

num = input()
vowel = input()
vowel = vowel.lower()
l = ""
for c in num:
    if vowel in d.get(c):
        l += c

print(l)