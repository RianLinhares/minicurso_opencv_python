#Rotação
# É necessário definir um ponto, para a fixação
import cv2
img = cv2.imread("robo.jpeg") # carregar a imagem
altura, largura = img.shape[:2]
ponto = (largura / 2, altura / 2) #ponto no centro da figura e ponto de fixação
#ponto = (0, altura)
rotacao = cv2.getRotationMatrix2D(ponto, 180, 1.0)
#(ponto de fixação, ãngulo, escala)
rotacionado = cv2.warpAffine(img, rotacao, (largura, altura))
cv2.imshow("Rotacionado 45 graus", rotacionado)
cv2.waitKey(0)
