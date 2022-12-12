# TODO Написать 3 класса с документацией и аннотацией типов
from typing import Union


class Boys:
    def __init__(self, car: str, bench_press: int):
        """

            :param car: марка его машины
            :param bench_press: оценка спортивности
            >>> vlad = Boys('Lexus', 11)
            """

        if not isinstance(car, str):
            raise TypeError("Необходимо ввести марку авто с помощью букв")
        self.cars = car
        self.ask_what_car(car)
        if not isinstance(bench_press, int):
            raise TypeError
        if bench_press < 11:
            print('its worth pumping up')
        self.b_p = bench_press
        self.ask_how_many_bp(bench_press)

    def ask_what_car(self, car):
        """

        :param car: марка любимой машины
        :return: ориентировочная стоимость
        """
        ...
    def ask_how_many_bp(self, bench_press):
        """

        :param bench_press: физические возможности в подтягиваниях
        :return: возможность получить значек ГТО
        """
        ...


class Girls:
    def __init__(self, city: str, phone_number: Union[int, float]):
        """

            :param city: любимый город
            :param phone_number: номер телефона владелицы
            Example:
            >>> kate = Girls('Saint-Peterburg', 79210900000)
            """
        if not isinstance(city, str):
            raise TypeError("Необходимо ввести название города с помощью букв")
        self.city = city
        if not isinstance(phone_number, (int, float)):
            raise TypeError("Необходимо ввести номер только цифрами")
        if len(str(phone_number)) < 11:
            raise ValueError("В номере не хватает цифр")
        self.phone_number = phone_number


    def ask_city(self, city: str):
        """

        :param city: название города
        :return: количество букв в названии
        """
        ...

    def ask_phone_number(self, phone_number) -> bool:
        """

        :param phone_number: номер телефона
        :return: проверяет российский номер или нет
        """
        ...

class Country:
    def __init__(self, g_d_product: list, pop_size: list):
        self.gdp = g_d_product
        self.ps = pop_size
        self.temp_1() # g_d_product имя атрибута
        self.temp_2(pop_size)

    def temp_1(self) -> list: # g_d_product просто название
        """

        :param g_d_product: внутренний валовый продукт по годам
        :return: темпы прироста
        """
        hh = [(self.gdp[i+1]/self.gdp[i]) for i in range(len(self.gdp)-1)]
        return hh

    def temp_2(self, pop_size):
        """

        :param pop_size: численность населения
        :return: темпы прироста
        """
        ...

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    pass

    # TODO работоспособность экземпляров класса проверить с помощью doctest

