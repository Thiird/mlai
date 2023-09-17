import os
import csv
from PIL import Image
import numpy as np

label_keys = {}

# Percorso della cartella contenente le immagini
image_folder_path = 'C:\\F_drive\\Ste\\UNIVERSITÀ\\Magistrale\\ML&AI\\images\\selected_datasets\\Training'
folders = sorted(os.listdir(image_folder_path))

# Percorso del file CSV da creare
csv_file_path = 'C:\\F_drive\\Ste\\UNIVERSITÀ\\Magistrale\\ML&AI\\images\\selected_datasets\\dataset.csv'

# Make labels
cont = 0
for label in folders:
    label_keys[label] = cont
    cont += 1

# Build csv fields string
fields = ["label"]

for x in range(70*70):
    for y in ["R","G","B"]:
        fields.append(str(x) + "_" + y)

# Write File
with open(csv_file_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(fields)

    # For each label folder
    for index, folder in enumerate(folders):
        print( folder + " =======================")
        currentFolderPath = os.path.join(image_folder_path, folder)
        if(os.path.isdir(currentFolderPath)):
            # For each file
            for file in os.listdir(currentFolderPath):
                currentFilePath = os.path.join(currentFolderPath, file)

                # Apri l'immagine e convertila in scala di grigi
                image = Image.open(currentFilePath)

                # Converti l'immagine in un array NumPy
                image_array = np.array(image)

                # Appiattisci l'array dell'immagine in un vettore 1D
                image_vector = image_array.flatten()

                # Crea una riga di dati contenente un intero seguito dai valori dei pixel dell'immagine
                row = [label_keys[folder]] + list(image_vector)

                # Scrivi la riga nel file CSV
                csv_writer.writerow(row)

