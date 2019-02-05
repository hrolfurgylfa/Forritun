s = input()
r = 0
for stafur in s:
    if stafur == "r":
        r += 1
        if r == 2:
            break

if s[0] == "b" and r >= 2 and s[-1] in ["a", "e", "i", "o", "u", "y"]:
    print("Jebb")
else:
    print("Neibb")