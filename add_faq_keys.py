import json

new_keys = {
    "contact_reach_us": "Reach Us",
    "faq_q1": "How accurate is AgriAid's disease detection?",
    "faq_a1": "AgriAid achieves 98.4% accuracy in disease detection through advanced AI algorithms trained on thousands of crop images from Indian agricultural conditions.",
    "faq_q2": "Which crops are supported by AgriAid?",
    "faq_a2": "We currently support 5 major Indian crops: Wheat, Rice, Corn, Sugarcane, and Potato with comprehensive disease detection capabilities.",
    "faq_q3": "Is AgriAid free to use?",
    "faq_a3": "Yes, AgriAid is completely free for farmers. Our mission is to democratize access to advanced agricultural technology.",
    "faq_q4": "Can I use AgriAid on my smartphone?",
    "faq_a4": "Absolutely! AgriAid is designed to work perfectly on smartphones, tablets, and computers. It's optimized for rural internet conditions.",
    "faq_q5": "How do I get the best results from image uploads?",
    "faq_a5": "For best results, take clear, well-lit photos of affected leaves or plant parts. Use natural daylight and focus on single leaves showing disease symptoms."
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
    
    print("Successfully added FAQ keys.")

except Exception as e:
    print(f"Error: {e}")
