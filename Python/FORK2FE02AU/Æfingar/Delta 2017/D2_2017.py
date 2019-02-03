import re

s = input()

if s[0] == "b" and re.match("*r*r*", s) and s[-1] in ["a","e","i","o","u","y"]:
    print("Jebb")
else:
    print("Neibb")