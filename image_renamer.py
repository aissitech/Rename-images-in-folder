import os 

source_folder = r'C:\Users\name_of_user\path_to_folder'

for item in os.listdir(source_folder):
	if os.path.isfile(os.path.join(source_folder, item)):
		if item.endswith('.jpeg'):
			try:
				os.rename(
					os.path.join(source_folder, item),
					os.path.join(source_folder, 'name_your_file'+ item)
					)
				
			except PermissionError:
				continue
			except Exception as e:
				raise Exception(e)
