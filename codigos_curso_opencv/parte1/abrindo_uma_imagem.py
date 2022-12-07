# Abrindo uma imagem com o OpenCV-Python
import cv2
imagem = cv2.imread("robo.jpeg") # carregar a imagem
cv2.imshow("Imagem", imagem) #mostrar a imagem
print(f'Altura: {imagem.shape[0]} pixels')
print(f'Largura: {imagem.shape[1]} pixels')
print(f'Canais de cor: {imagem.shape[2]} pixels')
print(imagem.shape)
# shape é um vetor
#cv2.imwrite('Imagem.jpeg', imagem)
cv2.waitKey(0) # mostrar a imagem por um determinado intervalo de tempo em ms
# quando coloca o 0 será mostrado em um infinito intervalo de tempo

