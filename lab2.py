import cv2
import numpy as np
import os
from glob import glob


menu = {
    1: "Apply_linear_filter",
    2: "Apply_blur",
    3: "Apply_medianBlur",
    4: "Apply_GaussianBlur",
    5: "Apply_erode",
    6: "Apply_dilate",
    7: "Apply_Sobel",
    8: "Apply_Laplacian",
    9: "Apply_Canny",
    10: "Apply_calcHist",
    11: "Apply_equalizeHist"
}


winNames = [
    "Initial image",
    "filter2d",
    "blur",
    "medianBlur",
    "GaussianBlur",
    "erode",
    "dilate",
    "Sobel",
    "Laplacian",
    "Canny",
    "calcHist",
    "equalizeHist"
]


#список изображений в пути
def getfiles(dirname):
    dirfiles = glob(os.path.join(dirname, '*.jpg'))
    return [i.split('\\')[1] for i in dirfiles]

pictures = getfiles('pictures')

def Read_image():
    PictureName = input(f'Введите название изображения из списка {pictures}: ')
    img = cv2.imread(f'pictures\\{PictureName}')
    #imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    #cv2.imshow(PictureName, img)
    #cv2.waitKey()
    return img


def linear_filter(image):
    kernel =np.array([
        [-0.1, 0.2, -0.1],
        [0.2, 3.0, 0.2],
        [-0.1, 0.2, -0.1]
    ])
    linear_image = cv2.filter2D(image, -1, kernel)
    cv2.imshow('linear_filter', linear_image)
    cv2.waitKey()


def main():
    img = Read_image()
    try:
        Menu_Num = int(input('Выберите пункт из меню'+ '\n'+ f'{menu}'+'\n'))
    except (ValueError):
        print('Пожалуйста, введите число')
        Menu_Num = int(input(f'{menu}' + '\n'))

    if Menu_Num == 1:
        linear_filter(img)
    elif Menu_Num == 2:
        pass
    main()

main()


