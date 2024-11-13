import re
pattern=r"rey"
text="wankhede ashray"
search=re.search(pattern,text)
print("match found:",search.group() if search else "no match")