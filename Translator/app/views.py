from django.shortcuts import render
from django.http import HttpRequest
from . import translator, forms
# Create your views here.

def translator_page(request: HttpRequest):
    form = forms.TranslateForm()
    choice_translator = forms.ChoiceTranslatorForm()
    return render(request, 'app/translator.html', context = {'form': form, 'translators': choice_translator})
