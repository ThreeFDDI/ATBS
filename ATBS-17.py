#!/usr/local/bin/python3

# Chapter 17 – Manipulating Images

# ATBS-17.py 

from PIL import ImageColor, Image

print(ImageColor.getcolor('red', 'RGBA'))

catIm = Image.open('ATBS/ATBS-17_zophie.png')

print()
print(catIm)
print(type(catIm))
print(catIm.size)
print(catIm.width)
print(catIm.height)
print(catIm.filename)
print(catIm.format)
print(catIm.format_description)
catIm.save('ATBS/ATBS-17_zophie.jpg')
print()

