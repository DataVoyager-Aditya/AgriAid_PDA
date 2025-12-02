import json
import shutil

def merge():
    # Load main translations
    with open('translations.json', 'r', encoding='utf-8') as f:
        translations = json.load(f)

    # Load fragment
    with open('translations_fragment.json', 'r', encoding='utf-8') as f:
        fragment = json.load(f)

    # Merge into 'en'
    if 'en' not in translations:
        translations['en'] = {}
    
    translations['en'].update(fragment)

    # Save back
    with open('translations.json', 'w', encoding='utf-8') as f:
        json.dump(translations, f, indent=4, ensure_ascii=False)
    
    print("Merged translations successfully.")

    # Overwrite disease database
    shutil.copy('disease_database_keys.json', 'disease_database.json')
    print("Updated disease_database.json")

if __name__ == "__main__":
    merge()
