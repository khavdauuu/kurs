from collections import deque
from typing import List

def rotate_list(nums: List[int], n: int):
    # YOUR CODE HERE
    nums_deque = deque(nums)
    nums_deque.rotate(-n)
    result = list(nums_deque)
    return result

code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)