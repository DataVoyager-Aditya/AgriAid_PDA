import json

required_keys = [
    "testimonials_subtitle",
    "testimonial_1_role", "testimonial_1_text",
    "testimonial_2_role", "testimonial_2_text",
    "testimonial_3_role", "testimonial_3_text",
    "testimonial_4_role", "testimonial_4_text",
    "testimonial_5_role", "testimonial_5_text",
    "testimonial_6_role", "testimonial_6_text",
    "success_stories_subtitle",
    "story_1_title", "story_1_desc",
    "stat_farmers", "stat_acres_protected",
    "story_2_title", "story_2_desc",
    "stat_acres_saved",
    "video_testimonials_subtitle",
    "video_desc_1", "video_desc_2"
]

try:
    with open('translations.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    print("JSON is valid.")
    
    lang = 'en'
    if lang not in data:
        print(f"Language '{lang}' not found in JSON.")
        exit(1)
        
    translations = data[lang]
    missing_keys = []
    for key in required_keys:
        if key not in translations:
            missing_keys.append(key)
            
    if missing_keys:
        print(f"Missing keys in '{lang}': {missing_keys}")
    else:
        print(f"All required keys found in '{lang}'.")
        
except json.JSONDecodeError as e:
    print(f"JSON Decode Error: {e}")
except Exception as e:
    print(f"Error: {e}")
