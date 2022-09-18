import cv2
import numpy as np
import os
from glob import glob


menu = {
    1: "Apply_medianBlur",
    2: "Apply_linear_filter",
    3: "Apply blur",
    4: "Apply_Laplacian",
    5: "Draw_figures"
}

figure_menu = {
    1: 'line',
    2: 'rectangle',
    3: 'circle',
    4: 'ellipse'
}


#список изображений в пути
def getfiles(dirname):
    dirfiles = glob(os.path.join(dirname, '*.jpg'))
    return [i.split('\\')[1] for i in dirfiles]


pictures = getfiles('pictures')


def Read_image():
    PictureName = input(f'Введите название изображения из списка {pictures}: ')
    img = cv2.imread(f'pictures\\{PictureName}')
    return img


def show_save(WinName, img):
    cv2.imshow(WinName, img)
    cv2.waitKey()
    Save_results(img)


def linear_filter(image):
    kernel =np.array([
        [-0.1, 0.2, -0.1],
        [0.2, 3.0, 0.2],
        [-0.1, 0.2, -0.1]
    ])
    linear_image = cv2.filter2D(image, -1, kernel)
    show_save('filter2d', linear_image)


def medianBlur(image):
    median_image = cv2.medianBlur(image, 5)
    show_save('medianBlur', median_image)


def blur_demo(image):
	 #Среднее размытие: случайный шум имеет хороший шумоподавляющий эффект
	 #(1, 15) - размытие по вертикали, (15, 1) - размытие по горизонтали

    blur_image = cv2.blur(image, (1, 15))
    show_save("blur", blur_image)


def Laplacian(image):
    s = cv2.Laplacian(image, cv2.CV_16S, ksize=3)
    s = cv2.convertScaleAbs(s)
    show_save("Laplacian", s)


def draw_line(img):
    img_line = cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)
    show_save("line", img_line)


def draw_rectangle(img):
    img_rectangle = cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)
    show_save("rectangle", img_rectangle)


def draw_circle(img):
    img_circle = cv2.circle(img, (447, 63), 63, (0, 0, 255), -1)
    show_save("circle", img_circle)


def draw_ellipse(img):
    img_ellipse = cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 360, 255, -1)
    show_save("ellipse", img_ellipse)


def Save_results(result_image):
    action = input('Хотите ли Вы сохранить результат? (Y/N)\n').lower()
    if action == 'y':
        format = input('Выберите формат изображения (jpg, png) \n').lower()
        name = input('Введите название файла\n')
        filename = f'results\\{name}.{format}'
        cv2.imwrite(filename, result_image)
    else:
        pass


def Figure_choosing(img):
    try:
        Figure_Num = int(input(f'Выберите пункт из меню\n{figure_menu}\n'))
    except (ValueError):
        print('Пожалуйста, введите число')
        Figure_Num = int(input(f'{figure_menu}\n'))
    if Figure_Num == 1:
        draw_line(img)
    elif Figure_Num == 2:
        draw_rectangle(img)
    elif Figure_Num == 3:
        draw_circle(img)
    elif Figure_Num == 4:
        draw_ellipse(img)
    main()


def main():
    img = Read_image()
    try:
        Menu_Num = int(input(f'Выберите пункт из меню\n{menu}\n'))
    except (ValueError):
        print('Пожалуйста, введите число')
        Menu_Num = int(input(f'{menu}\n'))

    if Menu_Num == 1:
        medianBlur(img)
    elif Menu_Num == 2:
        linear_filter(img)
    elif Menu_Num == 3:
        blur_demo(img)
    elif Menu_Num == 4:
        Laplacian(img)
    elif Menu_Num == 5:
        Figure_choosing(img)
    main()

main()