for file_name in vera.getSourceFileNames():
    for token in vera.getTokens(file_name, 1, 0, -1, -1, ['goto']):
        vera.report(file_name, token.line, "Error 1.7.c")
