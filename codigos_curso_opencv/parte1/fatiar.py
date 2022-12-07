import cv2
img = cv2.imread("robo.jpeg")
fatia = img[37:54, 40:142]
cv2.imshow("Fatia da imagem", fatia)
cv2.waitKey(0)
