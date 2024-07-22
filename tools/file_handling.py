from os.path import exists


class File:
    def __init__(self, path):
        self.path = path

    def read_line(self):
        with open(self.path, "r") as file:
            lines = file.readlines()
        file.close()
        return lines

    def read(self):
        with open(self.path, "r") as file:
            line = file.read()
        return line

    def append(self, line):
        with open(self.path, "a") as file:
            file.write(line)
            file.write("\n")

    def is_exist(self):
        if exists(self.path):
            return True
        return False

    def create(self):
        with open(self.path, "x") as file:
            file.close()

    def write(self, line):
        with open(self.path, "w") as file:
            file.write(line)
