import os 

source_folder = r'C:\Users\MSI\Desktop\folder'

for item in os.listdir(source_folder):
	if os.path.isfile(os.path.join(source_folder, item)):
		if item.endswith('.jpeg'):
			try:

				os.rename(
					os.path.join(source_folder, item),
					os.path.join(source_folder, 'FACTURE_'+ item)
					)
				
			except PermissionError:
				continue
			except Exception as e:
				raise Exception(e)