import csv
from PIL import Image as im
import numpy as np
import matplotlib.pyplot as plt

# Percorso del file CSV da creare
csv_file_path = 'C:\\F_drive\\Ste\\UNIVERSITÀ\\Magistrale\\ML&AI\\images\\selected_datasets\\dataset.csv'

with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    # Leggi la prima riga del file CSV (che contiene i dati dell'immagine)
    row = next(csv_reader)

    # Estrai i valori dei pixel dall'array di stringhe
    pixel_values = [int(value) for value in row[1:]]

    # Crea un array NumPy dai valori dei pixel
    image_array = np.array(pixel_values)

    # Ridimensiona l'array dell'immagine alle dimensioni originali dell'immagine
    image_array = image_array.reshape(( 70, 70, 3))

    # Visualizza l'immagine utilizzando matplotlib
    plt.imshow(image_array)
    plt.show()
