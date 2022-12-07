import cv2
img = cv2.imread("robo.jpeg")
inverter = cv2.flip(img, 1) # -1 verticalmente
cv2.imshow("Espelhado horizontalmente", inverter)
cv2.waitKey(0)
