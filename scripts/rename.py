import os
path = 'C:\\F_drive\\Ste\\UNIVERSITÀ\\Magistrale\\ML&AI\\images\\selected_datasets'
files = os.listdir(path)
cont = 0

# For each label folder
for index, folder in enumerate(files):
    currentFolderPath = os.path.join(path, folder)
    if(os.path.isdir(currentFolderPath)):
        cont = 0
        # For each file
        for file in os.listdir(currentFolderPath):
            currentFilePath = os.path.join(currentFolderPath, file)            
            newFilePath = os.path.join(currentFolderPath, folder + "_" + str(cont) + ".jpg")
            os.rename(currentFilePath, newFilePath)
            cont += 1