import re

commentRE = re.compile(r'\/\/[^\n]*|\/\*((?!\*\/).)+\*\/', re.IGNORECASE | re.DOTALL)
stringRE = re.compile(r'\"[^"]*\"', re.IGNORECASE | re.DOTALL)
mainFunctionRE = re.compile(r'(\w+)\s+(main)\s*\(\)', re.IGNORECASE | re.DOTALL)
ruleRE = re.compile(r'(\d+)\.\s*(.+)\s+(?!(g_)).*;', re.IGNORECASE | re.DOTALL)

for fileName in vera.getSourceFileNames():
	source = ''
	lineNum = 1;
	
	for line in vera.getAllLines(fileName):
		source += '%d.%s\n' % (lineNum, line)
		lineNum += 1
		
	#remove comment
	source = commentRE.sub('', source)
	
	#remove string
	source = stringRE.sub('', source)
	
	lines = source.splitlines()
	
	for i in lines:
		main = mainFunctionRE.search(i)
		if main is not None:
			#vera.report(fileName, int(1), "main")
			break;
	
		matcher = ruleRE.search(i)
		if matcher is not None:
			vera.report(fileName, int(matcher.group(1)), "Error_7_1_j")