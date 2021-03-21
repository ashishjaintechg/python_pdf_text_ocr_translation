from PIL import Image
import pytesseract

img = Image.open("out.jpg")
img.load()
custom_config = r'-l eng+hin --psm 6'
txt = pytesseract.image_to_string(img, config=custom_config)

print(txt)

from langdetect import detect_langs
print(detect_langs(txt))

img = Image.open("out.jpg")
img.load()
custom_config = r'-l eng --psm 6'
custom_config
text = pytesseract.image_to_string(img, custom_config)
#text = pytesseract.image_to_string(img, lang="en"custom_config)  #Specify language to look after!
print(text)
