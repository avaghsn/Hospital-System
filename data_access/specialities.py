from data_structures.trie import Trie
from tools.file_handling import File


class Specialities:
    def __init__(self):
        self.specialities = Trie()
        self.load()

    def load(self):
        path = "test_files/Specialties.txt"
        cities = File(path).read_line()

        for city in cities:
            name = city.replace("\n", "")
            self.specialities.insert(name)

    def save_data(self):
        path = "test_files/Specialties.txt"
        file = File(path)
        file.write("")
        words = self.specialities.get_all_words()
        while not words.is_empty():
            word = words.dequeue()
            file.append(word)

    def add_speciality(self, name):
        if self.specialities.search(name):
            return False
        else:
            self.specialities.insert(name)
            return True

    def get_specialities(self):
        return self.specialities

    def validate(self, name):
        if self.specialities.starts_with(name):
            return True
        return False
