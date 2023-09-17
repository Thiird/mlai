import os
import imageio.v3 as iio
from skimage.transform import resize
from skimage.color import rgba2rgb
from skimage import util

path = 'C:\\F_drive\\Ste\\UNIVERSITÀ\\Magistrale\\ML&AI\\images\\selected_datasets\\Training'
files = os.listdir(path)

HEIGHT = 70
WIDTH = 70

# For each label folder
for index, folder in enumerate(files):
    print( folder + " =======================")
    currentFolderPath = os.path.join(path, folder)
    if(os.path.isdir(currentFolderPath)):
        # For each file
        for file in os.listdir(currentFolderPath):
            print(file)
            currentFilePath = os.path.join(currentFolderPath, file)
            
            # read in image
            img = iio.imread(uri=currentFilePath)

            if(img.shape[2]) == 4:
                img = rgba2rgb(img)

            # resize the image
            new_shape = (HEIGHT, WIDTH, img.shape[2])
            resized = resize(image = img, output_shape=new_shape)
            resized = util.img_as_ubyte(resized)

            os.remove(currentFilePath)

            # write out image
            iio.imwrite(uri=currentFilePath, image=resized)
