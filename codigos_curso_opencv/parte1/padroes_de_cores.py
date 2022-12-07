import cv2
imagem = cv2.imread("ferrari.jpeg") # carregar a imagem
(b, g, r) = imagem[0, 0]
print(f'Cor do pixel em (0, 0) - Vermelho: {r}, Verde: {g}, Azul: {b}')
(b, g, r) = imagem[100, 180]
print(f'Cor do pixel em (0, 0) - Vermelho: {r}, Verde: {g}, Azul: {b}')
(b, g, r) = imagem[30, 200]
print(f'Cor do pixel em (0, 0) - Vermelho: {r}, Verde: {g}, Azul: {b}')

cv2.waitKey(0)
