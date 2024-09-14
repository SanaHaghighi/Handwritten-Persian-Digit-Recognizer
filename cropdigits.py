import cv2

image = cv2.imread('.\mnist2.jpg', 0)
height, width = image.shape
row_up = 108
row_down = 160
column_left = 180
column_right = 240
size = 60

n = 10
m = 17
for i in range(9,10):
    print(f"---------------------------------------------{i}---------------------------------------------")
    for j in range(0, m + 1):
        print(j)
        name = j + 18 # for mnist 2
        cv2.imwrite(f'./mnist_dataset/{i}/{name}.jpg', 
                    image[row_up + j * size - (3*j if j >= 2  else 0)  :row_down + j * size -  (4 * j if j<=11 else 2*j) - 4,
                          column_left + i * size - (i if j >= 4 else 0) :column_right + i * size - (i if j >= 4 else 0)])
