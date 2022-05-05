import googletrans 
from googletrans import *
translator = googletrans.Translator()
translate=translator.translate('Tomorrow i am going to Rutenga',dest='shona')


language_detection = Translator()
print('The word is in '+str(language_detection.detect(translate)))
print(translate.text)