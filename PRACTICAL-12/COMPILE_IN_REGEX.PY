import re
pattern = re.compile(r"\d+")
text = "The room number is 409."
search = pattern.search(text)
print("Compiled search result:", search.group() if search else "No match")

pattern = re.compile(r"\D+")
text = "The room number is 409."
search = pattern.search(text)
print("Compiled search result:", search.group() if search else "No match")
