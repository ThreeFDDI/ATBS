#!/usr/local/bin/python3

# multiclipboard saves and loads text to the clipboard

# Usage: py ATBS-8_multiclipboard.pyw save <keyword> saves clipboard to keyword
# Usage: py ATBS-8_multiclipboard.pyw  <keyword> loads keyword to clipboard
# Usage: py ATBS-8_multiclipboard.pyw list loads all keywords to clipboard

import shelve, pyperclip, sys

mcbShelf = shelve.open("mcb")

# TODO - save clipboard contents

# TODO - lisr keywords and load content

mcbShelf.close()