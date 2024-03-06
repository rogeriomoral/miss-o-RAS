import cv2
imagem = cv2.imread('C:\\Users\\roger\\Downloads\\barracadacidadelogo.jpg')
(b,g,r) = imagem[0,0]#cores do pix
print('O pixel (0, 0) tem as seguintes cores:')
print('Vermelho:', r, 'Verde:', g, 'Azul:', b)

