class Node:
    def __init__(self, data, name=''):
        self.data = data
        self.name = name
        self.next = None

    def __str__(self):
        return str(self.data)
