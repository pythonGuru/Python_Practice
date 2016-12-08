
def check_paranthesis(str):

    l = []

    for item in str:

        if item == "(":
            l.append(item)
        elif item == ")":
            l.pop()
        else:
            continue

    if len(l) != 0:
        return False
    else:
        return True

print check_paranthesis("It was (easy) if it was really (easy)")
