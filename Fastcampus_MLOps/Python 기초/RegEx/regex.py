import re
text = "The quick brown fox jumps over the lazy dog."

search_result = re.search(r'the', text)
print(f"Searching for {search_result}")

match_result = re.match(r'the', text)
print(f"Matching for {match_result}")

find_all_result = re.findall(r'the', text, re.IGNORECASE)
print(f"All Founding for {find_all_result}")


new_text = re.sub(r'fox', 'cat', text)
print(f"New text for: {new_text}")