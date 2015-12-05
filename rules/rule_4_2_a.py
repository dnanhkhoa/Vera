import re
import os

comment_regex = re.compile(r'\/\/[^\n]*|\/\*((?!\*\/).)+\*\/', re.IGNORECASE | re.DOTALL)
string_regex = re.compile(r'^(?:(?!#include\s*).)*?\"[^"]*\"', re.IGNORECASE | re.DOTALL)

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

    # Header file
    header_file = '%s.h' % os.path.splitext(file_name)[0]
    if not os.path.isfile(header_file):
        vera.report(file_name, 1, "Error 4.2.a: Missing header file: %s" % header_file)

    regex_rule_string = '#include (?:\"|<)%s(?:\"|>)' % header_file
    num_count = 0

    # Check rule 4.2.a
    lines = source_code.splitlines()
    for line in lines:
        matcher = re.search(regex_rule_string, line, re.IGNORECASE | re.DOTALL)
        if matcher is not None:
            num_count += 1

    if num_count != 1:
        vera.report(file_name, 1, "Error 4.2.a: #include <%s> is invalid" % header_file)
