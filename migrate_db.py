import json
import re

def make_key(text, prefix, index=None):
    # Create a simplified key from text or just use prefix + index
    if index is not None:
        return f"{prefix}_{index}"
    return prefix

def migrate():
    with open('disease_database.json', 'r') as f:
        db = json.load(f)

    translations = {}
    new_db = {}

    for crop, data in db.items():
        new_db[crop] = {"classes": data["classes"], "diseases": {}}
        for disease, info in data["diseases"].items():
            # Create a short disease identifier
            disease_id = disease.lower().replace("___", "_").replace(" ", "_")
            
            new_info = {}
            
            # Description
            desc_key = f"desc_{disease_id}"
            translations[desc_key] = info["description"]
            new_info["description"] = desc_key
            
            # Organic Solutions
            new_info["organic_solutions"] = []
            for i, sol in enumerate(info["organic_solutions"]):
                key = f"sol_org_{disease_id}_{i+1}"
                translations[key] = sol
                new_info["organic_solutions"].append(key)
                
            # Chemical Solutions
            new_info["chemical_solutions"] = []
            for i, sol in enumerate(info["chemical_solutions"]):
                key = f"sol_chem_{disease_id}_{i+1}"
                translations[key] = sol
                new_info["chemical_solutions"].append(key)
                
            # Prevention
            new_info["prevention"] = []
            for i, sol in enumerate(info["prevention"]):
                key = f"prev_{disease_id}_{i+1}"
                translations[key] = sol
                new_info["prevention"].append(key)
                
            new_db[crop]["diseases"][disease] = new_info

    # Save new DB
    with open('disease_database_keys.json', 'w') as f:
        json.dump(new_db, f, indent=4)

    # Save translations fragment
    with open('translations_fragment.json', 'w') as f:
        json.dump(translations, f, indent=4)

    print("Migration files created: disease_database_keys.json and translations_fragment.json")

if __name__ == "__main__":
    migrate()
