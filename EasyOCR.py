import minecart              #extracts images from pdf
import easyocr               #open source ocr library
import numpy as np           #numpy to convert PIL image to numpy array for opencv
import cv2 as cv             #opencv for image processing
import re                    #regular expression
import json                  #for outputting in a json file
from tqdm import tqdm        #just for a fancy progess bar as this program takes time for execution
import matplotlib.pyplot as plt
from pylab import rcParams
from IPython.display import Image
import PIL
from PIL import ImageDraw
rcParams['figure.figsize'] = 8, 16
location=input("Enter the location of your pdf file")
pdffile = open(location, 'rb')
doc = minecart.Document(pdffile)
#creating a reader object
reader = easyocr.Reader(['en'])
#getting images
images=[]
print("iterating through all pages")
for page in doc.iter_pages():
    im = page.images[0].as_pil()  # requires pillow
    images.append(im)
complete_text=''

pdffile.close()


print("pattern finding")
complete_text=complete_text.replace("\n","")
regx=r'(Q[\dI]+\.[\d’‘______‘’“”×-–\[\]&\sa-zA-Z\-\(\),\'\x21-\x2F\x3A-\x40\x5B-\x60\x7B-\x7E]+?)\(a\)([\d’‘______‘’“”×-–\[\]&\sa-zA-Z\-\(\),\'\x21-\x2F\x3A-\x40\x5B-\x60\x7B-\x7E]+?)\([b ]+\)([\d’‘______‘’“”×-–\[\]&\sa-zA-Z\-\(\),\'\x21-\x2F\x3A-\x40\x5B-\x60\x7B-\x7E]+?)\(c\)([\d’‘______‘’“”×-–\[\]&\sa-zA-Z\-\(\),\'\x21-\x2F\x3A-\x40\x5B-\x60\x7B-\x7E]+?)\(d\)([\d’‘______‘’“”×-–\[\]&\sa-zA-Z\-\(\),\'\x21-\x2F\x3A-\x40\x5B-\x60\x7B-\x7E]+?)Ans:([\sa-d\-\(\),\'\x21-\x2F\x3A-\x40\x5B-\x60\x7B-\x7E]+?\))'
questions_list=re.findall(regx,complete_text)
questions_list=[list(item) for item in questions_list]
print("outputing a JSON")

to_json=[]
for i in questions_list:
    if len(i[5])>4:
        i[5]=i[5][:-3]+i[5][-2:]
    to_json.append({'question':i[0],'option1':i[1],'option2':i[2],'option3':i[3],'option4':i[4],'answer':i[5]})
with open("book.json",'w') as file:
    json.dump(to_json,file,indent=4)
