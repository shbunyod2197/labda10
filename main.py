# 1
res = lambda a: a if a > 0 else 0
print(res(-1))

# 2
res = lambda a: a % 2 == 0
print(res(4))

# 3
res = lambda a, b: a if a > b else b
print(res(5,8))

# 4
res = lambda a: "musbat" if a > 0 else "Manfiy"
print(res(-1))

# 5
res = lambda a: a * 2  if a > 10 else a
print(res(11))

# 6
res = lambda a: a * 2 if a % 2 == 0 else a * 3
print(res(5))

# 7
res = lambda a, b: a if a > b else b
print(res(9,8))

# 8
res = lambda a: "OK" if a % 5 == 0 else "NO"
print(res(19))

# 9
res = lambda a: 100 if  a > 100 else a
print(res(101))

# 10
res = lambda son: -son if son < 0 else son
print(res(-9))
