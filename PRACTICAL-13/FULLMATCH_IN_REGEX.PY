import re
pattern = r"\d{3}-\d{1}-\d{4}"
text = "123-45-6789"
full_match = re.fullmatch(pattern, text)
print("Full match found:", full_match.group() if full_match else "No full match")
#
pattern = r"\d{3}-\d{2}-\d{4}"
text = "123-45-6789"
full_match = re.fullmatch(pattern, text)
print("Full match found:", full_match.group() if full_match else "No full match")
