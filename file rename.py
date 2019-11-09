from os import path, listdir, rename

filePath = 'C:\\some\\file\\path'

files = listdir(path.join(filePath))
renamedFiles = []

for names in files:
    tempString = names.replace(').', '.')
    renamedFiles.append(tempString)

for i in range(len(files)):
    rename(path.join(filePath, files[i]), path.join(filePath, renamedFiles[i]))
