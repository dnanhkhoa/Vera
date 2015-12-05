import re

commentRE = re.compile(r'\/\/[^\n]*|\/\*((?!\*\/).)+\*\/', re.IGNORECASE | re.DOTALL)
stringRE = re.compile(r'\"[^"]*\"', re.IGNORECASE | re.DOTALL)
ruleRE = re.compile(r'(\d+)\.\s*#ifndef (\w+)\s*\n(\d+)\.\s*#define \2\s*\n', re.IGNORECASE | re.DOTALL)

for fileName in vera.getSourceFileNames():
	lineNum = 1
	source = ''
	
	for line in vera.getAllLines(fileName):
		source += '%d.%s\n' % (lineNum, line)
		lineNum += 1
		
	#remove comment
	source = commentRE.sub('', source)
	
	#remove stringRE
	source = stringRE.sub('', source)
	
	#check rule 4_2_b
	matcher = ruleRE.search(source)
	if matcher is None:
		vera.report(fileName, int(1), "Error 4_2_b")