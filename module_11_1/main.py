"""
Выбранные библиотеки:
numpy
pillow
"""

# ПРИМЕР С numpy
import numpy as np

# Создание массивов
array_1 = np.array([9, 8, 7])
array_2 = np.arange(3)  # Создание одномерного массива от 0 до 3 [0, 1, 2]
array_3 = np.array([1, 1, 1])
print(array_1 + array_2 + array_3)

# Создание массива в определенном диапазоне с указанием количества элементов в нем
array = np.linspace(1, 20, 5)
print(array)

# Создание массива со случайными числами от 0 до 1 размером 2 х 2
array_random = np.random.rand(3, 3)
print(array_random)

# ПРИМЕР С pillow
from PIL import Image

image_path = 'image/cat.jpg'

# Функция, изменяющая размер изображения
def resize_image():
    image = Image.open(image_path)
    image = image.resize((2840, 1400))
    image.save(image_path)
    image.close()

# Функция, которая переворачивает изображение
def rotate_image():
    image = Image.open(image_path)
    image_rotate = image.rotate(180)
    image_rotate.save(image_path)
    image.close()

# изображение должно стать перевернутым и уменьшенным в размере
resize_image()
rotate_image()
