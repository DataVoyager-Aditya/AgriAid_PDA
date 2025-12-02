import json
from hindi_translations import hindi_data
from bengali_translations import bengali_data
from marathi_translations import marathi_data
from tamil_translations import tamil_data

def apply_translations():
    with open('translations.json', 'r', encoding='utf-8') as f:
        translations = json.load(f)

    # Apply Hindi
    if 'hi' in translations:
        print("Applying Hindi translations...")
        for key, value in hindi_data.items():
            translations['hi'][key] = value
    else:
        print("Hindi ('hi') key not found in translations.json")

    # Apply Bengali
    if 'bn' in translations:
        print("Applying Bengali translations...")
        for key, value in bengali_data.items():
            translations['bn'][key] = value
    else:
        print("Bengali ('bn') key not found in translations.json")

    # Apply Marathi
    if 'mr' in translations:
        print("Applying Marathi translations...")
        for key, value in marathi_data.items():
            translations['mr'][key] = value
    else:
        print("Marathi ('mr') key not found in translations.json")

    # Apply Tamil
    if 'ta' in translations:
        print("Applying Tamil translations...")
        for key, value in tamil_data.items():
            translations['ta'][key] = value
    else:
        print("Tamil ('ta') key not found in translations.json")

    # Save changes
    with open('translations.json', 'w', encoding='utf-8') as f:
        json.dump(translations, f, indent=4, ensure_ascii=False)
    
    print("Translations updated successfully.")

if __name__ == "__main__":
    apply_translations()
