import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:


    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    # Тест на добавление одной книги
    def test_add_one_book(self, collector):
        collector.add_new_book("Властелин колец")
        assert "Властелин колец" in collector.books_genre
        assert collector.books_genre["Властелин колец"] == ""

    # Тест на невозможность добавления дубликата
    def test_add_duplicate_books(self, collector):
        book_name = "Властелин колец"
        collector.add_new_book(book_name)
        collector.add_new_book(book_name)
        assert len(collector.books_genre) == 1

    # Тест на добавление книги с разными регистрами
    def test_case_sensitive_names(self, collector):
        collector.add_new_book("книга")
        collector.add_new_book("Книга")
        collector.add_new_book("КНИГА")

        assert len(collector.books_genre) == 3

    # Тест на валидные/невалидные имена
    @pytest.mark.parametrize(
        "book_name, expected_result",
        [
            ("Война и мир", True),  # Обычное название
            ("A", True),  # Минимальная длина (1 символ)
            ("А" * 40, True),  # Максимальная длина (40 символов)
            ("Книга с !@#$%^&*", True),  # Спецсимволы
            ("1234567890", True),  # Цифры
            ("Книга с пробелами", True),  # Пробелы внутри строки
            ("А" * 41, False) # Слишком длинное (41 символ)
        ],
        ids=[
            "valid_normal_name",
            "valid_min_length",
            "valid_max_length",
            "valid_special_chars",
            "valid_numbers",
            "valid_internal_spaces",
            "invalid_too_long"
        ]
    )
    def test_book_name_validation(self, book_name, expected_result, collector):
        collector.add_new_book(book_name)

        if expected_result:
            assert book_name in collector.get_books_genre(), f"Книга '{book_name}' должна была добавиться"
        else:
            assert book_name not in collector.get_books_genre(), f"Книга '{book_name}' не должна была добавиться"

    # Тест: Книги с возрастным рейтингом отсутствуют в списке книг для детей
    @pytest.mark.parametrize("book_name, genre, should_be_for_children", [
        ("Русалочка", "Мультфильмы", True),  # Детский жанр
        ("Дракула", "Ужасы", False),  # Возрастной жанр
        ("Шерлок Холмс", "Детективы", False),  # Возрастной жанр
        ("Заводной апельсин", "", False),  # Без жанра
        ("Ревизор", "Комедии", True),  # Обычный жанр, без ограничений
    ], ids=[
        "children_genre",
        "horror_genre",
        "detective_genre",
        "no_genre",
        "allowed_genre"
    ])
    def test_age_rated_books_not_for_children(self, book_name, genre, should_be_for_children, collector):
        collector.add_new_book(book_name)
        if genre:
            collector.set_book_genre(book_name, genre)
        children_books = collector.get_books_for_children()

        assert (book_name in children_books) == should_be_for_children

    # Тест: У добавленной книги нет жанра
    def test_new_book_has_no_genre(self, collector):
        test_book_name = "Книга без жанра"
        collector.add_new_book(test_book_name)

        assert collector.get_book_genre(test_book_name) == "", (
            f"У новой книги '{test_book_name}' нет жанра")

    # Тест на добавление книги с жанром
    def test_set_book_genre_success(self, collector):
        collector.add_new_book('Метро 2033')
        collector.set_book_genre('Метро 2033', 'Фантастика')
        assert collector.get_book_genre('Метро 2033') == 'Фантастика'

    # Тест на добавление несуществующей книги
    def test_set_book_genre_for_nonexistent_book(self, collector):
        collector.set_book_genre('Несуществующая книга', 'Фантастика')
        assert 'Несуществующая книга' not in collector.books_genre

    # Тест на добавление книги с несуществующим жанром
    def test_set_invalid_genre(self, collector):
        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', 'Несуществующий жанр')
        assert collector.get_book_genre('Книга') == ''

    # Тест для получения жанра существующей книги
    @pytest.mark.parametrize("book_name, expected_genre", [
        ("Властелин колец", "Фантастика"),
        ("Дракула", "Ужасы"),
        ("Шерлок Холмс", "Детективы")
    ])
    def test_get_book_genre_existing_book(self, collector, book_name, expected_genre):
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, expected_genre)
        assert collector.get_book_genre(book_name) == expected_genre

    # Тест для книги без жанра
    def test_get_book_genre_book_without_genre(self, collector):
        collector.add_new_book("Книга без жанра")
        assert collector.get_book_genre("Книга без жанра") == ""

    # Тест для пустого словаря
    def test_empty_collector(self, collector):
        assert collector.get_books_genre() == {}

    # Тест для словаря с одной книгой
    def test_single_book_with_genre(self, collector):
        collector.add_new_book("Властелин колец")
        collector.set_book_genre("Властелин колец", "Фантастика")

    # Тест поиска книги по жанру
    def test_get_books_with_specific_genre(self, collector):
        collector.add_new_book("Дракула")
        collector.set_book_genre("Дракула", "Ужасы")

        assert collector.get_books_with_specific_genre("Ужасы") == ["Дракула"]

    # Тест на добавление книги в Избранное
    def test_add_book_in_favorites(self, collector):
        collector.add_new_book('Книга')
        collector.add_book_in_favorites('Книга')
        assert 'Книга' in collector.get_list_of_favorites_books()

    # Тест на добавление дубликата книги в Избранное
    def test_add_duplicate_to_favorites(self, collector):
        collector.add_new_book('Книга')
        collector.add_book_in_favorites('Книга')
        collector.add_book_in_favorites('Книга')
        assert len(collector.get_list_of_favorites_books()) == 1

    # Тест на удаление книги из Избранного
    def test_delete_book_from_favorites(self, collector):
        collector.add_new_book('Книга')
        collector.add_book_in_favorites('Книга')
        collector.delete_book_from_favorites('Книга')
        assert len(collector.get_list_of_favorites_books()) == 0

    # Тест на получения списка избранных книг
    def test_get_list_of_favorites_books(self, collector):
        collector.add_new_book('Книга 1')
        collector.add_new_book('Книга 2')
        collector.add_book_in_favorites('Книга 1')
        assert collector.get_list_of_favorites_books() == ['Книга 1']