# adds image processing capabilities
from PIL import Image

# will convert the image to text string
import pytesseract

# translates into preferred language
from google_trans_new import google_translator

img = Image.open('out.jpg')

# converts the image to result and saves it into result variable
result = pytesseract.image_to_string(img)

p = google_translator()
# translates the text into french language
translated = p.translate(result, lang_tgt='french')
#https://gist.github.com/JT5D/a2fdfefa80124a06f5a9 language codes
#converts the result into string format
#translated = str(k.text)
with open('testresult.txt', mode ='w') as file:
  file.write(result)
  file.write("\n")
  file.write(translated)
  print("ready!")
