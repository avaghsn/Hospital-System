from Final.data_structures.trie import Trie
from Final.tools.file_handling import File


class Cities:
    def __init__(self):
        self.cities = Trie()
        self.load()

    def load(self):
        path = "C:\\Users\\AVA\\PycharmProjects\\pythonProject\\Data_Structure\\Final\\test_files\\Cities.txt"
        cities = File(path).read_line()

        for city in cities:
            name = city.replace("\n", "")
            self.cities.insert(name)

    def save_data(self):
        path = "C:\\Users\\AVA\\PycharmProjects\\pythonProject\\Data_Structure\\Final\\test_files\\Cities.txt"
        file = File(path)
        file.write("")
        words = self.cities.get_all_words()
        while not words.is_empty():
            word = words.dequeue()
            file.append(word)

    def add_city(self, name):
        if self.cities.search(name):
            return False
        else:
            self.cities.insert(name)
            return True

    def get_cities(self):
        return self.cities

    def validate(self, name):
        if self.cities.starts_with(name):
            return True
        return False
