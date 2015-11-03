import re

rule_regex = re.compile(r'#include (?:"|<)([^">]+)', re.IGNORECASE | re.DOTALL)

for file_name in vera.getSourceFileNames():
	for lineNumber, line in enumerate(vera.getAllLines(file_name)):
		matcher = rule_regex.search(line)
		if matcher is not None and matcher.group(1).find(':') != -1:
			vera.report(file_name, lineNumber + 1, "Error 4.3.d")
