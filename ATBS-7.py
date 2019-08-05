#!/usr/local/bin/python3

# Chapter 7 - Regular expressions

import re

# Pattern Matching with Regular Expressions
phoneNumRegex = re.compile(r"\d{3}-\d{3}-\d{4}")
mo = phoneNumRegex.search("My number is 415-555-4242. Your number is 415-555-5858")
print("Regex match: " + mo.group())

# Grouping with Parentheses
phoneNumRegex2 = re.compile(r"(\d{3})-(\d{3}-\d{4})")
mo2 = phoneNumRegex2.search("My number is 415-555-4242. Your number is 415-555-5858")
print("Regex group 1: {}".format(mo2.group(1)))
print("Regex group 2: {}".format(mo2.group(2)))
print("Regex group 0: {}".format(mo2.group(0)))
print("Regex group blank: {}".format(mo2.group()))
print("Regex groups: {}".format(mo2.groups()))

# The findall() Method
print("Regex findall: {}".format(phoneNumRegex.findall("My number is 415-555-4242. Your number is 415-555-5858")))
print("Regex findall groups: {}".format(phoneNumRegex2.findall("My number is 415-555-4242. Your number is 415-555-5858")))

# Matching Multiple Groups with the Pipe
heroRegex = re.compile(r"Batman|Tina Fey")
mo3 = heroRegex.search("Batman and Tina Fey.")
print(mo3.group())
mo3 = heroRegex.findall("Batman and Tina Fey.")
print(mo3)

# Optional Matching with the Question Mark
batRegex = re.compile(r"Bat(wo)?man")
mo4 = batRegex.search("The Adventures of Batman.")
print(mo4.group())
mo4 = batRegex.search("The Adventures of Batwoman.")
print(mo4.group())

# Character Classes
xmasRegex = re.compile(r"\d+\s\w+")
xmas = xmasRegex = xmasRegex.findall("12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge")
print(xmas)

# Making Your Own Character Classes
vowelRegex = re.compile(r"[aeiouAEIOU]")
print("Vowels: {}".format(vowelRegex.findall("Robocop eats baby food. BABY FOOD.")))
consonantRegex = re.compile(r"[^aeiouAEIOU]")
print("Consonants: {}".format(consonantRegex.findall("Robocop eats baby food. BABY FOOD.")))

# Case-Insensitive Matching
robocop = re.compile(r"robocop", re.I)
print(robocop.search("Robocop is part man, part machine, all cop.").group())
print(robocop.search("ROBOCOP protects the innocent.").group())
print(robocop.search("Al, why does your programming book talk about robocop so much?").group())

# Substituting Strings with the sub() Method
namesRegex = re.compile(r"Agent \w+")
print(namesRegex.sub("REDACTED", "Agent Alice gave the secret documents to Agent Bob."))
agentNamesRegex = re.compile(r"Agent (\w)\w*")
print(agentNamesRegex.sub(r"\1****", "Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent."))
