# qa_python

Тестирование класса BooksCollector
Описание
Набор тестов для проверки функциональности класса BooksCollector, который управляет коллекцией книг, их жанрами и списком избранных книг.

Структура тестов

1. Тесты добавления книг

test_add_one_book - проверка добавления одной книги

test_add_duplicate_books - проверка невозможности добавления дубликатов

test_case_sensitive_names - проверка чувствительности к регистру

test_book_name_validation - параметризованный тест валидации имен книг

2. Тесты с жанрами

test_age_rated_books_not_for_children - проверка фильтрации книг для детей

test_new_book_has_no_genre - проверка отсутствия жанра у новой книги

test_set_book_genre_success - проверка установки жанра

test_set_book_genre_for_nonexistent_book - проверка установки жанра несуществующей книге

test_set_invalid_genre - проверка установки несуществующего жанра

3. Тесты книг в Избранном

test_add_book_in_favorites - проверка добавления в Избранное

test_add_duplicate_to_favorites - проверка дублирования в Избранном

test_delete_book_from_favorites - проверка удаления из Избранного

test_get_list_of_favorites_books - проверка получения списка Избранного