import re
pattern = r"\s+"  # Split on whitespace
text = "so sure of yourselves"
words = re.split(pattern, text)
print("Words:", words)

pattern = r""  # Split on nospace
text = "sosureofyourselves"
words = re.split(pattern, text)
print("Words:", words)

