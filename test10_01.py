import cv2
import numpy as np
img1 = cv2.imread("./img/test4.jpg", 1)  # (flag = 0 or 1 or -1)
imggray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
ret, img = cv2.threshold(imggray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow("threshold", img)
# 找輪廓
contours, hierarchy = cv2.findContours(img,
                                       cv2.RETR_TREE,
                                       cv2.CHAIN_APPROX_SIMPLE)
color1 = (255, 255, 0)

# 設定感興趣的contour
contour = contours[17]

# 極點座標
fin = img1.copy()
cnt = contour
left = tuple(cnt[cnt[:, :, 0].argmin()][0])
right = tuple(cnt[cnt[:, :, 0].argmax()][0])
top = tuple(cnt[cnt[:, :, 1].argmin()][0])
bottom = tuple(cnt[cnt[:, :, 1].argmax()][0])
print("最左點 ", left)
print("最右點 ", right)
print("最上點 ", top)
print("最下點 ", bottom)
dst11 = cv2.circle(fin, left, 5, [0, 255, 0], -1)
dst11 = cv2.circle(fin, right, 5, [0, 255, 0], -1)
dst11 = cv2.circle(fin, top, 5, [0, 255, 255], -1)
dst11 = cv2.circle(fin, bottom, 5, [0, 255, 255], -1)
# cv2.imshow("most", dst11)
for i in range(len(contours)):
    a = cv2.contourArea(contours[i])
    if (2000 <= a <= 9000):
        dst11 = cv2.drawContours(fin,contours,i,color1,3)
        print(i,a)

cv2.imshow("most", dst11)
cv2.waitKey(0)
cv2.destroyAllWindows()