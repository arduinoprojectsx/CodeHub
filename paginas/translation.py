from modeltranslation.translator import translator, TranslationOptions
from .models import Inf

class ItemTranslationOptions(TranslationOptions):
    fields = ('titulo', 'descricao',)

translator.register(Inf, ItemTranslationOptions)