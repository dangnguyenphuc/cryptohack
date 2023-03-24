#!/usr/local/bin/python3
import numpy as np
from PIL import Image, ImageChops

# # Open images
# im1 = Image.open("course1/image/flag.png", mode = "1")
# im2 = Image.open("course1/image/lemur.png", mode = "1")

# result = ImageChops.logical_xor(im1,im2)
# result.save('image/result.png')

im1 = Image.open("course1/image/flag.png")
im2 = Image.open("course1/image/lemur.png")

# Make into Numpy arrays
im1np = np.array(im1)*255
im2np = np.array(im2)*255

# XOR with Numpy
result = np.bitwise_xor(im1np, im2np).astype(np.uint8)

# Convert back to PIL image and save
Image.fromarray(result).save('result.png')