from django import forms
from .languages_code import LANGUAGES_RU
from .translator import ts
from pprint import pprint as pp


class TranslateForm(forms.Form):
    
    language_choices = LANGUAGES_RU
    
    from_lan_choices = list(LANGUAGES_RU)
    from_lan_choices.insert(0,  ('en', 'Английский'))
    from_lan_choices.insert(1,  ('ru', 'Русский'))
    
    to_lan_choices = list(LANGUAGES_RU)
    to_lan_choices.insert(0, ('ru', 'Русский'))
    to_lan_choices.insert(1, ('en', 'Английский'))
    
    translator_choices = (
        ('tr', 'Кнопка 1'),
        ('gg', 'Кнопка 2')
    )
    
    from_lan = forms.ChoiceField(required = True, choices = from_lan_choices, widget = forms.Select(attrs = {'class': 'p-2 w-100 bg-body-tertiary rounded-3 text-center', 'id': 'from_lan', 'style': 'resize: none;'}, choices = from_lan_choices))
    to_lan = forms.ChoiceField(required = True, choices = to_lan_choices, widget = forms.Select(attrs = {'class': 'p-2 w-100 bg-body-tertiary rounded-3 text-center', 'id': 'to_lan'}, choices = to_lan_choices))
    text = forms.CharField(required = True, max_length = 1000, widget = forms.Textarea(attrs = {'class': 'p-2 w-100 bg-body-tertiary rounded-3', 'rows': 6, 'id': 'area', 'style': 'resize: none;'}))
    
    translator = forms.ChoiceField(required = True, choices = translator_choices, widget = forms.RadioSelect(choices = translator_choices, attrs = {'class': 'form-check-input'}))
    

class ChoiceTranslatorForm(forms.Form):
    
    translators = ((translator, translator.capitalize()) for translator in ts.translators_pool)
    
    choice_translator = forms.ChoiceField(required = True, choices = translators, initial = 'google',widget = forms.RadioSelect(attrs={"class": "form-check-input", "type": "radio", "name": "RadioTranslator"}))