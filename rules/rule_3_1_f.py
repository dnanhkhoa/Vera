import re

comment_regex = re.compile(r'\/\/[^\n]*|\/\*((?!\*\/).)+\*\/', re.IGNORECASE | re.DOTALL)
string_regex = re.compile(r'\"[^"]*\"', re.IGNORECASE | re.DOTALL)
rule_regex = re.compile(r'(\s*)\?(\s*)[^:?]+?(\s*):(\s*)', re.IGNORECASE | re.DOTALL)
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

    # Check rule 3.1.f
    lines = source_code.splitlines()
    for line in lines:
        matcher = rule_regex.search(line)
        while matcher is not None:
            if len(matcher.group(1)) + len(matcher.group(2)) + len(matcher.group(3)) + len(matcher.group(4)) != 4:
                # Extract line number
                line_number = line_number_regex.search(line)
                if line_number is not None:
                    vera.report(file_name, int(line_number.group(1)), "Error 3.1.f")
                break

            line = rule_regex.sub('', line)
            matcher = rule_regex.search(line)
