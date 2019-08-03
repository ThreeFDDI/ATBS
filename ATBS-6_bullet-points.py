#!/usr/local/bin/python3

# ATBS-6_bullet-points.py will add bullet points to text in the clipboard

import pyperclip

# take in text from the clipboard
text = pyperclip.paste()

# split text by newline
text = text.split("\n")

# prepend each line with a bullet point 
for i in range(len(text)):
    text[i] = "* " + text[i]

# convert list back into string    
text = "\n".join(text)

# send to the clipboard
pyperclip.copy(text)
