import re

pattern = re.compile(r'\bcontinue;')
for filename in vera.getSourceFileNames():
	file = open(filename, 'rb')
	lineCounter = 1
	lines = file.readlines()
	
	for line in lines:
		matcher = pattern.search(line)
		
		if matcher is not None:
			vera.report(filename, lineCounter, ': Error 1_7_b')

		lineCounter = lineCounter + 1

	file.close()