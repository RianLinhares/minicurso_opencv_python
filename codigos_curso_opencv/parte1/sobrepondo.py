import cv2
img = cv2.imread("robo.jpeg")
fatia = img[0:50, 50:100]
img[137: 137 + fatia.shape[0], 141: 141 + fatia.shape[1]] = fatia
cv2.imshow("Fatia da imagem", img)
cv2.waitKey(0)
