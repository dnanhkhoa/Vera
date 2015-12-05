tokenTypes = ["if", "else", "leftbrace", "rightbrace"]

for file_name in vera.getSourceFileNames():
    stack = []
    statement = None
    tab_count = 0
    old_type = None
    for token in vera.getTokens(file_name, 1, 0, -1, -1, tokenTypes):
        if token.type == 'if' and old_type == 'else':
            statement = ('else if', token.line, tab_count)
        elif token.type == 'if':
            if len(stack) > 0:
                has_elif = False
                statement_tmp = stack[len(stack) - 1]
                if statement_tmp[2] == tab_count:
                    if statement_tmp[0] == 'else if':
                        has_elif = True
                    while statement_tmp[0] != 'if':
                        stack.pop()
                        statement_tmp = stack[len(stack) - 1]
                    stack.pop()
                    if has_elif:
                        vera.report(file_name, statement_tmp[1], "Error 8.2.d")

            statement = ('if', token.line, tab_count)
        else:
            if token.type == 'leftbrace':
                tab_count += 1
                if old_type == 'else':
                    statement_tmp = stack[len(stack) - 1]
                    if statement_tmp[2] == tab_count - 1:
                        while statement_tmp[0] != 'if':
                            stack.pop()
                            statement_tmp = stack[len(stack) - 1]
                        stack.pop()
                if statement is not None:
                    stack.append(statement)
                    statement = None
            elif token.type == 'rightbrace':
                tab_count -= 1
        old_type = token.type
    while len(stack) > 0:
        statement_tmp = stack[len(stack) - 1]
        while statement_tmp[0] != 'if':
            stack.pop()
            statement_tmp = stack[len(stack) - 1]
        stack.pop()
        vera.report(file_name, statement_tmp[1], "Error 8.2.d")
    print stack
