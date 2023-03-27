#!/usr/local/bin/python3
import numpy as np
from PIL import Image, ImageChops

# Open images
im1 = Image.open("course1/image/flag.png", mode = "rw")
im2 = Image.open("course1/image/lemur.png", mode = "rw")

result = ImageChops.logical_xor(im1,im2)
result.save('image/result.png')