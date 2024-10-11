import string

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names
        self.all_words = {}

    def get_all_words(self):
        for file_name in self.file_names:
            words_list = []

            with open(file_name, 'r') as file:
                for line in file:
                    line = line.lower()
                    line = line.translate(str.maketrans('', '', string.punctuation))  # удаление пунктуации
                    words = line.split()
                    words_list.extend(words)

            self.all_words[file_name] = words_list

        return self.all_words

    def find(self, word):
        positions = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                positions[name] = words.index(word.lower()) + 1

        return positions

    def count(self, word):
        counts = {}
        for name, words in self.get_all_words().items():
            count = words.count(word.lower())
            counts[name] = count

        return counts

# Пример выполнения
finder = WordsFinder('test_file.txt')
print(finder.get_all_words())
print(finder.find('TEXT'))
print(finder.count('teXT'))
