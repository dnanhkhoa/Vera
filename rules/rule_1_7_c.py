import re

pattern = re.compile(r'\bgoto\b')
for filename in vera.getSourceFileNames():
	file = open(filename, 'rb')
	lineCounter = 1
	lines = file.readlines()
	
	for line in lines:
		matcher = pattern.search(line)
		
		if matcher is not None:
			vera.report(filename, lineCounter, ': Error 1_7_c')

		lineCounter = lineCounter + 1

	file.close()