#import library
import cv2
from matplotlib import pyplot as plt

#membaca/memasukan gambar
img = cv2.imread('kiwi.jpg')

#mengubah gambar/citra ke HSV
hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

#tampilkan
plt.subplot(1, 2, 1)
plt.title("Citra Asli")
plt.imshow(img)
plt.subplot(1, 2, 2)
plt.title("Citra HSV")
plt.imshow(hsv)
plt.show()