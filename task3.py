check_dict = {'(': ')', '[': ']', '{': '}'}


def check_code(code: str) -> bool:
    stack = []
    for c in code:
        if c in '([{':
            stack.append(c)
        elif c in ')]}':
            top = stack.pop()
            if check_dict[top] != c:
                return False
    if len(stack) == 0:
        return True
    else:
        return False


print(check_code('( ){[ 1 ]( 1 + 3 )( ){ }}'))
