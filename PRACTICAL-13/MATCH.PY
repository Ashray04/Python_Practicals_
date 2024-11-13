import re
pattern=r"Engineering"
text="Engineering College: sggs Nanded"
match=re.match(pattern,text)
print("match found:",match.group() if match else "no match")
#output ---> match found: Engineering
pattern=r"sggs"
text="Engineering College: sggs Nanded"
match=re.match(pattern,text)
print("match found:",match.group() if match else "no match")
# output---> match found: no match