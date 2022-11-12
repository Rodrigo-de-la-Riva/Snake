class Node:
    def __init__(self, data, name='', snake_len=0):
        self.data = data
        self.name = name
        self.snake_len = snake_len
        self.next = None

    def __str__(self):
        return str(self.data)
