#coding: utf-8
s = input()
c1 = len(s)
s = s.replace('!', '')
s = s.replace('@', '')
s = s.replace('#', '')
s = s.replace('%', '')
print(c1 - len(s))
print(s.lower())
