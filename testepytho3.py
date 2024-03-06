import cv2
imagem = cv2.imread('C:\\Users\\roger\\Downloads\\barracadacidadelogo.jpg')
for y in range(0, imagem.shape[0]):
     for x in range(0, imagem.shape[1]):
     
         imagem[y, x] = (255,0,0)#pinta todos os pixs varridos pelo for de azul
cv2.imshow("Imagem modificada", imagem)


