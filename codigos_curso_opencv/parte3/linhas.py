import cv2
import numpy as np
# linhas, círculo e retângulos
canvas = np.ones((300, 400, 3)) * 255
azul = (255, 0, 0)
verde = (0, 255, 0)
vermelho = (0, 0, 255)
preto = (0, 0, 0)
cv2.line(canvas, (0, 0), (400, 300), azul, 1)
#(imagem, ponto inicial, ponto final, cor, espessurada da linha
cv2.line(canvas, (200, 0), (200, 300), verde, 3)
cv2.rectangle(canvas, (10, 70), (90, 190), verde)
cv2.rectangle(canvas, (250, 50), (300, 125), vermelho, -1)
cv2.circle(canvas, (130, 230), 50, preto)
cv2.circle(canvas, (260, 230), 50, preto, -1)
#(imagem, ponto , diametro, cor, espessurada da linha
# -1 gera um retangulo com toda forma
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
