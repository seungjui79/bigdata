import cv2 #opencv 불러옴

img = cv2.imread('image.jpg') #이미지 읽어줘
cv2.imshow('image', img) #이미지 보여줘
cv2.waitKey(0) #무한으로 키입력을 기다리겠다는 용도
cv2.destroyAllWindows() #창 닫아줘