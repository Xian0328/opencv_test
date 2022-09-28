# OpenCV的影像梯度與邊緣偵測
# 讀圖
import cv2
import numpy as np
img1 = cv2.imread("./img/p02.jpg", 0)  # (flag = 0 or 1 or -1)
ret, img = cv2.threshold(img1, 150, 255, cv2.THRESH_BINARY)
cv2.imshow("img", img)

# Canny邊緣偵測
canny1 = cv2.Canny(img1, 30, 100)
cv2.imshow("canny1", canny1)
canny2 = cv2.Canny(img1, 50, 200)
cv2.imshow("canny2", canny2)
canny3 = cv2.Canny(img1, 100, 200)
cv2.imshow("canny3", canny3)

cv2.waitKey(0)
cv2.destroyAllWindows()