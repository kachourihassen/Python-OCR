import cv2
import pytesseract

img = cv2.imread('chequeAltijari.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

h, w, c = img.shape
boxes = pytesseract.image_to_boxes(img) 
print(boxes)

cv2.imshow('img', img)
cv2.waitKey(0)