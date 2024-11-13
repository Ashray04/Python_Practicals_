import re
pattern = r"\d+"
text = "Today is the 13th of November."
new_text = re.sub(pattern, "XX", text)
print("After substitution:", new_text)

pattern = r"\D+"
text = "Today is the 13"
new_text = re.sub(pattern, "his birthday is on ", text)
print("After substitution:", new_text)