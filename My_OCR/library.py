from PIL import Image


im_file = "D:\Personal Projects\My_OCR\data\page_01.jpg"

im = Image.open(im_file)
im2 = im.rotate(180)
im2.save("D:/Personal Projects/My_OCR/data/page_01_rotated.jpg")