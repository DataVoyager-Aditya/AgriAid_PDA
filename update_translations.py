import json

def load_translations():
    with open('translations.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def save_translations(data):
    with open('translations.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def update_translations():
    data = load_translations()
    
    # Hindi Translations
    hi_updates = {
        "crop_wheat": "गेहूँ",
        "crop_rice": "चावल",
        "crop_corn": "मक्का",
        "crop_sugarcane": "गन्ना",
        "crop_potato": "आलू",
        "disease_brown_rust": "भूरा रस्ट (Leaf Rust)",
        "disease_yellow_rust": "पीला रस्ट (Stripe Rust)",
        "disease_healthy": "स्वस्थ फसल",
        "disease_brown_spot": "भूरा धब्बा (Brown Spot)",
        "disease_leaf_blast": "लीफ ब्लास्ट",
        "disease_neck_blast": "नेक ब्लास्ट",
        "disease_common_rust": "सामान्य रस्ट",
        "disease_gray_leaf": "ग्रे लीफ स्पॉट",
        "disease_northern_blight": "उत्तरी लीफ ब्लाइट",
        "disease_bacterial_blight": "बैक्टीरियल ब्लाइट",
        "disease_red_rot": "लाल सड़न (Red Rot)",
        "disease_early_blight": "अगेती झुलसा (Early Blight)",
        "disease_late_blight": "पछेती झुलसा (Late Blight)",
        "tech_dl_title": "डीप लर्निंग मॉडल",
        "tech_dl_desc": "हमारा ResNet50-आधारित आर्किटेक्चर रोग पहचान में 98.4% सटीकता प्राप्त करता है, जिसे भारतीय कृषि स्थितियों से हजारों फसल छवियों पर प्रशिक्षित किया गया है।",
        "tech_db_title": "व्यापक डेटाबेस",
        "tech_db_desc": "जैविक और रासायनिक उपचार समाधान, रोकथाम विधियों और फसल-विशिष्ट सिफारिशों के साथ व्यापक रोग डेटाबेस।",
        "tech_cloud_title": "क्लाउड इन्फ्रास्ट्रक्चर",
        "tech_cloud_desc": "स्केलेबल क्लाउड-आधारित प्रसंस्करण भारत भर के किसानों के लिए तेजी से प्रतिक्रिया समय और विश्वसनीय सेवा उपलब्धता सुनिश्चित करता है।",
        "tech_mobile_title": "मोबाइल-फर्स्ट डिज़ाइन",
        "tech_mobile_desc": "रिस्पॉन्सिव वेब एप्लिकेशन जो स्मार्टफोन, टैबलेट और कंप्यूटर पर निर्बाध रूप से काम करता है, जिसे ग्रामीण कनेक्टिविटी स्थितियों के लिए डिज़ाइन किया गया है।",
        "faq_q1": "एग्रीएड की रोग पहचान कितनी सटीक है?",
        "faq_a1": "एग्रीएड उन्नत एआई एल्गोरिदम के माध्यम से रोग पहचान में 98.4% सटीकता प्राप्त करता है।",
        "faq_q2": "एग्रीएड द्वारा कौन सी फसलें समर्थित हैं?",
        "faq_a2": "हम वर्तमान में 5 प्रमुख भारतीय फसलों का समर्थन करते हैं: गेहूं, चावल, मक्का, गन्ना और आलू।",
        "faq_q3": "क्या एग्रीएड उपयोग करने के लिए स्वतंत्र है?",
        "faq_a3": "हाँ, एग्रीएड किसानों के लिए पूरी तरह से मुफ़्त है। हमारा मिशन उन्नत कृषि तकनीक तक पहुँच को लोकतांत्रिक बनाना है।",
        "faq_q4": "क्या मैं अपने स्मार्टफोन पर एग्रीएड का उपयोग कर सकता हूं?",
        "faq_a4": "बिल्कुल! एग्रीएड को स्मार्टफोन, टैबलेट और कंप्यूटर पर पूरी तरह से काम करने के लिए डिज़ाइन किया गया है।",
        "faq_q5": "मैं छवि अपलोड से सर्वोत्तम परिणाम कैसे प्राप्त करूं?",
        "faq_a5": "सर्वोत्तम परिणामों के लिए, प्रभावित पत्तियों या पौधों के हिस्सों की स्पष्ट, अच्छी तरह से रोशनी वाली तस्वीरें लें।"
    }
    
    # Bengali Translations
    bn_updates = {
        "crop_wheat": "গম",
        "crop_rice": "ধান",
        "crop_corn": "ভুট্টা",
        "crop_sugarcane": "আখ",
        "crop_potato": "আলু",
        "disease_brown_rust": "বাদামী মরিচা (Leaf Rust)",
        "disease_yellow_rust": "হলুদ মরিচা (Stripe Rust)",
        "disease_healthy": "সুস্থ ফসল",
        "disease_brown_spot": "বাদামী দাগ (Brown Spot)",
        "disease_leaf_blast": "লিফ ব্লাস্ট",
        "disease_neck_blast": "নেক ব্লাস্ট",
        "disease_common_rust": "সাধারণ মরিচা",
        "disease_gray_leaf": "ধূসর পাতার দাগ",
        "disease_northern_blight": "উত্তরের ঝলসানো রোগ",
        "disease_bacterial_blight": "ব্যাকটেরিয়াল ব্লাস্ট",
        "disease_red_rot": "লাল পচা রোগ (Red Rot)",
        "disease_early_blight": "আগাম ধসা রোগ (Early Blight)",
        "disease_late_blight": "নাবি ধসা রোগ (Late Blight)",
        "tech_dl_title": "ডিপ লার্নিং মডেল",
        "tech_dl_desc": "আমাদের ResNet50-ভিত্তিক আর্কিটেকচার রোগ সনাক্তকরণে ৯৮.৪% নির্ভুলতা অর্জন করে।",
        "tech_db_title": "বিস্তৃত ডেটাবেস",
        "tech_db_desc": "জৈব এবং রাসায়নিক চিকিত্সা সমাধান সহ বিস্তৃত রোগ ডেটাবেস।",
        "tech_cloud_title": "ক্লাউড ইনফ্রাস্ট্রাকচার",
        "tech_cloud_desc": "স্কেলেবল ক্লাউড-ভিত্তিক প্রসেসিং দ্রুত প্রতিক্রিয়া সময় নিশ্চিত করে।",
        "tech_mobile_title": "মোবাইল-ফার্স্ট ডিজাইন",
        "tech_mobile_desc": "রেসপন্সিভ ওয়েব অ্যাপ্লিকেশন যা স্মার্টফোন, ট্যাবলেট এবং কম্পিউটারে নির্বিঘ্নে কাজ করে।",
        "faq_q1": "এগ্রিএইড কতটা নির্ভুল?",
        "faq_a1": "এগ্রিএইড রোগ সনাক্তকরণে ৯৮.৪% নির্ভুলতা অর্জন করে।",
        "faq_q2": "কোন ফসলগুলি সমর্থিত?",
        "faq_a2": "আমরা বর্তমানে ৫টি প্রধান ফসল সমর্থন করি: গম, ধান, ভুট্টা, আখ এবং আলু।",
        "faq_q3": "এগ্রিএইড কি বিনামূল্যে?",
        "faq_a3": "হ্যাঁ, এগ্রিএইড কৃষকদের জন্য সম্পূর্ণ বিনামূল্যে।",
        "faq_q4": "আমি কি স্মার্টফোনে ব্যবহার করতে পারি?",
        "faq_a4": "অবশ্যই! এগ্রিএইড স্মার্টফোনে পুরোপুরি কাজ করার জন্য ডিজাইন করা হয়েছে।",
        "faq_q5": "কিভাবে সেরা ফলাফল পাব?",
        "faq_a5": "সেরা ফলাফলের জন্য, আক্রান্ত পাতার পরিষ্কার এবং ভালো আলোর ছবি নিন।"
    }

    # Marathi Translations
    mr_updates = {
        "crop_wheat": "गहू",
        "crop_rice": "तांदूळ",
        "crop_corn": "मका",
        "crop_sugarcane": "ऊस",
        "crop_potato": "बटाटा",
        "disease_brown_rust": "तपकिरी तांबेरा (Leaf Rust)",
        "disease_yellow_rust": "पिवळा तांबेरा (Stripe Rust)",
        "disease_healthy": "निरोगी पीक",
        "disease_brown_spot": "तपकिरी ठिपके (Brown Spot)",
        "disease_leaf_blast": "पानावरील करपा (Leaf Blast)",
        "disease_neck_blast": "मानेवरील करपा (Neck Blast)",
        "disease_common_rust": "सामान्य तांबेरा",
        "disease_gray_leaf": "करपा (Gray Leaf Spot)",
        "disease_northern_blight": "उत्तरी करपा",
        "disease_bacterial_blight": "जीवाणूजन्य करपा",
        "disease_red_rot": "लाल कुज (Red Rot)",
        "disease_early_blight": "लवकर येणारा करपा (Early Blight)",
        "disease_late_blight": "उशिरा येणारा करपा (Late Blight)",
        "tech_dl_title": "डीप लर्निंग मॉडेल्स",
        "tech_dl_desc": "आमचे ResNet50-आधारित आर्किटेक्चर रोग ओळखण्यात 98.4% अचूकता प्राप्त करते.",
        "tech_db_title": "व्यापक डेटाबेस",
        "tech_db_desc": "सेंद्रिय आणि रासायनिक उपचार उपायांसह विस्तृत रोग डेटाबेस.",
        "tech_cloud_title": "क्लाउड इन्फ्रास्ट्रक्चर",
        "tech_cloud_desc": "स्केलेबल क्लाउड-आधारित प्रक्रिया जलद प्रतिसाद वेळ सुनिश्चित करते.",
        "tech_mobile_title": "मोबाईल-फर्स्ट डिझाइन",
        "tech_mobile_desc": "रिस्पॉन्सिव्ह वेब ॲप्लिकेशन जे स्मार्टफोन, टॅब्लेट आणि संगणकावर अखंडपणे कार्य करते.",
        "faq_q1": "एग्रीएड किती अचूक आहे?",
        "faq_a1": "एग्रीएड रोग ओळखण्यात 98.4% अचूकता प्राप्त करते.",
        "faq_q2": "कोणती पिके समर्थित आहेत?",
        "faq_a2": "आम्ही सध्या 5 प्रमुख पिकांना समर्थन देतो: गहू, तांदूळ, मका, ऊस आणि बटाटा.",
        "faq_q3": "एग्रीएड वापरण्यासाठी विनामूल्य आहे का?",
        "faq_a3": "होय, एग्रीएड शेतकऱ्यांसाठी पूर्णपणे विनामूल्य आहे.",
        "faq_q4": "मी माझ्या स्मार्टफोनवर एग्रीएड वापरू शकतो का?",
        "faq_a4": "नक्कीच! एग्रीएड स्मार्टफोनवर उत्तम प्रकारे कार्य करण्यासाठी डिझाइन केले आहे.",
        "faq_q5": "मी सर्वोत्तम परिणाम कसे मिळवू शकतो?",
        "faq_a5": "सर्वोत्तम परिणामांसाठी, प्रभावित पानांचे स्पष्ट आणि चांगल्या प्रकाशात फोटो घ्या."
    }

    # Tamil Translations
    ta_updates = {
        "crop_wheat": "கோதுமை",
        "crop_rice": "அரிசி",
        "crop_corn": "சோளம்",
        "crop_sugarcane": "கரும்பு",
        "crop_potato": "உருளைக்கிழங்கு",
        "disease_brown_rust": "பழுப்பு துரு நோய்",
        "disease_yellow_rust": "மஞ்சள் துரு நோய்",
        "disease_healthy": "ஆரோக்கியமான பயிர்",
        "disease_brown_spot": "பழுப்பு புள்ளி நோய்",
        "disease_leaf_blast": "இலை கருகல் நோய்",
        "disease_neck_blast": "கழுத்து கருகல் நோய்",
        "disease_common_rust": "சாதாரண துரு நோய்",
        "disease_gray_leaf": "சாம்பல் இலை புள்ளி",
        "disease_northern_blight": "வடக்கு இலை கருகல்",
        "disease_bacterial_blight": "பாக்டீரியல் கருகல்",
        "disease_red_rot": "சிவப்பு அழுகல் நோய்",
        "disease_early_blight": "முன்கூட்டிய கருகல் நோய்",
        "disease_late_blight": "தாமதமான கருகல் நோய்",
        "tech_dl_title": "ஆழ்ந்த கற்றல் மாதிரிகள்",
        "tech_dl_desc": "எங்கள் ResNet50 அடிப்படையிலான கட்டமைப்பு நோய் கண்டறிதலில் 98.4% துல்லியத்தை அடைகிறது.",
        "tech_db_title": "விரிவான தரவுத்தளம்",
        "tech_db_desc": "இயற்கை மற்றும் ரசாயன சிகிச்சை தீர்வுகளுடன் விரிவான நோய் தரவுத்தளம்.",
        "tech_cloud_title": "கிளவுட் உள்கட்டமைப்பு",
        "tech_cloud_desc": "அளவிடக்கூடிய கிளவுட் செயலாக்கம் விரைவான பதில் நேரத்தை உறுதி செய்கிறது.",
        "tech_mobile_title": "மொபைல்-முதல் வடிவமைப்பு",
        "tech_mobile_desc": "ஸ்மார்ட்போன்கள், டேப்லெட்டுகள் மற்றும் கணினிகளில் சீராக செயல்படும் செயலி.",
        "faq_q1": "AgriAid எவ்வளவு துல்லியமானது?",
        "faq_a1": "AgriAid நோய் கண்டறிதலில் 98.4% துல்லியத்தை அடைகிறது.",
        "faq_q2": "எந்த பயிர்கள் ஆதரிக்கப்படுகின்றன?",
        "faq_a2": "நாங்கள் தற்போது 5 முக்கிய பயிர்களை ஆதரிக்கிறோம்: கோதுமை, அரிசி, சோளம், கரும்பு மற்றும் உருளைக்கிழங்கு.",
        "faq_q3": "AgriAid பயன்படுத்த இலவசமா?",
        "faq_a3": "ஆம், AgriAid விவசாயிகளுக்கு முற்றிலும் இலவசம்.",
        "faq_q4": "நான் எனது ஸ்மார்ட்போனில் பயன்படுத்தலாமா?",
        "faq_a4": "நிச்சயமாக! AgriAid ஸ்மார்ட்போன்களில் சிறப்பாக செயல்பட வடிவமைக்கப்பட்டுள்ளது.",
        "faq_q5": "சிறந்த முடிவுகளை எவ்வாறு பெறுவது?",
        "faq_a5": "சிறந்த முடிவுகளுக்கு, பாதிக்கப்பட்ட இலைகளின் தெளிவான புகைப்படங்களை எடுக்கவும்."
    }

    # Update Data
    if 'hi' in data: data['hi'].update(hi_updates)
    if 'bn' in data: data['bn'].update(bn_updates)
    if 'mr' in data: data['mr'].update(mr_updates)
    if 'ta' in data: data['ta'].update(ta_updates)

    save_translations(data)
    print("Translations updated successfully!")

if __name__ == "__main__":
    update_translations()
