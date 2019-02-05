import re

s = "Cats are smarter than dogs"

matchObj = re.match( r"(.*) are (.*?) .*", s, re.M|re.I)

if matchObj:
   print ("matchObj.group() : ", matchObj.group())
else:
   print ("No match!!")