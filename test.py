from translate import Translator


def translate_text(text):
    translator = Translator(to_lang="hi")  # Target language: Hindi
    translation = translator.translate(text)
    return translation


english_text = "Vaibhav Paliwal"
translated_text = translate_text(english_text)
print(translated_text)
print(type(translated_text))