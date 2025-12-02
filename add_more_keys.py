import json

new_keys = {
    "tech_mobile_title": "Mobile-First Design",
    "tech_mobile_desc": "Responsive web application that works seamlessly on smartphones, tablets, and computers, designed for rural connectivity conditions."
}

try:
    with open('translations.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    for lang in data:
        for key, value in new_keys.items():
            if key not in data[lang]:
                data[lang][key] = value

    with open('translations.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    
    print("Successfully added tech_mobile keys.")

except Exception as e:
    print(f"Error: {e}")
