# qa_python

Тестирование класса BooksCollector
Описание
Набор тестов для проверки функциональности класса BooksCollector, который управляет коллекцией книг, их жанрами и списком избранных книг.

Структура тестов

1. Тесты добавления книг

- `test_add_one_book` - проверка добавления одной книги
- `test_add_duplicate_books` - проверка невозможности добавления дубликатов
- `test_case_sensitive_names` - проверка чувствительности к регистру
- `test_book_name_validation` - параметризованный тест валидации имен книг
- `test_add_empty_or_whitespace_name` - проверка добавления книг с пустыми именами или пробелами
- `test_add_book_with_min_max_length` - проверка граничных значений длины имени книги

2. Тесты работы с жанрами

- `test_age_rated_books_not_for_children` - проверка фильтрации книг для детей
- `test_new_book_has_no_genre` - проверка отсутствия жанра у новой книги
- `test_set_book_genre_success` - проверка установки жанра
- `test_set_book_genre_for_nonexistent_book` - проверка установки жанра несуществующей книге
- `test_set_invalid_genre` - проверка установки несуществующего жанра
- `test_case_insensitive_genre` - проверка чувствительности к регистру при установке жанра
- `test_get_books_with_specific_genre` - проверка получения книг по жанру
- `test_get_books_with_empty_genre_list` - проверка получения книг по несуществующему жанру
- `test_books_without_genre_not_for_children` - проверка книг без жанра в списке для детей

3. Тесты работы с Избранным

- `test_add_book_in_favorites` - проверка добавления в Избранное
- `test_add_duplicate_to_favorites` - проверка дублирования в Избранном
- `test_delete_book_from_favorites` - проверка удаления из Избранного
- `test_delete_nonexistent_book_from_favorites` - проверка удаления несуществующей книги из Избранного
- `test_get_list_of_favorites_books` - проверка получения списка Избранного
- `test_add_to_favorites_nonexistent_book` - проверка добавления несуществующей книги в Избранное

4. Дополнительные тесты

- `test_empty_collector` - проверка работы с пустой коллекцией
- `test_single_book_with_genre` - проверка работы с коллекцией из одной книги
- `test_get_book_genre_existing_book` - проверка получения жанра существующей книги
- `test_get_book_genre_book_without_genre` - проверка получения жанра для книги без жанра
- `test_get_book_genre_nonexistent_book` - проверка получения жанра несуществующей книги
- `test_get_books_genre` - проверка получения всего словаря книг