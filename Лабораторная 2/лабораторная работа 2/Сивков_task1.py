
BOOKS_DATABASE = [
    {
        "id": 1,
        "name": 'test_name_1',
        "pages": 200,
    },
    {
        "id": 2,
        "name": 'test_name_2',
        "pages": 400,
    }
]


class Book:
    def __init__(self, id_: int, name: str, pages: int):
        """

        :param id_:
        :param name:
        :param pages:
        #>>> Book(23, 'dd', 5)
        """
        if not isinstance(id_, int):
            raise TypeError("Введите идентификатор книги арабскими цифрами")
        self.id = id_
        if not isinstance(name, str):
            raise TypeError("Поместите название книги внуть '' или "" ")
        self.name = name
        if not isinstance(id_, int):
            raise TypeError("Введите количество страниц арабскими цифрами")
        self.pages = pages

    def __str__(self) -> str:
        """
        :return: название книги в формате: Книга "название"
        """
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        """
        :return: Список книг с их параметрами в читаемом формате
        """
        return f"{self.__class__.__name__}(id_={self.id}, name='{self.name}', pages={self.pages})"


# TODO написать класс Book


if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
