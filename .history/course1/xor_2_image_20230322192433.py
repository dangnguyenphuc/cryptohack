#!/usr/local/bin/python3
import numpy as np
from PIL import Image, ImageChops

# Open images
im1 = Image.open("im1.png")
im2 = Image.open("im2.png")

result = ImageChops.logical_xor(im1,im2)
result.save('result.png')ßß