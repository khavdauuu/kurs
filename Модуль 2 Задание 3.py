start = 1
end = 10
step = 2

seq = range(start, end, step)
result = map(lambda x: x ** 2 if x % 2 != 0 else -x, seq)

for res in result:
    print(res)