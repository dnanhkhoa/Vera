def is_decrease(list):
    if len(list) == 0:
        return True

    old = list[0]
    for i in xrange(1, len(list)):
        if list[i] > old:
            return False
        else:
            old = list[i]
    return True

tokenTypes = ["if", "else", "leftbrace", "rightbrace"]

for file_name in vera.getSourceFileNames():
    stack = []
    statement = None
    tab_count = 0
    old_type = None
    for token in vera.getTokens(file_name, 1, 0, -1, -1, tokenTypes):
        if token.type == 'if' and old_type == 'else': # else if
            statement = ('else if', token.line, tab_count)
        elif token.type == 'if': # if
            statement = ('if', token.line, tab_count)
        elif token.type == 'else':
            statement = ('else', token.line, tab_count)
        else:
            if token.type == 'leftbrace':
                if old_type == 'else':
                    if statement is not None:
                        stack.append(statement)
                        statement = None

                tab_count += 1
                if statement is not None:
                    stack.append(statement)
                    statement = None

                if len(stack) > 0:
                    statement_tmp = stack[len(stack) - 1]
                    if statement_tmp[2] == tab_count - 1:
                        stack.append(('{', token.line, tab_count - 1))
            elif token.type == 'rightbrace':
                tab_count -= 1
                if len(stack) > 0:
                    statement_tmp = stack[len(stack) - 1]
                    if statement_tmp[2] == tab_count:
                        stack.append(('}', token.line, tab_count))
        old_type = token.type

    num_lines = []
    while len(stack) > 0:
        statement_tmp = stack[len(stack) - 1]
        stack.pop()

        if statement_tmp[0] == 'if':
            if is_decrease(num_lines) == False:
                vera.report(file_name, statement_tmp[1], "Error 8.2.a")
            num_lines = []

        if statement_tmp[0] == '}':
            left_brace = stack[len(stack) - 1]
            stack.pop()
            num_lines.append(statement_tmp[1] - left_brace[1] - 1)
