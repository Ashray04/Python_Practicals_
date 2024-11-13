import re
pattern = r"\D+"
text = "There are 24 hours in a day and 60 minutes in an hour."
matches = re.finditer(pattern, text)
for match in matches:
    print(f"Match found: {match.group()} at position {match.start()}")

pattern = r"\d+"
text = "There are 24 hours in a day and 60 minutes in an hour."
matches = re.finditer(pattern, text)
for match in matches:
    print(f"Match found: {match.group()} at position {match.start()}")