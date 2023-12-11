import unittest
from unittest.mock import patch
from statistics import read_file, compute_stats, main


class StatsFileTests(unittest.TestCase):

    #тесты на чтение файла
    def test_read_file_existing_file(self):
        content = read_file('temp_test_file.txt')
        self.assertEqual(content, "This is a test file. It contains words and characters.")

    def test_read_file_nonexistent_file(self):
        with patch('builtins.print') as mock_print:
            read_file('nonexistent_file.txt')
            mock_print.assert_called_with("Ошибка: Файл 'nonexistent_file.txt' не найден.")

    def test_read_file_permission_error(self):
        with patch('builtins.print') as mock_print:
            with patch('builtins.open', side_effect=PermissionError):
                read_file('temp_test_file.txt')
                mock_print.assert_called_with(f"Ошибка: Нет разрешения на чтение файла 'temp_test_file.txt'.")

    def test_read_file_exception_error(self):
        with patch('builtins.print') as mock_print:
            with patch('builtins.open', side_effect=Exception("Something went wrong")):
                read_file('temp_test_file.txt')
                mock_print.assert_called_with(f"Ошибка при чтении файла 'temp_test_file.txt': Something went wrong.")


    #тесты на подсчет статистики
    def test_compute_stats(self):
        content = "This is a test file. It contains words and characters."
        result = compute_stats(content)
        self.assertEqual(result, ('this', 10, 54))

    def test_compute_stats_with_hyphens(self):
        content = "rock-n-roll and r-n-b"
        result = compute_stats(content)
        self.assertEqual(result, ('rock-n-roll', 3, 21))

    def test_compute_stats_with_apostrophes(self):
        content = "rock'n'roll and r'n'b"
        result = compute_stats(content)
        self.assertEqual(result, ('rock\'n\'roll', 3, 21))

    def test_compute_stats_with_apostrophes_and_hyphens(self):
        content = "rock-n'roll and r-n-n'n'b"
        result = compute_stats(content)
        self.assertEqual(result, ('rock-n\'roll', 3, 25))

    def test_compute_stats_with_single_letter(self):
        content = "Я в А, а ты в В?"
        result = compute_stats(content)
        self.assertEqual(result, ('в', 7, 16))

    def test_compute_stats_with_other_punctuation(self):
        content = "This is one word - \"WORD\". But this is two words: 'wo.rd'.\nAnd this is also two words:\t wor\"ds"
        result = compute_stats(content)
        self.assertEqual(result, ('this', 20, 94))

    def test_compute_stats_empty_content(self):
        result = compute_stats(None)
        self.assertIsNone(result)


    #тесты основной функции
    def test_main_with_existing_file(self):
        with patch('builtins.print') as mock_print:
            main('temp_test_file.txt')
            mock_print.assert_called_with("Самое часто встречающееся слово: this\n"
                                          "Количество слов: 10\n"
                                          "Количество символов: 54")

    def test_main_with_nonexistent_file(self):
        with patch('builtins.print') as mock_print:
            main('nonexistent_file.txt')
            mock_print.assert_called_with("Ошибка: Файл 'nonexistent_file.txt' не найден.")

    def test_main_with_file_permission_error(self):
        with patch('builtins.print') as mock_print:
            with patch('builtins.open', side_effect=PermissionError):
                main('temp_test_file.txt')
                mock_print.assert_called_with(f"Ошибка: Нет разрешения на чтение файла 'temp_test_file.txt'.")

    def test_main_with_file_exception_error(self):
        with patch('builtins.print') as mock_print:
            with patch('builtins.open', side_effect=Exception("Something went wrong")):
                main('temp_test_file.txt')
                mock_print.assert_called_with(f"Ошибка при чтении файла 'temp_test_file.txt': Something went wrong.")


if __name__ == '__main__':
    unittest.main()
