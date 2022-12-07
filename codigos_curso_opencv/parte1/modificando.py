import cv2
img = cv2.imread("robo.jpeg")
img[0, 0] = (255, 0, 0)
img[0:50] = (0, 0, 255)
cv2.imshow("Modificada", img)
cv2.waitKey(0)

