def is_balanced(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for ch in s:
        if ch in "({[":
            stack.append(ch)
        elif ch in ")}]":
            if not stack or stack[-1] != pairs[ch]:
                return "Not Balanced"
            stack.pop()
    if len(stack) == 0:
        return "Balanced"
    else:
        return "Not Balanced"
    
s = input("Enter bracket string: ")

print(is_balanced(s))