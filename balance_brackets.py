from stack import Stack


def str_in_stack(str_=str()):
    stack = Stack()
    for elem in str_:
        stack.push(elem)
    return stack


def stack_in_inverted_str(stack=Stack()):
    str_ = ""
    while not stack.is_empty():
        elem = stack.pop()
        if elem == ")":
            str_ += "("
        if elem == "(":
            str_ += ")"
        if elem == "[":
            str_ += "]"
        if elem == "]":
            str_ += "["
        if elem == "{":
            str_ += "}"
        if elem == "}":
            str_ += "{"
    return str_


def balance_brackets(brackets=str()):
    brackets_stack = str_in_stack(brackets)
    brackets_inverted = stack_in_inverted_str(brackets_stack)
    if brackets == brackets_inverted:
        print("Сбалансировано")
    else:
        print("Несбалансированно")
