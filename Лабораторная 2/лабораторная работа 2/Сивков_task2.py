from pydantic import BaseModel, conint

BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book


class Book(BaseModel):
    id_: conint(gt=0)  # порядковый номер больше нуля
    name: str
    pages: int
    """
    проверка данных на адекватность с помощью модуля pydantic
    """

# TODO написать класс Library


class Library:
    def __init__(self, books=None):
        self.books = {} if books is None else books

    def get_next_book_id(self, name=None) -> str:
        """
        :param
        name: Название книги
        :return: Идентификатор новой книги
        """
        if name in list(self.books):
            print('Данная книга уже есть в библиотеке')
        else:
            Book.id_ = len(list(self.books)) + 1

        return f'{Book.id_}'

    def get_index_by_book_id(self, id_: int) -> str:
        """
        :param id_: идентификатор книги
        :return:
        """
        spisok = list(self.books)
        if id_ <= len(spisok):
            needed_book = spisok[id_-1]
            index_of_list = id_-1
            #return f'Индекс списка: {index_of_list}, Параметры книги: {needed_book!r}'
            return index_of_list
        else:
            raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
