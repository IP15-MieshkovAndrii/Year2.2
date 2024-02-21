import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy.spatial import distance


def map_downloading(img_path):
    map_img = mpimg.imread(img_path)
    return map_img

def bubles(map_img, coords, population):
    fig, ax = plt.subplots(figsize=(15, 15))
    fig.suptitle('Ukraine', fontsize=16)
    ax.imshow(map_img)
    ax.scatter(
        coords[:, 0],
        coords[:, 1],
        s=population * 2,
        c='green',
        alpha=0.5,
        linewidth=2
    )
    ax.axis('off')

    plt.show()

def greatest_distance(map_img, cities, coords):
    distances = distance.cdist(coords, coords, 'euclidean')

    city_A, city_B = np.unravel_index(distances.argmax(), distances.shape)

    pixel_distance = distances[city_A, city_B]

    ukraine_width_km = 1316
    km_per_pixel = ukraine_width_km / map_img.shape[1]
    km_distance = distances[city_A, city_B] * km_per_pixel
    print(f'Найбільша відстань - між містами {cities[city_A]} та {cities[city_B]}.')
    print(f'Відстань у пікселях: {pixel_distance:.2f} пікселів')
    print(f'Відстань у кілометрах: {km_distance:.2f} км')


if __name__ == "__main__":
    #Додаткове завдання 1
    img_path = 'Ukraine.jpg'
    #Завантажемо карту
    map_img = map_downloading(img_path)
    #Розмістити бульбашки, що відповідають їх населенню, на довільних 5 містах 
    cities = ['Київ', 'Краматорськ', 'Харків', 'Львів', 'Миколаїв']
    cities_coords = np.array([(387, 146), (715, 256), (647, 176), (91, 188), (452, 381)])
    cities_population = np.array([2884, 185, 1419, 721, 486])
    bubles(map_img, cities_coords, cities_population)
    #Знайти найбільшу відстань між містами в пікселях та кілометрах
    greatest_distance(map_img, cities, cities_coords)
    