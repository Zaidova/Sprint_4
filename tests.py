import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2
    def test_set_book_genre_set_genre_success(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')

        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')

        assert collector.get_books_genre()['Гордость и предубеждение и зомби'] == 'Фантастика'

    def test_get_book_genre_get_genre_success(self):
        collector = BooksCollector()

        collector.books_genre['Гордость и предубеждение и зомби'] = 'Фантастика'

        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Фантастика'

    @pytest.mark.parametrize(
        'genre,books',
        [
            ['Фантастика', ['Гордость и предубеждение и зомби', 'Властелин колец']],
            ['Комедии', ['Ревизор']]
        ]
    )
    def test_get_books_with_specific_genre_get_fantastic_books_success(self, genre, books):
        collector = BooksCollector()

        collector.books_genre['Гордость и предубеждение и зомби'] = 'Фантастика'
        collector.books_genre['Властелин колец'] = 'Фантастика'
        collector.books_genre['Ревизор'] = 'Комедии'

        assert collector.get_books_with_specific_genre(genre) == books

    def test_get_books_genre_empty_dictionary(self):
        collector = BooksCollector()

        assert collector.get_books_genre() == {}

    def test_get_books_for_children_books_with_age_rating_not_for_children(self):
        collector = BooksCollector()

        collector.books_genre['Гордость и предубеждение и зомби'] = 'Фантастика'
        collector.books_genre['Оно'] = 'Ужасы'
        collector.books_genre['Ревизор'] = 'Комедии'

        assert collector.get_books_for_children() == ['Гордость и предубеждение и зомби', 'Ревизор']

    def test_add_book_in_favorites_not_add_again(self):
        collector = BooksCollector()

        collector.add_new_book('Евгений Онегин')
        collector.add_new_book('Букварь')

        collector.add_book_in_favorites('Евгений Онегин')
        collector.add_book_in_favorites('Букварь')
        collector.add_book_in_favorites('Евгений Онегин')

        assert len(collector.favorites) == 2

    def test_delete_book_from_favorites_delete_book(self):
        collector = BooksCollector()

        collector.add_new_book('Евгений Онегин')
        collector.add_new_book('Букварь')

        collector.add_book_in_favorites('Евгений Онегин')
        collector.add_book_in_favorites('Букварь')

        collector.delete_book_from_favorites('Букварь')

        assert collector.favorites == ['Евгений Онегин']

    def test_get_list_of_favorites_books_get_list_of_two_books(self):
        collector = BooksCollector()

        collector.add_new_book('Евгений Онегин')
        collector.add_new_book('Букварь')

        collector.add_book_in_favorites('Евгений Онегин')
        collector.add_book_in_favorites('Букварь')

        assert collector.get_list_of_favorites_books() == ['Евгений Онегин', 'Букварь']
