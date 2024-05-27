from collections import deque
from typing import List


def rotate_list(nums: List[int], n: int):
    queue = deque(nums)
    n = n % len(queue)  # Если n больше длины списка, берем остаток от деления
    for _ in range(n):
        queue.appendleft(queue.pop())
    return list(queue)


code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)
