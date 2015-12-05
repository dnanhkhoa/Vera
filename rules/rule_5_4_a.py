import re

commentRE = re.compile(r'\/\/[^\n]*|\/\*((?!\*\/).)+\*\/', re.IGNORECASE | re.DOTALL)
stringRE = re.compile(r'\"[^"]*\"', re.IGNORECASE | re.DOTALL)
ruleRE01 = re.compile(r'(\d+)\.\s*(\w+\s+|\s*)(float|double)\s+', re.IGNORECASE | re.DOTALL)
ruleRE02 = re.compile(r'(\d+)\.\s*(.+)=\s*\d+\.\d+\s*;', re.IGNORECASE | re.DOTALL)

for fileName in vera.getSourceFileNames():
	source = ''
	lineNum = 1
	
	for line in vera.getAllLines(fileName):
		source += '%d.%s\n' % (lineNum, line)
		lineNum += 1
		
	#remove comment
	source = commentRE.sub('', source)
	
	#remove string
	source = stringRE.sub('', source)
	
	#rule 5_4_a
	lines = source.splitlines()
	for line in lines:
		matcher01 = ruleRE01.search(line)
		matcher02 = ruleRE02.search(line)
		
		flag = False
		
		if (matcher01 is not None):
			vera.report(fileName, int(matcher01.group(1)), "Error 5_4_a")
			flag = True
			
		if (matcher02 is not None) and (flag == False):
			vera.report(fileName, int(matcher02.group(1)), "Error 5_4_a")