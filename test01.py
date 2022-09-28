import cv2

img = cv2.imread("./img/p01.jpg")
cv2.imshow("圖1",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
