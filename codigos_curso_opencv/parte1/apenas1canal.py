import cv2
img = cv2.imread("robo.jpeg")
print(f"As dimensões dessa imagem são: {img.shape}")
altura, largura, cores = img.shape
for y in range(0, altura):
    for x in range(0, largura):
        azul, verde, vermelho = img[y][x]
        img[y][x] = [0, 0, vermelho]

cv2.imshow("Apenas 1 canal", img)
cv2.waitKey(0)
