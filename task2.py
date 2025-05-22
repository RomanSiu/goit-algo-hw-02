from collections import deque


def check_str(pal: str) -> bool:
    pal = pal.replace(" ", "").lower()
    d = deque()
    d.extend(list(pal))
    while d:
        if len(d) == 1:
            return True
        first = d.popleft()
        last = d.pop()
        if first != last:
            return False
    return True


print(check_str('abc BA'))
