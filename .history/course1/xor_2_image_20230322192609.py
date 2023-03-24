#!/usr/local/bin/python3
import numpy as np
from PIL import Image, ImageChops

# Open images
im1 = Image.open("image/flag.png")
im2 = Image.open("image/lemur.png")

result = ImageChops.logical_xor(im1,im2)
result.save('image/result.png')