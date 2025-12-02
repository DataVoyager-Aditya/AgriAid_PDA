import json

try:
    with open('translations.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    print("JSON is valid.")
except json.JSONDecodeError as e:
    print(f"JSON Decode Error: {e}")
    print(f"Line: {e.lineno}, Column: {e.colno}")
    print(f"Char: {e.pos}")
except Exception as e:
    print(f"Error: {e}")
