import pytesseract
import PIL.Image
import cv2

#https://www.youtube.com/watch?v=PY_N1XdFp4w

myconfig = r"--psm 11 --oem 3"

text = pytesseract.image_to_string(PIL.Image.open("img_2.png"), config=myconfig)
print(text)