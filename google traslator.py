from googletrans import Translator

translator = Translator()

translated = translator.translate("Wie geht es Ihnen",src='de',dest='en')#traslate english langage to german langage

print(translated.text)