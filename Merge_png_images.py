#This program is used to merge two different .png . Start the program, it will open a dialogue box, you'll need to select a first image.
#After that, it will open a second dialogue box, select the second image. The second image is the foreground. This one will appear first.
#To finish, it will open a last dialogue box. This one asks you where do you want to save the result.
#Finaly, this will open your photos and show the result. 
#BEWARE, THIS PROGRAM ONLY ACCEPT .PNG. EVERY TIME YOU RUN IT, THERE WILL BE A NEW SAVE IF YOU DON'T NAME THE NEW IMAGES SAME AS OLDER IMAGES. 

from PIL import Image
from tkinter.filedialog import askopenfilename, asksaveasfile

#this function paste on image on an other by verifying the pixels RGBA values
def merge_images(image1, image2):
    image1_width, image1_height = image1.size
    image2_width, image2_height = image2.size

    image_merge = Image.new('RGBA', (max(image1_width, image2_width), max(image1_height, image2_height)))

    for x in range(image1_width):
        for y in range(image1_height):
            pixel = image1.getpixel((x, y))
            image_merge.putpixel((x, y), pixel)

    for x in range(image2_width):
        for y in range(image2_height):
            pixel = image2.getpixel((x, y))
            if pixel[3] != 0:
                image_merge.putpixel((x, y), pixel)

    return image_merge

#this function takes a background image, paste it to a foreground image and remove all red in the pixels
def imgin(background_path, foreground_path, save_path):
    background = Image.open(background_path)
    foreground = Image.open(foreground_path)

    # if background size is different than foreground size, stop
    if (background.size!=foreground.size):
        print("Error : The two images need to have the same size.")
        return 1
    
# ask the path to access to the images and where to save the result
foreground_path = askopenfilename(filetypes=[('PNG files','.png')])
background_path = askopenfilename(filetypes=[('PNG files','.png')])
save_path = asksaveasfile(defaultextension=".png")

#merge the two images
image1 = Image.open(foreground_path)
image2 = Image.open(background_path)

image_merge = merge_images(image1, image2)

#save the result
image_merge.save(save_path.name)

#show the result
image_merge = Image.open(save_path.name)
image_merge.show()