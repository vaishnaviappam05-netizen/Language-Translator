from translate import Translator

def translate_text(input_text, target_language):
    
    translator = Translator(to_lang=target_language)

   
    translated_text = translator.translate(input_text)

    return translated_text

if __name__ == "__main__":
    
    input_text = input("Enter text to translate: ")

    
    target_lang = input("Enter target language code (e.g., 'hi' for Hindi, 'te' for Telugu): ")

    
    translated_text = translate_text(input_text, target_lang)

   
    print("Translated text:", translated_text)
