import pytest
from conftest import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_all_pets(my_pets):
# присутствуют все питомцы 1
    WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".\\.col-sm-4.left")))
# статистика
    statistic = pytest.driver.find_elements(By.CSS_SELECTOR, ".\\.col-sm-4.left")
    WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))
# cохраняем в переменную pets элементы карточек питомцев
    data_pets = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')
# получаем количество питомцев из статистики
    number = statistic[0].text.split('\n')
    number = number[1].split(' ')
    number = int(number[1])
# получаем количество карточек
    num_cards = len(data_pets)
# Проверяем, что количество питомцев из статистики совпадает с количеством карточек питомцев
    assert number == num_cards


def test_pets_photo(my_pets):
# у половины питомцев есть фото 2
    pytest.driver.implicitly_wait(10)
# статистика
    statistic = pytest.driver.find_elements(By.CSS_SELECTOR, ".\\.col-sm-4.left")
# сохраняем images как img
    images = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover img')
# ищем половину
    number = statistic[0].text.split('\n')
    number = number[1].split(' ')
    number = int(number[1])
    polovina = number / 2
#количество кол-во питомцев с фотографией
    number_photos = 0
    for i in range(len(images)):
        if images[i].get_attribute('src') != '':
            number_photos += 1

    assert number_photos >= polovina


def test_name_age_breed(my_pets):
#у всех питомцев есть имя, возраст и порода
    pytest.driver.implicitly_wait(10)
#создаем переменную data_pets для элементов с данными о питомцах
    data_pets = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')
    for i in range(len(data_pets)):
        all_info = data_pets[i].text.replace('\n', '').replace('×', '').split(' ')
        assert len(all_info) == 3
        print(all_info)


def test_name_age_breed(my_pets):
#у всех питомцев есть имя, возраст и порода
    pytest.driver.implicitly_wait(10)
    names = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-title')
    descriptions = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-text')

    for i in range(len(names)):
        assert names[i].text != ''
        assert descriptions[i].text != ''
        assert ', ' in descriptions[i]
        parts = descriptions[i].text.split(", ")
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0


def test_different_names(my_pets):
# у всех питомцев разные имена 3
    pytest.driver.implicitly_wait(10)
# сохраняем в переменную data_pets элементы с данными о питомцах
    data_pets = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')
    name_pets = []
    for i in range(len(data_pets)):
        name_pets.append(data_pets[i].text.replace('\n', '').split(' ')[0])
    set_name_pets = set(name_pets)
# если равно, то карточки с одинаковыми именами отсутствуют
    assert len(name_pets) == len(set_name_pets)


def test_no_duplicate_pets(my_pets):
# на странице со списком моих питомцев нет повторяющихся питомцев 4
    pytest.driver.implicitly_wait(10)
# сохраняем в переменную data_pets элементы с данными о питомцах
    data_pets = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')
    name_pets = []
    for i in range(len(data_pets)):
        name_pets.append(data_pets[i].text.replace('\n', '').replace('×', '').split(' '))
# сохраняем имя, возраст, породу из списка list_data и разделяем пробелом;
    row = ''
    for i in name_pets:
        row += ''.join(i)
        row += ' '
# получаем список
    list_row = row.split()
# превращаем list в set
    set_list_row = set(list_row)
# если равно, то карточки с одинаковыми данными отсутствуют
    assert len(set_list_row) == len(list_row)