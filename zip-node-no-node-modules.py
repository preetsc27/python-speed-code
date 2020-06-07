from zipfile import ZipFile
import os

file_count = 0

def get_file_paths(path):
	global file_count
	all_paths = []
	file_exceptions = ["node_modules"]
	for f in os.listdir(path):
		if f in file_exceptions:
			continue
		full_path = os.path.join(path, f)
		if os.path.isdir(full_path):
			more_paths = get_file_paths(full_path)
			all_paths += more_paths
		else:
			file_count += 1
			all_paths.append(full_path)
	return all_paths

def zip_files(paths):
	with ZipFile('the_zip.zip', 'w') as zip:
		for p in paths:
			zip.write(p)

	print("Done Zipping")

dir_path = "."
file_paths = get_file_paths(dir_path)
print(file_count)
zip_files(file_paths)
