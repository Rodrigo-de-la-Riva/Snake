class Node:
    def __init__(self, data, snake_len, name=''):
        self.data = data
        self.name = name
        self.snake_len = snake_len
        self.next = None

    def __str__(self):
        return str(self.data)
