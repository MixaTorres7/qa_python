from main import BooksCollector
import pytest


class TestBooksCollector:

    # Фикстура для создания экземпляра коллектора перед каждым тестом
    @pytest.fixture
    def collector(self):
        return BooksCollector()

    # Тест 1: Добавление одной книги с валидным названием
    def test_add_new_book_valid_name_book_added(self, collector):
        collector.add_new_book('Гарри Поттер')
        assert 'Гарри Поттер' in collector.books_genre
        assert collector.books_genre['Гарри Поттер'] == ''

    # Тест 2: Проверка граничных значений длины названия книги
    @pytest.mark.parametrize('book_name, expected_count', [
        ('А' * 1, 1),      # минимальная длина
        ('А' * 40, 1),     # максимальная длина
        ('А' * 41, 0),     # превышение длины
        ('', 0),           # пустая строка
    ])
    def test_add_new_book_name_length_boundaries(self, collector, book_name, expected_count):
        collector.add_new_book(book_name)
        assert len(collector.books_genre) == expected_count

    # Тест 3: Невозможность добавления дубликата книги
    def test_add_new_book_duplicate_not_added(self, collector):
        collector.add_new_book('Дубликат')
        collector.add_new_book('Дубликат')
        assert len(collector.books_genre) == 1

    # Тест 4: Установка валидного жанра для существующей книги
    def test_set_book_genre_valid_data_genre_set(self, collector):
        collector.add_new_book('Метро 2033')
        collector.set_book_genre('Метро 2033', 'Фантастика')
        assert collector.books_genre['Метро 2033'] == 'Фантастика'

    # Тест 5: Невозможность установки несуществующего жанра
    def test_set_book_genre_invalid_genre_not_set(self, collector):
        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', 'Несуществующий жанр')
        assert collector.books_genre['Книга'] == ''

    # Тест 6: Получение жанра книги по имени
    def test_get_book_genre_returns_correct_genre(self, collector):
        collector.add_new_book('Книга')
        collector.books_genre['Книга'] = 'Комедии'
        assert collector.get_book_genre('Книга') == 'Комедии'

    # Тест 7: Получение списка книг с определенным жанром
    def test_get_books_with_specific_genre_returns_correct_books(self, collector):
        # Добавляем книги разных жанров
        collector.books_genre = {
            'Книга 1': 'Ужасы',
            'Книга 2': 'Ужасы', 
            'Книга 3': 'Фантастика',
            'Книга 4': ''
        }
        
        result = collector.get_books_with_specific_genre('Ужасы')
        assert result == ['Книга 1', 'Книга 2']

    # Тест 8: Получение словаря books_genre
    def test_get_books_genre_returns_current_dict(self, collector):
        test_books = {'Книга 1': 'Фантастика', 'Книга 2': 'Комедии'}
        collector.books_genre = test_books
        assert collector.get_books_genre() == test_books

    # Тест 9: Получение книг, подходящих для детей
    def test_get_books_for_children_returns_only_child_friendly_books(self, collector):
        collector.books_genre = {
            'Детская книга': 'Мультфильмы',
            'Страшная книга': 'Ужасы',
            'Фантастическая книга': 'Фантастика',
            'Книга без жанра': ''
        }
        
        children_books = collector.get_books_for_children()
        assert 'Детская книга' in children_books
        assert 'Фантастическая книга' in children_books
        assert 'Страшная книга' not in children_books
        assert 'Книга без жанра' not in children_books

    # Тест 10: Добавление книги в избранное
    def test_add_book_in_favorites_book_added_to_favorites(self, collector):
        collector.books_genre = {'Любимая книга': 'Фантастика'}
        collector.add_book_in_favorites('Любимая книга')
        assert 'Любимая книга' in collector.favorites

    # Тест 11: Удаление книги из избранного
    def test_delete_book_from_favorites_book_removed(self, collector):
        collector.favorites = ['Книга']
        collector.delete_book_from_favorites('Книга')
        assert 'Книга' not in collector.favorites

    # Тест 12: Получение списка избранных книг
    def test_get_list_of_favorites_books_returns_correct_list(self, collector):
        collector.favorites = ['Книга 1', 'Книга 2']
        favorites = collector.get_list_of_favorites_books()
        assert favorites == ['Книга 1', 'Книга 2']