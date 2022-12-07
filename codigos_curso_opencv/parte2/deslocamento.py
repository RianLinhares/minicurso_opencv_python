import numpy as np
import cv2
img = cv2.imread('robo.jpeg')
print(img.shape)
altura, largura = img.shape[:2]
cv2.imshow("Original", img)
#A translação de uma imagem é realizada utilizando o método da OpenCV chamado warpAffine()
#Esse método espera o objeto de imagem que será transladado, uma matriz de deslocamento e as dimensões da imagem
#translacao (deslocamento)
#A matrix de deslocamento está sendo estabelecida indicando na primeira linha o deslocamento no eixo
# “x” e na segunda linha o deslocamento a ser aplicado no eixo “y”.
#Para o deslocamento deve ser fornecida uma matriz com valores de ponto flutuante,
#com feito na linha 11. As duas primeira colunas não devem ser alteradas, sendo a última coluna a de
#interesse para especificar o deslocamento. O valor na primeira linha é o deslocamento no eixo “x”,
#fazendo com que seja deslocado horizontalmente a quantidade de
#pixels informada. Já o valor na segunda linha especifica o deslocamento no eixo “y”, fazendo o deslocamento vertical.
deslocamento1 = np.float32([[1, 0, 25], [0, 1, 50]])
deslocado1 = cv2.warpAffine(img, deslocamento1, (largura, altura))
cv2.imshow("Baixo e direita", deslocado1)

deslocamento2 = np.float32([[1, 0, -50], [0, 1, -90]])
deslocado2 = cv2.warpAffine(img, deslocamento2, (largura, altura))
cv2.imshow("Cima e esquerda", deslocado2)
cv2.waitKey(0)
