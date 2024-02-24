import translators as ts
from translate import Translator


def translate(text, to_lang, translator = 'google'):
    if translator == 'google':
        result = Translator(to_lang = to_lang).translate(text = text)
        return result
    
    else:
        try:
            result = ts.translate_text(text, translator = translator, to_language = to_lang)
            return result
        
        except:
            return None