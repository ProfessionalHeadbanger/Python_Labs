import argparse
import sys
import re
from collections import Counter


def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"Ошибка: Файл '{file_path}' не найден.")
    except PermissionError:
        print(f"Ошибка: Нет разрешения на чтение файла '{file_path}'.")
    except Exception as e:
        print(f"Ошибка при чтении файла '{file_path}': {str(e)}.")
    return None


def compute_stats(content):
    if content is not None:
        num_characters = len(content)
        words = re.findall(r"\b(?:\w+['-]?)+\w*\b", content.lower())
        num_words = len(words)
        most_frequent_word = Counter(words).most_common(1)[0][0]
        return most_frequent_word, num_words, num_characters
    return None


def main(file_path):
    file_content = read_file(file_path)
    result = compute_stats(file_content)
    if result:
        most_frequent_word, num_words, num_characters = result
        print(f"Самое часто встречающееся слово: {most_frequent_word}\n"
              f"Количество слов: {num_words}\n"
              f"Количество символов: {num_characters}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Ошибка: требуется один аргумент - путь к файлу")
        sys.exit(1)
    parser = argparse.ArgumentParser(description='Вычисление статистики содержимого текстового файла')
    parser.add_argument('file', metavar='file', type=str, help='Путь к файлу')
    args = parser.parse_args()
    main(args.file)

