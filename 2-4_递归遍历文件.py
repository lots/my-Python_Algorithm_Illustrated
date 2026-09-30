import os

def displayFile(path):
	for each in os.listdir(path):
		absolute_path = os.path.join(path,each)
		is_file = os.path.isfile(absolute_path)
		if is_file:
			print(each)
		else:
			print('----------------',each,'----------------------')
			displayFile(absolute_path)
			print('----------------------------------------------')

displayFile('e:/www/angular')