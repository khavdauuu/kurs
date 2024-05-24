from collections import defaultdict
from typing import List, Tuple

def fill_specializations(specializations: List[Tuple[str, str]]):
    # YOUR CODE HERE
    result = defaultdict(list)
    for specialization, name in specializations:
        result[specialization].append(name)
    return dict(result)

code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)