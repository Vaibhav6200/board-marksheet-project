from django import template
from translate import Translator


def translate_text(text):
    translator = Translator(to_lang="hi")  # Target language: Hindi
    translation = translator.translate(text)
    return translation

register = template.Library()


@register.filter
def hindi_filter(english_text):
    return translate_text(english_text)