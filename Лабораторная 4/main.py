# Создано консольное приложение, позволяющее расчитать расход топлива
# для двух типов авто: грузового и легкового

list_of_right_answers = ['да', ' да', 'Да', ' Да']
engine = input('В данном устройстве есть двигатель и хотя бы 4 колеса? ')

if engine in list_of_right_answers:

    class Cars:
        def __init__(self, eng: str = 'Двигатель присутствует', tank: str = 'Бак присутствует'):
            """
            Создается базовый класс Автомобили с двумя атрибутами
            :param eng: Показывает, что у объектов данного класса есть двигатель
            :param tank: Показывает, что у объектов данного класса есть топливный бак
            """
            self.availibility_of_engine = eng
            self.availibility_of_buck = tank

        def __str__(self):
            return f'{self.__class__.__name__}'

        def __repr__(self):
            return f'{self.availibility_of_engine}, {self.availibility_of_buck}'

        def action1(self, fuel_1path: float = 1) -> float:
            """
            Метод предназначен для расчета количества топлива, необходимого для
            преодоления введенного пользователем расстоянием
            :param fuel_1path: Расход топлива в литрах на один километр
            :return: расход топлива (литров)
            """
            path = input('Введити расстояние, которое нужно преодолеть (км): ')
            if float(path) < 0:
                raise ValueError('Введите число, которое больше нуля (разделитель - точка')
            waste_ = float(path) * fuel_1path
            return waste_

    c_p = input('Для управления данным авто нужны права категории С? ')

    if c_p in list_of_right_answers:
        class Trucks(Cars):
            def __init__(self, cargo_platform: str = 'Грузовой кузов присутствует'):
                """
                Создается дочерний класс Грузовики с одним атрибутум
                :param cargo_platform: Показывает наличие грузового кузова
                """
                super().__init__()
                self.availibility_of_platform = cargo_platform

            def __str__(self):
                return f'Это грузовой автомобиль'

            def action1(self, fuel: float = 0.35) -> float:
                """
                Перегруженный метод вычисления расхода топлива, поскольку
                грузовые автомобили имеют свой собственный расход топлива
                :param fuel: новое значение расхода топлива (литров на 1 км)
                :return: расход топлива в литрах
                """
                aa = super().action1()
                return round(aa * fuel, 3)


        truck_car = Trucks()
        print(truck_car)
        tt = input('Хотите расчитать расход топлива? ')

        # Условие, реализующее возможность вычисления расхода топлива
        if tt in list_of_right_answers:
            print(f'Потребуется {truck_car.action1()} литров топлива')
        else:
            print('До новых встреч!')

    else:
        e_p = input('Для управления данным авто нужны права категории В? ')
        if e_p in list_of_right_answers:
            class PasCars(Cars):
                def __init__(self, passagers_seats: str = 'присутствуют'):
                    super().__init__()
                    self.p_s = passagers_seats

                def __str__(self):
                    return f'Это легковой автомобиль'

            pas_car = PasCars()
            print(pas_car)
            tt = input('Хотите расчитать расход топлива? ')

            if tt in list_of_right_answers:
                print(f'Потребуется {pas_car.action1()} литров топлива')
            else:
                print('До новых встреч!')

        else:
            print('К сожалению, я пока что знаю только такие авто')


else:
    print('Увы, но ваше устройство не является автомобилем')
