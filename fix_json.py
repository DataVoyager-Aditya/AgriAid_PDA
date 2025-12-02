with open('translations.json', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Keep lines from index 103 to -1 (excluding last line)
# Line 103 in file is index 102. But wait.
# Python output said "Line 103: ```json". That is index 102.
# So I want to start from index 103 (Line 104).
# And exclude the last line (index -1).
new_content = lines[103:-1]

with open('translations.json', 'w', encoding='utf-8') as f:
    f.writelines(new_content)
