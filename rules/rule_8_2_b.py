tokenTypes = ["if", "else", "leftbrace", "rightbrace"]

for file_name in vera.getSourceFileNames():
    tab_count = 0
    old_type = None
    for token in vera.getTokens(file_name, 1, 0, -1, -1, tokenTypes):
        if token.type == 'if':
            if old_type != 'else' and tab_count >= 2:
                    vera.report(file_name, token.line, "Error 8.2.b")
        else:
            if token.type == 'leftbrace':
                tab_count += 1
            elif token.type == 'rightbrace':
                tab_count -= 1
        old_type = token.type
