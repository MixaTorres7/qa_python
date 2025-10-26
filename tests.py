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
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    
    
from main import BooksCollector
import pytest


class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    # Тест для add_new_book - добавление книги с валидным названием
    def test_add_new_book_valid_name_book_added(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        assert 'Гарри Поттер' in collector.get_books_genre()
        assert collector.get_book_genre('Гарри Поттер') == ''

    # Тест для set_book_genre - установка жанра для существующей книги
    def test_set_book_genre_valid_data_genre_set(self):
        collector = BooksCollector()
        collector.add_new_book('Метро 2033')
        collector.set_book_genre('Метро 2033', 'Фантастика')
        assert collector.get_book_genre('Метро 2033') == 'Фантастика'

    # Тест для get_books_with_specific_genre - получение книг по жанру
    def test_get_books_with_specific_genre_returns_correct_books(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        collector.add_new_book('Книга 2')
        collector.set_book_genre('Книга 1', 'Ужасы')
        collector.set_book_genre('Книга 2', 'Ужасы')
        
        result = collector.get_books_with_specific_genre('Ужасы')
        assert 'Книга 1' in result
        assert 'Книга 2' in result
        assert len(result) == 2

    # Тест для get_books_for_children - книги без возрастного рейтинга
    def test_get_books_for_children_returns_only_child_friendly_books(self):
        collector = BooksCollector()
        collector.add_new_book('Детская книга')
        collector.add_new_book('Страшная книга')
        collector.set_book_genre('Детская книга', 'Мультфильмы')
        collector.set_book_genre('Страшная книга', 'Ужасы')
        
        children_books = collector.get_books_for_children()
        assert 'Детская книга' in children_books
        assert 'Страшная книга' not in children_books

    # Тест для add_book_in_favorites - добавление в избранное
    def test_add_book_in_favorites_book_added_to_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Любимая книга')
        collector.add_book_in_favorites('Любимая книга')
        assert 'Любимая книга' in collector.get_list_of_favorites_books()

    # Тест для delete_book_from_favorites - удаление из избранного
    def test_delete_book_from_favorites_book_removed(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.add_book_in_favorites('Книга')
        collector.delete_book_from_favorites('Книга')
        assert 'Книга' not in collector.get_list_of_favorites_books()

    # Тест для get_list_of_favorites_books - получение списка избранного
    def test_get_list_of_favorites_books_returns_correct_list(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        collector.add_new_book('Книга 2')
        collector.add_book_in_favorites('Книга 1')
        
        favorites = collector.get_list_of_favorites_books()
        assert 'Книга 1' in favorites
        assert 'Книга 2' not in favorites

    # Параметризованный тест для проверки граничных значений длины названия
    @pytest.mark.parametrize('book_name, expected_count', [
        ('А' * 1, 1),      # 1 символ - должно добавиться
        ('А' * 40, 1),     # 40 символов - должно добавиться  
        ('А' * 41, 0),     # 41 символ - не должно добавиться
        ('', 0),           # пустая строка - не должно добавиться
    ])
    def test_add_new_book_name_length_boundaries(self, book_name, expected_count):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert len(collector.get_books_genre()) == expected_count

    # Тест для проверки, что нельзя добавить дубликат книги
    def test_add_new_book_duplicate_not_added(self):
        collector = BooksCollector()
        collector.add_new_book('Дубликат')
        collector.add_new_book('Дубликат')
        assert len(collector.get_books_genre()) == 1

    # Тест для проверки, что нельзя установить несуществующий жанр
    def test_set_book_genre_invalid_genre_not_set(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', 'Несуществующий жанр')
        assert collector.get_book_genre('Книга') == ''