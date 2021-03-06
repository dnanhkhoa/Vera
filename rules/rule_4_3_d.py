import re

comment_regex = re.compile(r'\/\/[^\n]*|\/\*((?!\*\/).)+\*\/', re.IGNORECASE | re.DOTALL)
string_regex = re.compile(r'^(?:(?!#include\s*).)*?\"[^"]*\"', re.IGNORECASE | re.DOTALL)
rule_regex = re.compile(r'#include (?:"|<)([^">]+)', re.IGNORECASE | re.DOTALL)
line_number_regex = re.compile(r'^(\d+)@', re.IGNORECASE | re.DOTALL)

for file_name in vera.getSourceFileNames():
    line_number = 1
    source_code = ''
    for line in vera.getAllLines(file_name):
        source_code += '%d@%s\n' % (line_number, line)
        line_number += 1

    # Remove comments
    source_code = comment_regex.sub('', source_code)

    # Remove strings
    source_code = string_regex.sub('', source_code)

    # Check rule 4.3.d
    lines = source_code.splitlines()
    for line in lines:
        matcher = rule_regex.search(line)
        if matcher is not None and matcher.group(1).find(':') != -1:
            # Extract line number
            line_number = line_number_regex.search(line)
            if line_number is not None:
                vera.report(file_name, int(line_number.group(1)), "Error 4.3.d")
