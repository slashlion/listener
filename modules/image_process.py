import pytesseract
import cv2

def img_txt(img):
    try:
        pytesseract.pytesseract.tesseract_cmd = r'C:\\Users\\adrian.leon\\miniconda3\\envs\\receptor-mensajes\\Library\\bin\\tesseract.exe'
        image = cv2.imread(img)
        image = cv2.resize(image, (500, 500))
        crop_img = image[300:450, 60:450]
        text = pytesseract.image_to_string(crop_img)
        large = len(text)
        txt = text.split()

        if len(txt) > 1:
            txt = txt[0]+txt[2]
            return txt


        # para llamar a la funcion usar:
        # path = 'images/example.jpg'
        # print(img_txt(path))

        return txt
    except Exception as e:
        print("ERROR : ", e)

