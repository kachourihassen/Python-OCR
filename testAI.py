import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread('7.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
 
custom_config = r'--oem 3 --psm 6'

boxes= pytesseract.image_to_boxes(img)
hImg,WImg,_= img.shape
for b in boxes.splitlines():
    b=b.split(' ')
    print(b)
    x,y,w,h = int(b[1]),int(b[2]),int(b[3]),int(b[4])
    cv2.rectangle(img,(x,hImg-y),(w,hImg-h),(0,0,255),1)
    # cv2.putText(img,b[0],(x,hImg-y+25),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),1)
print("############################")
print(pytesseract.image_to_string(img, config=custom_config))
print("############################")
cv2.imshow('Result',img)
cv2.waitKey(0)