from sys import stdin


class Matrix:
    def __init__(self, lines=list()):
        self.lines = lines.deepcopy()

    def __str__(self):
        return '\n'.join(
            ['\t'.join(['%d' % i for i in self.lines])])

    def size(self):
        sizepair = (len(self.lines), len(self.lines[0]))
        return sizepair


exec(stdin.read())
