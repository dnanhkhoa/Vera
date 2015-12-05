tokenTypes = ["for", "if", "while", "else", "semicolon"]

for file_name in vera.getSourceFileNames():
    map = [0] * vera.getLineCount(file_name)
    old_type = None
    old_column = None
    for token in vera.getTokens(file_name, 1, 0, -1, -1, tokenTypes):
        if old_type is not None and old_column is not None:
            if old_type == 'else' and token.type == 'if' and (token.column - old_column) == 5:
                map[token.line - 1] -= 1

        map[token.line - 1] += 1
        old_type = token.type
        old_column = token.column

    for i in xrange(len(map)):
        if map[i] >= 2:
            vera.report(file_name, i + 1, "Error 3.3.a")
