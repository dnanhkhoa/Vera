import re

commentRE = re.compile(r'\/\/[^\n]*|\/\*((?!\*\/).)+\*\/', re.IGNORECASE | re.DOTALL)
stringRE = re.compile(r'\"[^"]*\"', re.IGNORECASE | re.DOTALL)
#declare and assign
ruleRE01 = re.compile(r'(\d+)\.\s*(\w+\s+|\s*)float\s+(\w+)\s*=\s*\d+(\.\d+|)\s*;', re.IGNORECASE | re.DOTALL)
#assign after declared
ruleRE02 = re.compile(r'(\d+)\.\s*(\w+\s+|\s*)float\s+(\w+)\s*;(.*)(\d+)\.\s*\3\s*=\s*\d+(\.\d+|)\s*;', re.DOTALL)
#replace pattern

for fileName in vera.getSourceFileNames():
	source = ''
	lineNum = 1;
	
	for line in vera.getAllLines(fileName):
		source += '%d.%s\n' % (lineNum, line)
		lineNum += 1
		
	#remove comment
	source  = commentRE.sub('', source)
	
	#remove string
	source = stringRE.sub('', source)
	
	#rule
	matcher01 = ruleRE01.findall(source)
	matcher02 = ruleRE02.findall(source)
	
	if matcher01 is not None:		
		for i in matcher01:
			vera.report(fileName, int(i[0]), "Error 5_4_b2")
	
	if matcher02 is not None:
		for i in matcher02:
			vera.report(fileName, int(i[4]), "Error 5_4_b2")