import cv2
import numpy as np
import os
from glob import glob


menu = {
    1: "Apply_medianBlur",
    2: "Apply_linear_filter",
    3: "Apply blur",
    4: "Apply_Laplacian"
}


winNames = [
    "Initial image",
    "medianBlur",
    "filter2d",
    "blur",
    "Laplacian"
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
    cv2.imshow('filter2d', linear_image)
    cv2.waitKey()


def medianBlur(image):
    median_image = cv2.medianBlur(image, 5)
    cv2.imshow('medianBlur', median_image)
    cv2.waitKey()


def blur_demo(image):
	 #Среднее размытие: случайный шум имеет хороший шумоподавляющий эффект
	 #(1, 15) - размытие по вертикали, (15, 1) - размытие по горизонтали

    blur_image = cv2.blur(image, (1, 15))
    cv2.imshow("blur", blur_image)
    cv2.waitKey()


def Laplacian(image):
    s = cv2.Laplacian(image, cv2.CV_16S, ksize=3)
    s = cv2.convertScaleAbs(s)
    cv2.imshow("Laplacian", s)
    cv2.waitKey()


def main():
    img = Read_image()
    try:
        Menu_Num = int(input('Выберите пункт из меню'+ '\n'+ f'{menu}'+'\n'))
    except (ValueError):
        print('Пожалуйста, введите число')
        Menu_Num = int(input(f'{menu}' + '\n'))

    if Menu_Num == 1:
        medianBlur(img)
    elif Menu_Num == 2:
        linear_filter(img)
    elif Menu_Num == 3:
        blur_demo(img)
    elif Menu_Num == 4:
        Laplacian(img)
    main()

main()


