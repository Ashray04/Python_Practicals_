import re
pattern = r"\d+"  # Match any sequence of digits
text = "There are 24 hours in a day and 60 minutes in an hour."
all_matches = re.findall(pattern, text)
print("All matches:", all_matches)
# OUTPUT---> All matches: ['24', '60']