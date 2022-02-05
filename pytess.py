
from PIL import Image
import pytesseract




pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

img_obj = Image.open('Desktop/Python/syn.jpg')

#print(img_obj.size)




def binarize(img, thres):
    '''Changing the image to just black and white'''
    img = img.convert('L')
    


    for x in range(img.width):
        for y in range(img.height):
            if img.getpixel((x,y))>thres:
                img.putpixel((x,y),255)
            else:
                img.putpixel((x,y),0)
    return img                


def modstring(st):
    '''Removes unwanted characters from the string that is passed into the function'''
    new_st=''

    for char in st:
        if char in char_check:
            rep_char= char.replace(char, ' ')
        else:
            rep_char=char    

        new_st= new_st+ rep_char
       
    return new_st

#crops out only the text paragraph living out the picture and table of content
text_box = img_obj.crop((1250,2200,2800,3700))
#text_box.show()

char_check=['@','-','|','°',',','"']


bina_img = binarize(text_box,160)

#converts the image to string
img_to_st= pytesseract.image_to_string(bina_img)
words= img_to_st.split()


#counts the number of words in the paragraph
word_count={}

for word in words:
    ref_word= modstring(word)
    word_count[ref_word]= word_count.get(ref_word,0)+1

print(word_count)   



