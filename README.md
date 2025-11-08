# qa_python
Этот набор тестов покрывает все методы класса BooksCollector:

test_add_new_book_valid_name_book_added - проверяет добавление книги с валидным названием

test_set_book_genre_valid_data_genre_set - проверяет установку жанра для книги

test_get_books_with_specific_genre_returns_correct_books - проверяет получение книг по конкретному жанру

test_get_books_for_children_returns_only_child_friendly_books - проверяет, что возвращаются только книги без возрастного рейтинга

test_add_book_in_favorites_book_added_to_favorites - проверяет добавление книги в избранное

test_delete_book_from_favorites_book_removed - проверяет удаление книги из избранного

test_get_list_of_favorites_books_returns_correct_list - проверяет получение списка избранных книг

test_add_new_book_name_length_boundaries - параметризованный тест для проверки граничных значений длины названия

test_add_new_book_duplicate_not_added - проверяет, что дубликаты не добавляются

test_set_book_genre_invalid_genre_not_set - проверяет, что несуществующий жанр не устанавливается

Все тесты независимы и каждый создает свой экземпляр класса. Параметризация используется для тестирования разных длин названий книг.

-