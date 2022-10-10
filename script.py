# Pyhton Image Library 
#Pyhton Image Library
from PIL import Image
#Library to read files in a folder
import glob

images = glob.glob('images/*.jpg')
i = 0
for image in images:
    im = Image.open(image).rotate(90).save('newImages/starwars'+ str(i) +'.jpg')
    i+=1