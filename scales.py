notes = ["a", "a#", "b", "c", "c#", "d", "d#", "e", "f", "f#", "g", "g#"]


class Scale:
    def __init__(self, root):
        self.root = root
        
    def major(self):
        ind = notes.index(self.root)
        intervals = [0, 2, 4, 5, 7, 9, 11]
        return [notes[(ind+i)%12] for i in intervals]

    def minor(self):
            ind = notes.index(self.root)
            intervals = [0, 2, 3, 5, 7, 8, 10]
            return [notes[(ind+i)%12] for i in intervals]
    