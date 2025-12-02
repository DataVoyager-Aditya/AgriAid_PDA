import json

def propagate():
    with open('translations.json', 'r', encoding='utf-8') as f:
        translations = json.load(f)

    if 'en' not in translations:
        print("Error: 'en' key not found in translations.")
        return

    en_data = translations['en']
    
    modified = False
    for lang, data in translations.items():
        if lang == 'en':
            continue
        
        print(f"Checking {lang}...")
        for key, value in en_data.items():
            if key not in data:
                data[key] = value
                modified = True
                # print(f"Added missing key '{key}' to '{lang}'")

    if modified:
        with open('translations.json', 'w', encoding='utf-8') as f:
            json.dump(translations, f, indent=4, ensure_ascii=False)
        print("Successfully propagated missing keys from 'en' to all other languages.")
    else:
        print("No missing keys found.")

if __name__ == "__main__":
    propagate()
