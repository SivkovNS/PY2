class Book():
    """ Базовый класс книги. """
    def __init__(self, name: str = None, author: str = None):
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        if not isinstance(name, str):
            raise TypeError('Введите название, используя '' или ""')
        self._name = name

    @property
    def author(self) -> str:
        return self._author

    @author.setter
    def author(self, author: str) -> None:
        if not isinstance(author, str):
            raise TypeError('Введите автора, используя '' или ""')
        self._author = author


class PaperBook(Book):

    def __init__(self, name: str = None, author: str = None, pages: int = 1):
        super().__init__(name, author)
        self._pages = pages

    def __str__(self):
        return f"Книга {self._name!r}. Автор {self._author}. Страниц {self._pages!r}"

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, pages: int) -> None:
        """
        :param pages:
        Новое значение количества страниц проверяется по типу данных и по значению
        """
        if not isinstance(pages, int):
            raise TypeError('Укажите количество страниц арабскими цифрами')
        if pages < 1:
            raise ValueError('Введите целое число, которое больше нуля')
        self._pages = pages

class AudioBook(Book):
    def __init__(self, duration: float = 1):
        super().__init__()
        self._duration = duration

    def __str__(self):
        return f"Книга {self._name!r}. Автор {self._author}. Длительность (часов) {self._duration}"

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, duration: float) -> None:
        """
        :param duration:
        проверка, выполняемая при установке нового значения продолжительности
        """
        if not isinstance(duration, float):
            raise TypeError('Укажите длительность арабскими цифрами (разделитель точка)')
        if duration < 1:
            raise ValueError('Введите число, которое больше нуля (разделитель - точка')
        self._duration = duration

if __name__ == "__main__":
    b = Book()
    pb = PaperBook()
    eb = AudioBook()
    print(b)
    print(pb)
    # print(pb.name)
    # print(eb)
    # pb.pages = -3
    # print(pb.pages)

